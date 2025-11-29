from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.services import tutor_service
from app.schemas.tutor_schema import TutorCreate, TutorLogin, TutorUpdate

def cadastrar_tutor(db: Session, data: TutorCreate):
    tutor = tutor_service.buscar_por_email(db, data.email)
    if tutor:
        raise HTTPException(400, "Email já cadastrado")
    return tutor_service.criar_tutor(db, data)


def login(db: Session, data: TutorLogin):
    tutor = tutor_service.buscar_por_email(db, data.email)
    if not tutor:
        raise HTTPException(401, "Email não encontrado")
    if tutor.senha != data.senha:
        raise HTTPException(401, "Senha inválida")
    return {"message": "Login realizado", "tutor": tutor.nome}


def alterar_tutor(db: Session, tutor_id: int, data: TutorUpdate):
    tutor = tutor_service.alterar_tutor(
        db,
        tutor_id,
        data.nome,
        data.email
    )

    if tutor == "email_existente":
        raise HTTPException(400, "Esse email já está em uso por outro tutor")

    if not tutor:
        raise HTTPException(404, "Tutor não encontrado")

    return tutor