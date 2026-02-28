from sqlalchemy.orm import Session
from entities.vacuna import Vacuna
from schemas.vacuna_schema import VacunaCreate


def create_vacuna(db: Session, vacuna: VacunaCreate):
    db_vacuna = Vacuna(**vacuna.dict())
    db.add(db_vacuna)
    db.commit()
    db.refresh(db_vacuna)
    return db_vacuna


def get_vacuna(db: Session, vacuna_id: int):
    return db.query(Vacuna).filter(Vacuna.id == vacuna_id).first()


def get_vacunas(db: Session):
    return db.query(Vacuna).all()


def delete_vacuna(db: Session, vacuna_id: int):
    db_vacuna = db.query(Vacuna).filter(Vacuna.id == vacuna_id).first()
    if db_vacuna:
        db.delete(db_vacuna)
        db.commit()
    return db_vacuna