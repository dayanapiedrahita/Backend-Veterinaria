from sqlalchemy.orm import Session
from entities.vacuna import Vacuna
from schemas.vacuna_schema import VacunaCreate

def get_vacunas(db: Session):
    return db.query(Vacuna).all()

def get_vacuna(db: Session, vacuna_id: int):
    return db.query(Vacuna).filter(Vacuna.id == vacuna_id).first()

def create_vacuna(db: Session, data: VacunaCreate):
    db_vacuna = Vacuna(**data.dict())
    db.add(db_vacuna)
    db.commit()
    db.refresh(db_vacuna)
    return db_vacuna

def update_vacuna(db: Session, vacuna_id: int, nombre: str | None = None,
                  fabricante: str | None = None, descripcion: str | None = None,
                  dosis_requeridas: int | None = None):
    db_vacuna = db.query(Vacuna).filter(Vacuna.id == vacuna_id).first()
    if not db_vacuna:
        return None
    if nombre is not None:
        db_vacuna.nombre = nombre
    if fabricante is not None:
        db_vacuna.fabricante = fabricante
    if descripcion is not None:
        db_vacuna.descripcion = descripcion
    if dosis_requeridas is not None:
        db_vacuna.dosis_requeridas = dosis_requeridas
    db.commit()
    db.refresh(db_vacuna)
    return db_vacuna

def delete_vacuna(db: Session, vacuna_id: int):
    db_vacuna = db.query(Vacuna).filter(Vacuna.id == vacuna_id).first()
    if db_vacuna:
        db.delete(db_vacuna)
        db.commit()
    return db_vacuna