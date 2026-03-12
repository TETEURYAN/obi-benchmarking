from typing import List, Optional
from pydantic import BaseModel

class Example(BaseModel):
    input: str
    output: str

class Problem(BaseModel):
    id: str
    title: str
    statement: str
    input: str
    output: str
    constraints: str
    examples: List[Example]

class EvaluationResult(BaseModel):
    question_id: str
    model: str
    understanding_text: str
    plan_text: str
