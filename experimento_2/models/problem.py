from typing import List, Optional
from pydantic import BaseModel
from .example import Example

class Problem(BaseModel):
    path: str
    imgs: Optional[list] = None
    title: str
    statement: str
    input: str
    output: str
    constraints: str
    examples: List[Example]
