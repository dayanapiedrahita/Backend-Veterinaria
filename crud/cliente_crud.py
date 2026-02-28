from sqlalchemy.orm import Session
from entities.cliente import Cliente
from schemas.cliente_schema import ClienteCreate


def create_cliente(db: Session, cliente: ClienteCreate):
    db_cliente = Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente


def get_cliente(db: Session, cliente_id: int):
    return db.query(Cliente).filter(Cliente.id == cliente_id).first()


def get_clientes(db: Session):
    return db.query(Cliente).all()


def delete_cliente(db: Session, cliente_id: int):
    db_cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if db_cliente:
        db.delete(db_cliente)
        db.commit()
    return db_cliente