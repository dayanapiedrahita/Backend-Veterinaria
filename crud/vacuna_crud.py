from sqlalchemy.orm import Session
from entities.vacuna import Vacuna
from schemas.vacuna_schema import VacunaCreate
from core.exceptions import NotFoundException



def get_vacunas(db: Session):
    return db.query(Vacuna).all()


def get_vacuna(db: Session, vacuna_id: int):
    vacuna = db.query(Vacuna).filter(Vacuna.id == vacuna_id).first()

    if not vacuna:
        raise NotFoundException("Vacuna no encontrada")

    return vacuna



def create_vacuna(db: Session, data: VacunaCreate):
    db_vacuna = Vacuna(**data.dict())

    db.add(db_vacuna)
    db.commit()
    db.refresh(db_vacuna)

    return db_vacuna


def update_vacuna(
    db: Session,
    vacuna_id: int,
    nombre: str | None = None,
    fabricante: str | None = None,
    descripcion: str | None = None,
 Feat--Pipeline
    dosis_requeridas: int | None = None

    dosis_requeridas: int | None = None,
 dev
):
    db_vacuna = db.query(Vacuna).filter(Vacuna.id == vacuna_id).first()

    if not db_vacuna:
        raise NotFoundException("Vacuna no encontrada")

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
 Feat--Pipeline

    if not db_vacuna:
        raise NotFoundException("Vacuna no encontrada")

    db.delete(db_vacuna)
    db.commit()

    return {"message": "Vacuna eliminada correctamente"}

    if db_vacuna:
        db.delete(db_vacuna)
        db.commit()
    return db_vacuna
 dev
