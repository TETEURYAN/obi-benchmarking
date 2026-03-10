import os
from typing import Dict, List, Any
from haystack import Pipeline
from haystack.components.builders import PromptBuilder
from haystack.components.generators.chat import OpenAIChatGenerator
from haystack.dataclasses import ChatMessage
from haystack.utils import Secret
from pydantic import BaseModel, Field

class PlanningStatus(BaseModel):
    is_complete: bool = Field(description="Whether the student has devised a feasible and correct step-by-step plan.")
    plan: str = Field(description="The final step-by-step plan if complete, otherwise empty.")
    feedback: str = Field(description="The message to send back to the student.")

class PlanningAgent:
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
        Você é um tutor especialista ajudando um estudante a elaborar um plano para um problema de programação usando o método de Pólya.
        O estudante já entendeu o problema. Agora, seu objetivo é guiá-lo a criar um algoritmo ou plano passo a passo.
        NÃO escreva código para o estudante. Foque na lógica e nos passos.

        Problema: {{problem_description}}
        Resumo da Compreensão: {{comprehension_summary}}

        Histórico da Conversa:
        {% for msg in history %}
            {{msg.role.value}}: {{msg.text}}
        {% endfor %}

        Mensagem do estudante: {{student_message}}

        Avalie se o plano do estudante está completo, viável e correto.
        Retorne sua resposta no formato JSON com estes campos:
        - is_complete: booleano
        - plan: Um resumo claro passo a passo do plano se completo, caso contrário vazio.
        - feedback: Sua resposta ao estudante para guiá-lo, apontar falhas ou confirmar o plano. Responda em português brasileiro.
        """)

        self.pipeline = Pipeline()
        self.pipeline.add_component("prompt_builder", self.prompt_builder)
        self.pipeline.add_component("llm", self.generator)
        self.pipeline.connect("prompt_builder.prompt", "llm.messages")

    def run(self, problem_description: str, comprehension_summary: str, student_message: str, history: List[ChatMessage] = None) -> Dict[str, Any]:
        history = history or []
        
        result = self.pipeline.run({
            "prompt_builder": {
                "problem_description": problem_description,
                "comprehension_summary": comprehension_summary,
                "student_message": student_message,
                "history": history
            }
        })
        
        print("test: ", result)
        
        import json
        raw_reply = result["llm"]["replies"][0].text
        try:
            data = json.loads(raw_reply)
            return data
        except json.JSONDecodeError:
            return {
                "is_complete": False,
                "plan": "",
                "feedback": "Estou tendo dificuldade em processar isso. Pode reformular seu plano?"
            }
