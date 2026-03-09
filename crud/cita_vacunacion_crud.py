from sqlalchemy.orm import Session
from entities.cita_vacunacion import CitaVacunacion
from schemas.cita_vacunacion_schema import CitaVacunacionCreate
from datetime import datetime


def get_citas_vacunacion(db: Session):
    return db.query(CitaVacunacion).all()


def get_cita_vacunacion(db: Session, cita_id: int):
    return db.query(CitaVacunacion).filter(CitaVacunacion.id == cita_id).first()


def create_cita_vacunacion(db: Session, data: CitaVacunacionCreate):
    payload = data.dict()
    # map id_mascota/id_veterinario/id_vacuna -> mascota_id/veterinario_id/vacuna_id
    if "id_mascota" in payload:
        payload["mascota_id"] = payload.pop("id_mascota")
    if "id_veterinario" in payload:
        payload["veterinario_id"] = payload.pop("id_veterinario")
    if "id_vacuna" in payload:
        payload["vacuna_id"] = payload.pop("id_vacuna")

    db_cita = CitaVacunacion(**payload)
    db.add(db_cita)
    db.commit()
    db.refresh(db_cita)
    return db_cita


def update_cita_vacunacion(db: Session, cita_id: int, data: CitaVacunacionCreate):
    db_cita = db.query(CitaVacunacion).filter(CitaVacunacion.id == cita_id).first()
    if not db_cita:
        return None
    payload = data.dict()
    # map ids
    if "id_mascota" in payload and payload["id_mascota"] is not None:
        setattr(db_cita, "mascota_id", payload.pop("id_mascota"))
    if "id_veterinario" in payload and payload["id_veterinario"] is not None:
        setattr(db_cita, "veterinario_id", payload.pop("id_veterinario"))
    if "id_vacuna" in payload and payload["id_vacuna"] is not None:
        setattr(db_cita, "vacuna_id", payload.pop("id_vacuna"))
    # map fecha
    if "fecha" in payload and payload["fecha"] is not None:
        setattr(db_cita, "fecha", payload.pop("fecha"))
    # map estado
    if "estado" in payload and payload["estado"] is not None:
        setattr(db_cita, "estado", payload["estado"])
    db.commit()
    db.refresh(db_cita)
    return db_cita


def delete_cita_vacunacion(db: Session, cita_id: int):
    db_cita = db.query(CitaVacunacion).filter(CitaVacunacion.id == cita_id).first()
    if db_cita:
        db.delete(db_cita)
        db.commit()
    return db_cita
