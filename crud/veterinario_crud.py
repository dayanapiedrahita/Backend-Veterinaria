from sqlalchemy.orm import Session
from entities.veterinario import Veterinario

def get_veterinarios(db: Session):
    return db.query(Veterinario).all()

def get_veterinario(db: Session, veterinario_id: int):
    return db.query(Veterinario).filter(Veterinario.id == veterinario_id).first()

def update_veterinario(db: Session, veterinario_id: int, nombre: str | None = None,
                       especialidad: str | None = None, id_sede: int | None = None):
    db_veterinario = db.query(Veterinario).filter(Veterinario.id == veterinario_id).first()
    if not db_veterinario:
        return None
    if nombre is not None:
        db_veterinario.nombre = nombre
    if especialidad is not None:
        db_veterinario.especialidad = especialidad
    if id_sede is not None:
        db_veterinario.id_sede = id_sede
    db.commit()
    db.refresh(db_veterinario)
    return db_veterinario

def delete_veterinario(db: Session, veterinario_id: int):
    db_veterinario = db.query(Veterinario).filter(Veterinario.id == veterinario_id).first()
    if db_veterinario:
        db.delete(db_veterinario)
        db.commit()
    return db_veterinario