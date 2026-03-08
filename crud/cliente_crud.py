from sqlalchemy.orm import Session
from entities.cliente import Cliente

def get_clientes(db: Session):
    return db.query(Cliente).all()

def get_cliente(db: Session, cliente_id: int):
    return db.query(Cliente).filter(Cliente.id == cliente_id).first()

def update_cliente(db: Session, cliente_id: int, nombre: str | None = None, telefono: str | None = None, direccion: str | None = None):
    db_cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not db_cliente:
        return None
    if nombre is not None:
        db_cliente.nombre = nombre
    if telefono is not None:
        db_cliente.telefono = telefono
    if direccion is not None:
        db_cliente.direccion = direccion
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def delete_cliente(db: Session, cliente_id: int):
    db_cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if db_cliente:
        db.delete(db_cliente)
        db.commit()
    return db_cliente