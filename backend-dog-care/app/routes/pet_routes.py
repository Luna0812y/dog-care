from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers import pet_controller
from app.schemas.pet_schema import PetCreate, PetUpdate
from app.database import get_db

router = APIRouter(prefix="/pet")

@router.post("/cadastro")
def cadastro(data: PetCreate, db: Session = Depends(get_db)):
    return pet_controller.cadastrar_pet(db, data)


@router.delete("/apagar/{pet_id}")
def apagar(pet_id: int, db: Session = Depends(get_db)):
    return pet_controller.apagar_pet(db, pet_id)


@router.put("/alterar/{pet_id}")
def alterar(pet_id: int, data: PetUpdate, db: Session = Depends(get_db)):
    return pet_controller.alterar_pet(db, pet_id, data)
