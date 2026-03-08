import json
from pathlib import Path
from pydantic import BaseModel, Field
from typing import List, Dict

class TestCase(BaseModel):
    input: str
    expected_output: str

class Example(BaseModel):
    input: str
    output: str

class Question(BaseModel):
    id: str
    title: str
    description: str
    constraints: List[str]
    examples: List[Example]
    test_cases: List[TestCase]

class QuestionManager:
    def __init__(self, db_path: str = None):
        if db_path is None:
            self.db_path = Path(__file__).parent / "database" / "questions.json"
        else:
            self.db_path = Path(db_path)

    def load_questions(self) -> List[Question]:
        if not self.db_path.exists():
            return []
        with open(self.db_path, "r") as f:
            data = json.load(f)
            return [Question(**q) for q in data]

    def get_question_by_id(self, question_id: str) -> Question:
        questions = self.load_questions()
        for q in questions:
            if q.id == question_id:
                return q
        return None
