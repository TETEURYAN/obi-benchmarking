from pydantic import BaseModel

class EvaluationResult(BaseModel):
    question_name: str
    llm_code_creation_time: float
    info: str
    judge_predict: str
    execution_time: float
    AC: int
    WA: int
    RE: int
    TLE: int
    CE: int
    total_test_cases: int