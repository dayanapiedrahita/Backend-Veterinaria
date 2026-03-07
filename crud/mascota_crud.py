from sqlalchemy.orm import Session
from entities.mascota import Mascota
from schemas.mascota_schema import MascotaCreate

def get_mascotas(db: Session):
    return db.query(Mascota).all()

def get_mascota(db: Session, mascota_id: int):
    return db.query(Mascota).filter(Mascota.id == mascota_id).first()

def create_mascota(db: Session, data: MascotaCreate):
    db_mascota = Mascota(**data.dict())
    db.add(db_mascota)
    db.commit()
    db.refresh(db_mascota)
    return db_mascota

def update_mascota(db: Session, mascota_id: int, nombre: str | None = None,
                   especie: str | None = None, raza: str | None = None, fecha_nacimiento = None):
    db_mascota = db.query(Mascota).filter(Mascota.id == mascota_id).first()
    if not db_mascota:
        return None
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
    if db_mascota:
        db.delete(db_mascota)
        db.commit()
    return db_mascota