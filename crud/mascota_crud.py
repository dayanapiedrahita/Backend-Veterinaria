from sqlalchemy.orm import Session
from entities.mascota import Mascota
from schemas.mascota_schema import MascotaCreate


def create_mascota(db: Session, mascota: MascotaCreate):
    db_mascota = Mascota(**mascota.dict())
    db.add(db_mascota)
    db.commit()
    db.refresh(db_mascota)
    return db_mascota


def get_mascota(db: Session, mascota_id: int):
    return db.query(Mascota).filter(Mascota.id == mascota_id).first()


def get_mascotas(db: Session):
    return db.query(Mascota).all()


def delete_mascota(db: Session, mascota_id: int):
    db_mascota = db.query(Mascota).filter(Mascota.id == mascota_id).first()
    if db_mascota:
        db.delete(db_mascota)
        db.commit()
    return db_mascota