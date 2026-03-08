import os
from typing import Dict, List, Any
from haystack import Pipeline
from haystack.components.builders import PromptBuilder
from haystack.components.generators.chat import OpenAIChatGenerator
from haystack.dataclasses import ChatMessage
from haystack.utils import Secret
from pydantic import BaseModel, Field

class ComprehensionStatus(BaseModel):
    is_complete: bool = Field(description="Whether the student fully understands the problem and its constraints.")
    summary: str = Field(description="A concise summary of the student's understanding if complete, or what's missing.")
    feedback: str = Field(description="The message to send back to the student.")

class ComprehensionAgent:
    def __init__(self, model: str = None, api_key: str = None, base_url: str = None):
        self.model = model or os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.base_url = base_url or os.getenv("OPENAI_BASE_URL")
        
        # Generator for structured output
        # Haystack 2.x expects a Secret object for api_key
        self.generator = OpenAIChatGenerator(
            model=self.model,
            api_key=Secret.from_token(self.api_key) if self.api_key else None,
            api_base_url=self.base_url,
            generation_kwargs={"response_format": {"type": "json_object"}}
        )

        self.prompt_builder = PromptBuilder(template="""
        You are an expert tutor helping a student understand a programming problem using the Pólya method.
        Your goal for this phase is ONLY to ensure the student understands the problem statement, inputs, outputs, and constraints.
        DO NOT provide solutions or plans yet.

        Problem: {{problem_description}}
        Constraints: {{constraints}}

        Conversation History:
        {% for msg in history %}
            {{msg.role.value}}: {{msg.text}}
        {% endfor %}

        Student message: {{student_message}}

        Evaluate if the student has a solid understanding.
        Return your response in JSON format with these fields:
        - is_complete: boolean
        - summary: A summary of the problem if complete, otherwise empty.
        - feedback: Your response to the student to guide them or confirm understanding.
        """)

        self.pipeline = Pipeline()
        self.pipeline.add_component("prompt_builder", self.prompt_builder)
        self.pipeline.add_component("llm", self.generator)
        self.pipeline.connect("prompt_builder.prompt", "llm.messages")

    def run(self, problem_description: str, constraints: str, student_message: str, history: List[ChatMessage] = None) -> Dict[str, Any]:
        history = history or []
        
        # Prepare the prompt
        # Note: Haystack PromptBuilder expects specific keys
        result = self.pipeline.run({
            "prompt_builder": {
                "problem_description": problem_description,
                "constraints": constraints,
                "student_message": student_message,
                "history": history
            }
        })
        
        # Parse JSON response
        import json
        raw_reply = result["llm"]["replies"][0].text
        try:
            data = json.loads(raw_reply)
            return data
        except json.JSONDecodeError:
            return {
                "is_complete": False,
                "summary": "",
                "feedback": "I'm having trouble processing that. Can you rephrase?"
            }
