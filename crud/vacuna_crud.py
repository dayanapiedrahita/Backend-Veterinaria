from sqlalchemy.orm import Session
from entities.vacuna import Vacuna
from schemas.vacuna_schema import VacunaCreate, VacunaUpdate
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
    data: VacunaUpdate
):
    db_vacuna = db.query(Vacuna).filter(Vacuna.id == vacuna_id).first()

    if not db_vacuna:
        raise NotFoundException("Vacuna no encontrada")

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(db_vacuna, key, value)

    db.commit()
    db.refresh(db_vacuna)

    return db_vacuna


def delete_vacuna(db: Session, vacuna_id: int):
    db_vacuna = db.query(Vacuna).filter(Vacuna.id == vacuna_id).first()

    if not db_vacuna:
        raise NotFoundException("Vacuna no encontrada")

    db.delete(db_vacuna)
    db.commit()

    return {"message": "Vacuna eliminada correctamente"}
