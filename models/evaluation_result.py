from pydantic import BaseModel

class EvaluationResult(BaseModel):
    question_name: str
    model: str
    level_to_llm: str
    modality: str
    period: str
    judge_correctness: bool
    correct_test_cases: int
    total_test_cases: int
