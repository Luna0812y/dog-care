from pydantic import BaseModel
from typing import Optional

class PetCreate(BaseModel):
    nome: str
    idade: int
    tipo: str
    tutor_id: int

class PetUpdate(BaseModel):
    nome: Optional[str] = None
    idade: Optional[str] = None

class PetResponse(BaseModel):
    id: int
    nome: str
    idade: int
    tipo: str
    tutor_id: int

    class Config:
        orm_mode = True