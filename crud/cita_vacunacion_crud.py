from sqlalchemy.orm import Session
from entities.cita_vacunacion import CitaVacunacion
from schemas.cita_vacunacion_schema import CitaVacunacionCreate


def create_cita(db: Session, cita: CitaVacunacionCreate):
    db_cita = CitaVacunacion(**cita.dict())
    db.add(db_cita)
    db.commit()
    db.refresh(db_cita)
    return db_cita


def get_cita(db: Session, cita_id: int):
    return db.query(CitaVacunacion).filter(CitaVacunacion.id == cita_id).first()


def get_citas(db: Session):
    return db.query(CitaVacunacion).all()


def delete_cita(db: Session, cita_id: int):
    db_cita = db.query(CitaVacunacion).filter(CitaVacunacion.id == cita_id).first()
    if db_cita:
        db.delete(db_cita)
        db.commit()
    return db_cita