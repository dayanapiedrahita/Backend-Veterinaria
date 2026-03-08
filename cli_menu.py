from datetime import datetime, date, time
from database import SessionLocal
from schemas.sede_schema import SedeCreate
from schemas.vacuna_schema import VacunaCreate
from schemas.usuario_schema import ClienteRegistro, VeterinarioRegistro
from schemas.mascota_schema import MascotaCreate
from schemas.cita_vacunacion_schema import CitaVacunacionCreate
from crud import (
    get_sedes, create_sede, get_vacunas, create_vacuna,
    register_cliente, register_veterinario, create_mascota,
    get_clientes, get_mascotas, get_veterinarios, get_cliente,
    get_citas_vacunacion, create_cita_vacunacion
)


def menu():
    db = SessionLocal()
    try:
        while True:
            print('\n--- Menú de prueba CRUD ---')
            print('1. Listar sedes')
            print('2. Crear sede')
            print('3. Listar vacunas')
            print('4. Crear vacuna')
            print('5. Registrar cliente')
            print('6. Registrar veterinario')
            print('7. Crear mascota')
            print('8. Listar clientes')
            print('9. Listar mascotas')
            print('10. Listar veterinarios')
            print('11. Listar citas')
            print('12. Crear cita')
            print('0. Salir')
            opt = input('Opción: ').strip()

            if opt == '1':
                for s in get_sedes(db):
                    print(s.id, s.nombre, s.direccion, s.telefono)

            elif opt == '2':
                nombre = input('Nombre sede: ')
                direccion = input('Dirección: ')
                telefono = input('Teléfono: ')
                data = SedeCreate(nombre=nombre, direccion=direccion, telefono=telefono)
                s = create_sede(db, data)
                print('Creada sede id=', s.id)

            elif opt == '3':
                for v in get_vacunas(db):
                    print(v.id, v.nombre, v.fabricante, v.dosis_requeridas)

            elif opt == '4':
                nombre = input('Nombre vacuna: ')
                fabricante = input('Fabricante: ')
                dosis = int(input('Dosis requeridas: '))
                data = VacunaCreate(nombre=nombre, fabricante=fabricante, dosis_requeridas=dosis)
                v = create_vacuna(db, data)
                print('Creada vacuna id=', v.id)

            elif opt == '5':
                nombre = input('Nombre cliente: ')
                telefono = input('Teléfono: ')
                direccion = input('Dirección: ')
                email = input('Email: ')
                data = ClienteRegistro(nombre=nombre, telefono=telefono, direccion=direccion, email=email)
                c = register_cliente(db, data)
                print('Cliente creado id=', c.id)

            elif opt == '6':
                nombre = input('Nombre vet: ')
                especialidad = input('Especialidad: ')
                id_sede = int(input('ID sede: '))
                email = input('Email: ')
                data = VeterinarioRegistro(nombre=nombre, especialidad=especialidad, id_sede=id_sede, email=email)
                v = register_veterinario(db, data)
                print('Veterinario creado id=', v.id)

            elif opt == '7':
                nombre = input('Nombre mascota: ')
                especie = input('Especie: ')
                raza = input('Raza: ')
                fecha = input('Fecha nacimiento (YYYY-MM-DD): ')
                id_cliente = int(input('ID cliente: '))
                # comprobar si el cliente existe
                if not get_cliente(db, id_cliente):
                    print(f'Cliente id={id_cliente} no encontrado.')
                    crear = input('¿Deseas crear el cliente ahora? (s/n): ').lower()
                    if crear in ('s','y'):
                        nombre_c = input('Nombre cliente: ')
                        telefono_c = input('Teléfono: ')
                        direccion_c = input('Dirección: ')
                        email_c = input('Email: ')
                        cdata = ClienteRegistro(nombre=nombre_c, telefono=telefono_c, direccion=direccion_c, email=email_c)
                        c = register_cliente(db, cdata)
                        print('Cliente creado id=', c.id)
                        id_cliente = c.id
                    else:
                        print('Cancelando creación de mascota: cliente inexistente.')
                        continue
                try:
                    fecha_dt = date.fromisoformat(fecha)
                    data = MascotaCreate(nombre=nombre, especie=especie, raza=raza, fecha_nacimiento=fecha_dt, id_cliente=id_cliente)
                    m = create_mascota(db, data)
                    print('Mascota creada id=', m.id)
                except ValueError as e:
                    print(f'Error: Fecha inválida. Por favor usa el formato YYYY-MM-DD. Detalle: {e}')

            elif opt == '8':
                for c in get_clientes(db):
                    print(c.id, c.nombre, c.telefono)

            elif opt == '9':
                for m in get_mascotas(db):
                    print(m.id, m.nombre, m.especie, m.cliente_id)

            elif opt == '10':
                for v in get_veterinarios(db):
                    print(v.id, v.nombre, v.especialidad, getattr(v, 'sede_id', None))

            elif opt == '11':
                for c in get_citas_vacunacion(db):
                    print(c.id, c.fecha, c.estado, c.id_mascota, c.id_veterinario, c.id_vacuna)

            elif opt == '12':
                try:
                    fecha_str = input('Fecha y hora (YYYY-MM-DD HH:MM:SS): ')
                    estado = input('Estado: ')
                    id_mascota = int(input('ID mascota: '))
                    id_veterinario = int(input('ID veterinario: '))
                    id_vacuna = int(input('ID vacuna: '))
                    fecha_dt = datetime.fromisoformat(fecha_str)
                    data = CitaVacunacionCreate(fecha=fecha_dt, estado=estado, id_mascota=id_mascota, id_veterinario=id_veterinario, id_vacuna=id_vacuna)
                    c = create_cita_vacunacion(db, data)
                    print('Cita creada id=', c.id)
                except ValueError as e:
                    print(f'Error: Entrada inválida. Verifica los formatos (fecha YYYY-MM-DD HH:MM:SS). Detalle: {e}')

            elif opt == '0':
                break
            else:
                print('Opción no válida')

    finally:
        db.close()


if __name__ == '__main__':
    menu()
