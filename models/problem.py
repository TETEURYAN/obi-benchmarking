from typing import List
from pydantic import BaseModel
from .example import Example

class Problem(BaseModel):
    id: str
    title: str
    statement: str
    input: str
    output: str
    constraints: str
    examples: List[Example]
