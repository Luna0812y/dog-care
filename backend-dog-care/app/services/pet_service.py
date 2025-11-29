from sqlalchemy.orm import Session
from app.models.pet import Pet
from app.services.tutor_service import buscar_por_id as buscar_tutor
from app.schemas.pet_schema import PetCreate
from typing import Optional
from fastapi import HTTPException

def criar_pet(db: Session, data: PetCreate) -> Pet:
    tutor = buscar_tutor(db, data.tutor_id)

    if not tutor:
        raise HTTPException(404, detail="Tutor não encontrado")

    novo_pet = Pet(
        nome=data.nome,
        idade=data.idade,
        tipo=data.tipo,
        tutor_id=data.tutor_id
    )

    db.add(novo_pet)
    db.commit()
    db.refresh(novo_pet)

    return novo_pet


def apagar_pet(db: Session, pet_id: int) -> bool:
    pet = db.query(Pet).filter(Pet.id == pet_id).first()

    if not pet:
        return False

    db.delete(pet)
    db.commit()

    return True


def atualizar_pet(db: Session, pet_id: int, nome: Optional[str], idade: Optional[int]) -> Optional[Pet]:
    pet = db.query(Pet).filter(Pet.id == pet_id).first()

    if not pet:
        return None

    if nome:
        pet.nome = nome
    if idade:
        pet.idade = idade

    db.commit()
    db.refresh(pet)

    return pet
