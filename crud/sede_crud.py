from sqlalchemy.orm import Session
from entities.sede import Sede
from schemas.sede_schema import SedeCreate, SedeUpdate


def get_sedes(db: Session):
    return db.query(Sede).all()


def get_sede(db: Session, sede_id: int):
    return db.query(Sede).filter(Sede.id == sede_id).first()


def create_sede(db: Session, data: SedeCreate):
    db_sede = Sede(**data.dict())
    db.add(db_sede)
    db.commit()
    db.refresh(db_sede)
    return db_sede


def update_sede(db: Session, sede_id: int, data: SedeUpdate):
    db_sede = get_sede(db, sede_id)
    if not db_sede:
        return None
    for key, value in data.dict().items():
        setattr(db_sede, key, value)
    db.commit()
    db.refresh(db_sede)
    return db_sede


def delete_sede(db: Session, sede_id: int):
    db_sede = get_sede(db, sede_id)
    if db_sede:
        db.delete(db_sede)
        db.commit()
    return db_sede
