from pydantic import BaseModel

class EvaluationResult(BaseModel):
    question_name: str
    model: str
    level_to_llm: str
    info: str
    judge_predict: str
    correct_test_cases: int
    total_test_cases: int
