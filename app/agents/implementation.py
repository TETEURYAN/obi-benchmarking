import os
from typing import Dict, List, Any
from haystack import Pipeline
from haystack.components.builders import PromptBuilder
from haystack.components.generators.chat import OpenAIChatGenerator
from haystack.dataclasses import ChatMessage
from haystack.utils import Secret
from pydantic import BaseModel, Field

class ImplementationStatus(BaseModel):
    is_correct: bool = Field(description="Whether the user code passes all test cases and aligns with the plan.")
    feedback: str = Field(description="Helpful tips and guidance for the student based on their code and errors.")

class ImplementationAgent:
    def __init__(self, model: str = None, api_key: str = None, base_url: str = None):
        self.model = model or os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.base_url = base_url or os.getenv("OPENAI_BASE_URL")
        
        # Generator for structured output
        self.generator = OpenAIChatGenerator(
            model=self.model,
            api_key=Secret.from_token(self.api_key) if self.api_key else None,
            api_base_url=self.base_url,
            generation_kwargs={"response_format": {"type": "json_object"}}
        )

        self.prompt_builder = PromptBuilder(template="""
        Você é um tutor especialista ajudando um estudante a implementar sua solução em código usando o método de Pólya.
        O estudante já entendeu o problema e elaborou um plano.
        Agora, eles estão escrevendo código e você deve fornecer dicas com base no progresso e nos resultados dos testes.
        NÃO forneça a solução completa. Dê dicas pequenas e acionáveis.

        Problema: {{problem_description}}
        Plano: {{plan}}

        Histórico da Conversa:
        {% for msg in history %}
            {{msg.role.value}}: {{msg.text}}
        {% endfor %}

        Código do Usuário:
        ```python
        {{user_code}}
        ```

        Resultados da Execução (Casos de Teste):
        {{execution_results}}

        Mensagem do estudante: {{student_message}}

        Avalie o progresso. Se o código estiver incorreto ou não seguir o plano, forneça feedback.
        Retorne sua resposta no formato JSON com estes campos:
        - is_correct: booleano
        - feedback: Sua resposta ao estudante com dicas ou confirmação. Responda em português brasileiro.
        """)

        self.pipeline = Pipeline()
        self.pipeline.add_component("prompt_builder", self.prompt_builder)
        self.pipeline.add_component("llm", self.generator)
        self.pipeline.connect("prompt_builder.prompt", "llm.messages")

    def run(self, problem_description: str, plan: str, user_code: str, execution_results: str, student_message: str = "", history: List[ChatMessage] = None) -> Dict[str, Any]:
        history = history or []
        
        result = self.pipeline.run({
            "prompt_builder": {
                "problem_description": problem_description,
                "plan": plan,
                "user_code": user_code,
                "execution_results": execution_results,
                "student_message": student_message,
                "history": history
            }
        })
        
        import json
        raw_reply = result["llm"]["replies"][0].text
        try:
            data = json.loads(raw_reply)
            return data
        except json.JSONDecodeError:
            return {
                "is_correct": False,
                "feedback": "Estou tendo dificuldade em analisar seu código. Pode tentar explicar o que está tentando fazer?"
            }
