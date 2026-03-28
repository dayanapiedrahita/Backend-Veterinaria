from database import SessionLocal
from entities.usuario import Usuario
from entities.cliente import Cliente
from entities.veterinario import Veterinario
from entities.sede import Sede


def seed():
    db = SessionLocal()

    # SEDE
    sede = db.query(Sede).filter_by(nombre="Principal").first()
    if not sede:
        sede = Sede(nombre="Principal", direccion="Centro")
        db.add(sede)
        db.commit()
        db.refresh(sede)

    # CLIENTE
    cliente = db.query(Cliente).filter_by(nombre="Cliente Demo").first()
    if not cliente:
        cliente = Cliente(
            nombre="Cliente Demo",
            telefono="123456789",
            direccion="Calle 1"
        )
        db.add(cliente)
        db.commit()
        db.refresh(cliente)

    # USUARIO CLIENTE
    usuario_cliente = db.query(Usuario).filter_by(email="cliente@test.com").first()
    if not usuario_cliente:
        usuario_cliente = Usuario(
            email="cliente@test.com",
            rol="cliente",
            cliente_id=cliente.id
        )
        db.add(usuario_cliente)
        db.commit()

    # VETERINARIO
    veterinario = db.query(Veterinario).filter_by(nombre="Vet Demo").first()
    if not veterinario:
        veterinario = Veterinario(
            nombre="Vet Demo",
            especialidad="General",
            sede_id=sede.id
        )
        db.add(veterinario)
        db.commit()
        db.refresh(veterinario)

    # USUARIO VETERINARIO
    usuario_vet = db.query(Usuario).filter_by(email="vet@test.com").first()
    if not usuario_vet:
        usuario_vet = Usuario(
            email="vet@test.com",
            rol="veterinario",
            veterinario_id=veterinario.id
        )
        db.add(usuario_vet)
        db.commit()

    db.close()


if __name__ == "__main__":
    seed()