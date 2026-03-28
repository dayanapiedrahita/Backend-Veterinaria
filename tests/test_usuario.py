# tests/test_usuario.py
import uuid
import pytest
from crud.usuario_crud import create_usuario, update_usuario
from database import SessionLocal
from core.exceptions import ConflictException

@pytest.fixture
def db():
    from database import SessionLocal
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_create_usuario(db):
    unique_email = f"{uuid.uuid4()}@test.com"
    user = create_usuario(db, email=unique_email, rol="cliente")
    assert user.email == unique_email

def test_get_usuario(db):
    unique_email = f"{uuid.uuid4()}@test.com"
    user = create_usuario(db, email=unique_email, rol="cliente")
    fetched = db.query(user.__class__).filter_by(id=user.id).first()
    assert fetched.email == unique_email

def test_update_usuario(db):
    old_email = f"{uuid.uuid4()}@test.com"
    user = create_usuario(db, email=old_email, rol="cliente")
    new_email = f"{uuid.uuid4()}@test.com"
    updated = update_usuario(db, user.id, email=new_email)
    assert updated.email == new_email