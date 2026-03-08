from sqlalchemy.orm import Session
from entities.usuario import Usuario
from entities.cliente import Cliente
from entities.veterinario import Veterinario
from schemas.usuario_schema import ClienteRegistro, VeterinarioRegistro

def get_usuarios(db: Session):
    return db.query(Usuario).all()

def get_usuario_by_id(db: Session, user_id: int):
    return db.query(Usuario).filter(Usuario.id == user_id).first()

<<<<<<< HEAD
def get_usuario_by_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()

def contar_usuarios(db: Session) -> int:
    """Retorna el número total de usuarios"""
    return db.query(Usuario).count()

=======
>>>>>>> 5bd09800c98fc85e16530f65b638b366716b6ff5
def create_usuario(db: Session, email: str, rol: str, cliente_id: int | None = None, veterinario_id: int | None = None):
    usuario = Usuario(
        email=email,
        rol=rol,
        cliente_id=cliente_id,
        veterinario_id=veterinario_id
    )
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

def update_usuario(db: Session, user_id: int, email: str | None = None, rol: str | None = None):
    db_usuario = db.query(Usuario).filter(Usuario.id == user_id).first()
    if not db_usuario:
        return None
    if email:
        db_usuario.email = email
    if rol:
        db_usuario.rol = rol
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def delete_usuario(db: Session, user_id: int):
    db_usuario = db.query(Usuario).filter(Usuario.id == user_id).first()
    if not db_usuario:
        return None
    db.delete(db_usuario)
    db.commit()
    return db_usuario

def login_usuario(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()

def register_cliente(db: Session, data: ClienteRegistro):
    existing_user = db.query(Usuario).filter(Usuario.email == data.email).first()
    if existing_user:
        raise ValueError("El email ya está registrado")
    cliente = Cliente(
        nombre=data.nombre,
        telefono=data.telefono,
        direccion=data.direccion
    )
    db.add(cliente)
    db.flush()
    usuario = Usuario(
        email=data.email,
        rol="cliente",
        cliente_id=cliente.id
    )
    db.add(usuario)
    db.commit()
    db.refresh(cliente)
    return cliente

def register_veterinario(db: Session, data: VeterinarioRegistro):
    existing_user = db.query(Usuario).filter(Usuario.email == data.email).first()
    if existing_user:
        raise ValueError("El email ya está registrado")
    veterinario = Veterinario(
        nombre=data.nombre,
        especialidad=data.especialidad,
        sede_id=data.id_sede
    )
    db.add(veterinario)
    db.flush()
    usuario = Usuario(
        email=data.email,
        rol="veterinario",
        veterinario_id=veterinario.id
    )
    db.add(usuario)
    db.commit()
    db.refresh(veterinario)
    return veterinario