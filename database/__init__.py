from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

# Configuração da conexão com o banco de dados (pode ser SQLite, MySQL, etc.)
engine = create_engine('sqlite:///library.db', echo=True)

# Cria uma sessão de banco de dados
db_session = scoped_session(sessionmaker(bind=engine))

# Base para os modelos (caso você use isso nos models)
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import models  # importa os modelos para registrar as tabelas
    Base.metadata.create_all(bind=engine)
