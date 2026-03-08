from haystack import Pipeline
from haystack.components.builders import PromptBuilder

class PlanningAgent:
    def __init__(self):
        self.pipeline = Pipeline()
        self.pipeline.add_component("prompt_builder", PromptBuilder(template="""
        You are a Planning Agent. Your goal is to help students devise a plan for the following problem:
        Problem: {{problem_description}}
        Comprehension Summary: {{comprehension_summary}}
        
        Student message: {{student_message}}
        """))

    def run(self, problem_description: str, comprehension_summary: str, student_message: str):
        return {"reply": f"Planning strategy for: {student_message}"}
