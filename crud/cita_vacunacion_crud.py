from sqlalchemy.orm import Session
from entities.cita_vacunacion import CitaVacunacion
from schemas.cita_vacunacion_schema import CitaVacunacionCreate

def get_citas_vacunacion(db: Session):
    return db.query(CitaVacunacion).all()

def get_cita_vacunacion(db: Session, cita_id: int):
    return db.query(CitaVacunacion).filter(CitaVacunacion.id == cita_id).first()

def create_cita_vacunacion(db: Session, data: CitaVacunacionCreate):
    db_cita = CitaVacunacion(**data.dict())
    db.add(db_cita)
    db.commit()
    db.refresh(db_cita)
    return db_cita

def update_cita_vacunacion(db: Session, cita_id: int, data: CitaVacunacionCreate):
    db_cita = db.query(CitaVacunacion).filter(CitaVacunacion.id == cita_id).first()
    if not db_cita:
        return None
    for key, value in data.dict().items():
        setattr(db_cita, key, value)
    db.commit()
    db.refresh(db_cita)
    return db_cita

def delete_cita_vacunacion(db: Session, cita_id: int):
    db_cita = db.query(CitaVacunacion).filter(CitaVacunacion.id == cita_id).first()
    if db_cita:
        db.delete(db_cita)
        db.commit()
    return db_cita