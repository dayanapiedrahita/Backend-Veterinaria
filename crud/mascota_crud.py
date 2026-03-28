from sqlalchemy.orm import Session
from entities.mascota import Mascota
from entities.cliente import Cliente
from schemas.mascota_schema import MascotaCreate
from core.exceptions import NotFoundException



def get_mascotas(db: Session):
    return db.query(Mascota).all()


def get_mascota(db: Session, mascota_id: int):
    mascota = db.query(Mascota).filter(Mascota.id == mascota_id).first()

    if not mascota:
        raise NotFoundException("Mascota no encontrada")

    return mascota



def create_mascota(db: Session, data: MascotaCreate):
 Feat--Pipeline

    cliente_id = payload.get('id_cliente')
    if cliente_id is not None:
        existing = db.query(Cliente).filter(Cliente.id == cliente_id).first()
        if not existing:
            raise NotFoundException(f"Cliente con id={cliente_id} no existe")

    if 'id_cliente' in payload:
        payload['cliente_id'] = payload.pop('id_cliente')


    # ensure cliente exists
    cliente_id = payload.get("id_cliente")
    if cliente_id is not None:
        existing = db.query(Cliente).filter(Cliente.id == cliente_id).first()
        if not existing:
            raise ValueError(f"Cliente con id={cliente_id} no existe")
    # map schema field id_cliente -> entidad cliente_id
    if "id_cliente" in payload:
        payload["cliente_id"] = payload.pop("id_cliente")
 dev
    db_mascota = Mascota(**payload)

    db.add(db_mascota)
    db.commit()
    db.refresh(db_mascota)

    return db_mascota


def update_mascota(
    db: Session,
    mascota_id: int,
    nombre: str | None = None,
    especie: str | None = None,
    raza: str | None = None,
 Feat--Pipeline
    fecha_nacimiento=None

    fecha_nacimiento=None,
 dev
):
    db_mascota = db.query(Mascota).filter(Mascota.id == mascota_id).first()

    if not db_mascota:
        raise NotFoundException("Mascota no encontrada")

    if nombre is not None:
        db_mascota.nombre = nombre

    if especie is not None:
        db_mascota.especie = especie

    if raza is not None:
        db_mascota.raza = raza

    if fecha_nacimiento is not None:
        db_mascota.fecha_nacimiento = fecha_nacimiento

    db.commit()
    db.refresh(db_mascota)

    return db_mascota


def delete_mascota(db: Session, mascota_id: int):
    db_mascota = db.query(Mascota).filter(Mascota.id == mascota_id).first()
 Feat--Pipeline

    if not db_mascota:
        raise NotFoundException("Mascota no encontrada")

    db.delete(db_mascota)
    db.commit()

    return {"message": "Mascota eliminada correctamente"}

    if db_mascota:
        db.delete(db_mascota)
        db.commit()
    return db_mascota
 dev
