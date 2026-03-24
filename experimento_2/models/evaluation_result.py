from pydantic import BaseModel

class EvaluationResult(BaseModel):
    question_name: str
    difficulty: str
    llm_code_creation_time: float
    total_tokens: int
    cost_prompt: float
    judge_predict: str
    execution_time: float
    AC: int
    WA: int
    RE: int
    TLE: int
    CE: int
    total_test_cases: int