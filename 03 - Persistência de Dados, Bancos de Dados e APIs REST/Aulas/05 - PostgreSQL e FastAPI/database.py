from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import sessionmaker

DATABASE_URL = "postgresql://usuario123:senha123@localhost/escola"

# Estabele a comunicação entre o banco de dados e o FastAPI.
engine = create_engine(DATABASE_URL)
# Cria uma conexão temporária com o banco de dados.
SessionLocal = sessionmaker(bind=engine)
# Permite a criação de entidades.
Base = declarative_base()