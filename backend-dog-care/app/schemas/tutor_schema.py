from pydantic import BaseModel
from typing import List, Optional
from app.schemas.pet_schema import PetResponse

class TutorCreate(BaseModel):
    nome: str
    email: str
    senha: str

class TutorLogin(BaseModel):
    email: str
    senha: str

class TutorUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None

class TutorReponse(BaseModel):
    id: int
    nome: str
    email: str
    pets: List[PetResponse] = []

    class Config:
        orm_mode = True