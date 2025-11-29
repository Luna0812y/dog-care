from fastapi import HTTPException
from app.services import pet_service
from app.schemas.pet_schema import PetCreate, PetUpdate

def cadastrar_pet(data: PetCreate):
    return pet_service.criar_pet(data.nome, data.idade, data.tipo, data.tutor_id)

def apagar_pet(pet_id: int):
    if pet_service.apagar_pet(pet_id):
        return {"message": "Pet apagado"}
    raise HTTPException(404, "Pet não cadastrado")

def alterar_pet(pet_id: int, data: PetUpdate):
    pet = pet_service.atualizar_pet(pet_id, data.nome, data.idade)
    if not pet:
        raise HTTPException(404, "Pet não cadastrado")
    return pet