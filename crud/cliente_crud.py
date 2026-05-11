from sqlalchemy.orm import Session
from entities.cliente import Cliente
from schemas.cliente_schema import ClienteUpdate
from core.exceptions import NotFoundException



def get_clientes(db: Session):
    return db.query(Cliente).all()


def get_cliente(db: Session, cliente_id: int):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not cliente:
        raise NotFoundException("Cliente no encontrado")

    return cliente


def update_cliente(db: Session, cliente_id: int, data: ClienteUpdate):
    db_cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not db_cliente:
        raise NotFoundException("Cliente no encontrado")

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(db_cliente, key, value)

    db.commit()
    db.refresh(db_cliente)

    return db_cliente


def delete_cliente(db: Session, cliente_id: int):
    db_cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not db_cliente:
        raise NotFoundException("Cliente no encontrado")

    db.delete(db_cliente)
    db.commit()

    return {"message": "Cliente eliminado correctamente"}
