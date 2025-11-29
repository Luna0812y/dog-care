from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    idade = Column(Integer)
    tipo = Column(String)

    tutor_id = Column(Integer, ForeignKey("tutores.id"))
    tutor = relationship("Tutor", back_populates="pets")