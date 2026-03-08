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
        You are an expert tutor helping a student implement their solution in code using the Pólya method.
        The student has already understood the problem and devised a plan.
        Now, they are writing code and you must provide tips based on their progress and test results.
        DO NOT provide the full solution. Give small, actionable hints.

        Problem: {{problem_description}}
        Plan: {{plan}}

        Conversation History:
        {% for msg in history %}
            {{msg.role.value}}: {{msg.text}}
        {% endfor %}

        User Code:
        ```python
        {{user_code}}
        ```

        Execution Results (Test Cases):
        {{execution_results}}

        Student message: {{student_message}}

        Evaluate the progress. If the code is incorrect or doesn't follow the plan, provide feedback.
        Return your response in JSON format with these fields:
        - is_correct: boolean
        - feedback: Your response to the student with tips or confirmation.
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
                "feedback": "I'm having trouble analyzing your code. Can you try to explain what you're attempting?"
            }
