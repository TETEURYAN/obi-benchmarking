from pydantic import BaseModel

class Level(BaseModel):
    question_name: str
    level_to_llm: str