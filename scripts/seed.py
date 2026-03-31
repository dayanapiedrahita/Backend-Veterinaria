#!/usr/bin/env python
"""Seeder script to populate database with initial data."""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from database import SessionLocal
from entities.sede import Sede
from entities.vacuna import Vacuna
from entities.usuario import Usuario
from entities.cliente import Cliente
from entities.veterinario import Veterinario
from entities.mascota import Mascota


def seed():
    """Populate database with initial data if not already populated."""
    db = SessionLocal()
    
    try:
        print("🌱 Iniciando seeder...")
        
        # Check if data already exists
        if db.query(Sede).first() is not None:
            print("✓ Base de datos ya contiene datos. Saltando seeder.")
            return
        
        # Create Sedes
        print("📍 Creando sedes...")
        sedes = [
            Sede(nombre="Sede Centro", direccion="Calle 1 #123", telefono="3001234567"),
            Sede(nombre="Sede Norte", direccion="Carrera 5 #456", telefono="3009876543"),
            Sede(nombre="Sede Sur", direccion="Avenida 10 #789", telefono="3005555555"),
        ]
        db.add_all(sedes)
        db.commit()
        print(f"✓ {len(sedes)} sedes creadas")
        
        # Create Vacunas
        print("💉 Creando vacunas...")
        vacunas = [
            Vacuna(nombre="Rabia", descripcion="Protección contra rabia", presentacion="Inyectable"),
            Vacuna(nombre="Parvovirus", descripcion="Protección contra parvovirus canino", presentacion="Inyectable"),
            Vacuna(nombre="Moquillo", descripcion="Protección contra moquillo", presentacion="Inyectable"),
            Vacuna(nombre="Leucemia (Gatos)", descripcion="Protección contra leucemia felina", presentacion="Inyectable"),
            Vacuna(nombre="Rinotraqueitis", descripcion="Protección contra rinotraqueitis", presentacion="Inyectable"),
        ]
        db.add_all(vacunas)
        db.commit()
        print(f"✓ {len(vacunas)} vacunas creadas")
        
        # Create Veterinarios
        print("👨‍⚕️ Creando veterinarios...")
        sede = db.query(Sede).first()
        vet_data = [
            ("dr.garcia@veterinaria.com", "Dr. García López"),
            ("dr.martin@veterinaria.com", "Dr. Martín Pérez"),
            ("dra.silva@veterinaria.com", "Dra. Silva Rodríguez"),
        ]
        
        for email, nombre in vet_data:
            vet_entity = Veterinario(
                nombre=nombre,
                especialidad="Clínica General",
                id_sede=sede.id
            )
            db.add(vet_entity)
            db.flush()
            
            usuario = Usuario(
                email=email,
                rol="veterinario",
                veterinario_id=vet_entity.id
            )
            db.add(usuario)
        
        db.commit()
        print(f"✓ 3 veterinarios creados")
        
        # Create Clientes
        print("👥 Creando clientes...")
        client_data = [
            ("Juan García", "3101111111", "Calle Principal 100", "juan.garcia@email.com"),
            ("María López", "3102222222", "Carrera Secundaria 200", "maria.lopez@email.com"),
            ("Carlos Rodríguez", "3103333333", "Avenida Central 300", "carlos.rodriguez@email.com"),
            ("Ana Martínez", "3104444444", "Calle Lateral 400", "ana.martinez@email.com"),
        ]
        
        clientes = []
        for nombre, telefono, direccion, email in client_data:
            cliente = Cliente(
                nombre=nombre,
                telefono=telefono,
                direccion=direccion
            )
            db.add(cliente)
            db.flush()
            
            usuario = Usuario(
                email=email,
                rol="cliente",
                cliente_id=cliente.id
            )
            db.add(usuario)
            clientes.append(cliente)
        
        db.commit()
        print(f"✓ {len(clientes)} clientes creados")
        
        # Create Mascotas
        print("🐕 Creando mascotas...")
        pet_data = [
            ("Rex", "Perro", "Golden Retriever", 5, 0),
            ("Mimi", "Gato", "Persa", 3, 1),
            ("Buddy", "Perro", "Labrador", 2, 2),
            ("Luna", "Gato", "Siamés", 1, 3),
        ]
        
        for nombre, tipo, raza, edad, cliente_idx in pet_data:
            mascota = Mascota(
                nombre=nombre,
                tipo=tipo,
                raza=raza,
                edad=edad,
                id_cliente=clientes[cliente_idx].id
            )
            db.add(mascota)
        
        db.commit()
        print(f"✓ {len(pet_data)} mascotas creadas")
        
        print("\n✅ Seeder completado exitosamente!")
        
    except Exception as e:
        db.rollback()
        print(f"❌ Error en seeder: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        db.close()


if __name__ == "__main__":
    seed()