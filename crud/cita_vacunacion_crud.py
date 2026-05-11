from sqlalchemy.orm import Session
from entities.cita_vacunacion import CitaVacunacion
from schemas.cita_vacunacion_schema import CitaVacunacionCreate, CitaVacunacionUpdate
from core.exceptions import NotFoundException


def get_citas_vacunacion(db: Session):
    return db.query(CitaVacunacion).all()


def get_cita_vacunacion(db: Session, cita_id: int):
    cita = db.query(CitaVacunacion).filter(CitaVacunacion.id == cita_id).first()
    
    if not cita:
        raise NotFoundException("Cita de vacunación no encontrada")
    
    return cita



def create_cita_vacunacion(db: Session, data: CitaVacunacionCreate):
    payload = data.model_dump()

    db_cita = CitaVacunacion(**payload)
    db.add(db_cita)
    db.commit()
    db.refresh(db_cita)

    return db_cita


def update_cita_vacunacion(db: Session, cita_id: int, data: CitaVacunacionUpdate):
    db_cita = db.query(CitaVacunacion).filter(CitaVacunacion.id == cita_id).first()

    if not db_cita:
        raise NotFoundException("Cita de vacunación no encontrada")

    update_data = data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_cita, key, value)

    db.commit()
    db.refresh(db_cita)

    return db_cita


def delete_cita_vacunacion(db: Session, cita_id: int):
    db_cita = db.query(CitaVacunacion).filter(CitaVacunacion.id == cita_id).first()

    if not db_cita:
        raise NotFoundException("Cita de vacunación no encontrada")

    db.delete(db_cita)
    db.commit()

    return {"message": "Cita eliminada correctamente"}
