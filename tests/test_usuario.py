# tests/test_usuario.py
import uuid
import pytest
from crud.usuario_crud import create_usuario, update_usuario
from entities.usuario import Usuario
from core.exceptions import ConflictException


def test_create_usuario(db):
    """Test creating a new usuario."""
    unique_email = f"{uuid.uuid4()}@test.com"
    user = create_usuario(db, email=unique_email, rol="cliente")
    assert user.email == unique_email
    assert user.rol == "cliente"


def test_get_usuario(db):
    """Test retrieving a usuario."""
    unique_email = f"{uuid.uuid4()}@test.com"
    user = create_usuario(db, email=unique_email, rol="cliente")
    fetched = db.query(Usuario).filter_by(id=user.id).first()
    assert fetched.email == unique_email


def test_update_usuario(db):
    """Test updating a usuario."""
    old_email = f"{uuid.uuid4()}@test.com"
    user = create_usuario(db, email=old_email, rol="cliente")
    
    new_email = f"{uuid.uuid4()}@test.com"
    updated = update_usuario(db, user.id, email=new_email)
    assert updated.email == new_email
    assert updated.rol == "cliente"