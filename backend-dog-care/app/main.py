from app.routes.tutor_routes import router as tutor_router
from app.routes.pet_routes import router as pet_router
from app.database import Base, engine
from fastapi import FastAPI

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tutor_router)
app.include_router(pet_router)