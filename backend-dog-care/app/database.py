from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Caminho do banco SQLite
DATABASE_URL = "sqlite:///./database.db"

# Criar engine
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Criar sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base das models
Base = declarative_base()


# Dependência usada nas rotas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()