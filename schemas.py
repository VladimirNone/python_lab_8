from pydantic import BaseModel, Field
from typing import List, Optional

class Term(BaseModel):
    keyword: str = Field(..., min_length=1, max_length=100, description="Ключевое слово термина")
    description: str = Field(..., min_length=1, description="Описание термина")

class TermRequest(BaseModel):
    keyword: str = Field(..., min_length=1, max_length=100, description="Ключевое слово термина")

class TermList(BaseModel):
    terms: List[Term] = []

class OperationStatus(BaseModel):
    success: bool
    message: Optional[str]
