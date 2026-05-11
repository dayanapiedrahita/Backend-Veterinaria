from sqlalchemy.orm import Session
from entities.mascota import Mascota
from schemas.mascota_schema import MascotaCreate, MascotaUpdate
from core.exceptions import NotFoundException



def get_mascotas(db: Session):
    return db.query(Mascota).all()


def get_mascota(db: Session, mascota_id: int):
    mascota = db.query(Mascota).filter(Mascota.id == mascota_id).first()

    if not mascota:
        raise NotFoundException("Mascota no encontrada")

    return mascota



def create_mascota(db: Session, data: MascotaCreate):
    payload = data.model_dump()

    db_mascota = Mascota(**payload)

    db.add(db_mascota)
    db.commit()
    db.refresh(db_mascota)

    return db_mascota


def update_mascota(
    db: Session,
    mascota_id: int,
    data: MascotaUpdate
):
    db_mascota = db.query(Mascota).filter(Mascota.id == mascota_id).first()

    if not db_mascota:
        raise NotFoundException("Mascota no encontrada")

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(db_mascota, key, value)

    db.commit()
    db.refresh(db_mascota)

    return db_mascota


def delete_mascota(db: Session, mascota_id: int):
    db_mascota = db.query(Mascota).filter(Mascota.id == mascota_id).first()

    if not db_mascota:
        raise NotFoundException("Mascota no encontrada")

    db.delete(db_mascota)
    db.commit()

    return {"exito": True, "mensaje": "Mascota eliminada correctamente"}
