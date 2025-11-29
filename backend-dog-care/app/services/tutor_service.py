from sqlalchemy.orm import Session
from app.models.tutor import Tutor
from app.schemas.tutor_schema import TutorCreate
from typing import Optional

def criar_tutor(db: Session, data: TutorCreate) -> Tutor:
    tutor = Tutor(**data.dict())
    db.add(tutor)
    db.commit()
    db.refresh(tutor)
    return tutor


def buscar_por_email(db: Session, email: str):
    return db.query(Tutor).filter(Tutor.email == email).first()


def buscar_por_id(db: Session, tutor_id: int):
    return db.query(Tutor).filter(Tutor.id == tutor_id).first()


def alterar_tutor(db: Session, tutor_id: int, novo_nome: Optional[str] = None, novo_email: Optional[str] = None) -> Optional[Tutor]:
    tutor = buscar_por_id(db, tutor_id)
    if not tutor:
        return None

    if novo_email:
        existe = buscar_por_email(db, novo_email)
        if existe and existe.id != tutor_id:
            return "email_existente"

    if novo_nome is not None:
        tutor.nome = novo_nome
    if novo_email is not None:
        tutor.email = novo_email

    db.commit()
    db.refresh(tutor)
    return tutor
