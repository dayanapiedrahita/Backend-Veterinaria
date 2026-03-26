# tests/conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db  # tu Base y función para obtener sesiones
from main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"  # o la URL de test
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear las tablas de prueba
Base.metadata.create_all(bind=engine)

@pytest.fixture
def db():
    connection = engine.connect()
    transaction = connection.begin()
    db = TestingSessionLocal(bind=connection)
    try:
        yield db
    finally:
        db.rollback()
        db.close()
        connection.close()