from app.schemas.tutor_schema import TutorCreate, TutorLogin, TutorUpdate
from app.controllers import tutor_controller
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter(prefix="/tutor")

@router.post("/cadastro")
def cadastro(data: TutorCreate, db: Session = Depends(get_db)):
    return tutor_controller.cadastrar_tutor(db, data)

@router.post("/login")
def login(data: TutorLogin, db: Session = Depends(get_db)):
    return tutor_controller.login(db, data)

@router.put("/alterar/{tutor_id}")
def alterar(tutor_id: int, data: TutorUpdate, db: Session = Depends(get_db)):
    return tutor_controller.alterar_tutor(db, tutor_id, data)