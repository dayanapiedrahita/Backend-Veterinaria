from sqlalchemy.orm import Session
from entities.cliente import Cliente
from core.exceptions import NotFoundException



def get_clientes(db: Session):
    return db.query(Cliente).all()


def get_cliente(db: Session, cliente_id: int):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not cliente:
        raise NotFoundException("Cliente no encontrado")

    return cliente


 Feat--Pipeline

 dev
def update_cliente(
    db: Session,
    cliente_id: int,
    nombre: str | None = None,
    telefono: str | None = None,
 Feat--Pipeline
    direccion: str | None = None

    direccion: str | None = None,
 dev
):
    db_cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not db_cliente:
        raise NotFoundException("Cliente no encontrado")

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
 Feat--Pipeline

    if not db_cliente:
        raise NotFoundException("Cliente no encontrado")

    db.delete(db_cliente)
    db.commit()

    return {"message": "Cliente eliminado correctamente"}

    if db_cliente:
        db.delete(db_cliente)
        db.commit()
    return db_cliente
 dev
