from haystack import Pipeline
from haystack.components.builders import PromptBuilder

class ImplementationAgent:
    def __init__(self):
        self.pipeline = Pipeline()
        self.pipeline.add_component("prompt_builder", PromptBuilder(template="""
        You are an Implementation Agent. Your goal is to help students write code for their plan.
        Problem: {{problem_description}}
        Plan: {{plan}}
        
        User code: {{user_code}}
        Execution results: {{execution_results}}
        """))

    def run(self, problem_description: str, plan: str, user_code: str, execution_results: str):
        return {"reply": "Refining implementation..."}
