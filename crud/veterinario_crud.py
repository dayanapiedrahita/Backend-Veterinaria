from sqlalchemy.orm import Session
from entities.veterinario import Veterinario
from schemas.veterinario_schema import VeterinarioCreate


def create_veterinario(db: Session, veterinario: VeterinarioCreate):
    db_veterinario = Veterinario(**veterinario.dict())
    db.add(db_veterinario)
    db.commit()
    db.refresh(db_veterinario)
    return db_veterinario


def get_veterinario(db: Session, veterinario_id: int):
    return db.query(Veterinario).filter(Veterinario.id == veterinario_id).first()


def get_veterinarios(db: Session):
    return db.query(Veterinario).all()


def delete_veterinario(db: Session, veterinario_id: int):
    db_veterinario = db.query(Veterinario).filter(Veterinario.id == veterinario_id).first()
    if db_veterinario:
        db.delete(db_veterinario)
        db.commit()
    return db_veterinario