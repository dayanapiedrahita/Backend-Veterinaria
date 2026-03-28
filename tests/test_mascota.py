from datetime import date
import pytest
from schemas.mascota_schema import MascotaCreate
from entities.cliente import Cliente
from crud.mascota_crud import create_mascota
from core.exceptions import NotFoundException

def test_create_mascota_con_cliente(db):
    cliente = Cliente(nombre="Test", telefono="123", direccion="X")
    db.add(cliente)
    db.commit()

    mascota = create_mascota(db, MascotaCreate(
        nombre="Firulais",
        especie="Perro",
        raza="Criollo",
        id_cliente=cliente.id,
        fecha_nacimiento=date(2020, 5, 20)  # <--- Campo obligatorio agregado
    ))
    assert mascota.nombre == "Firulais"

def test_mascota_cliente_inexistente(db):
    with pytest.raises(NotFoundException):
        create_mascota(db, MascotaCreate(
            nombre="Firulais",
            especie="Perro",
            raza="Criollo",
            id_cliente=999,
            fecha_nacimiento=date(2020, 5, 20)  # <--- Campo obligatorio agregado
        ))