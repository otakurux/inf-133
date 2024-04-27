import sqlite3

db_filename = "personal.db"
conn = sqlite3.connect(db_filename)

def empleado_existe(nombre, apellido_paterno, apellido_materno):
    cursor = conn.execute("""
        SELECT COUNT(*) FROM EMPLEADOS
        WHERE nombre = ? AND apellido_paterno = ? AND apellido_materno = ?
    """, (nombre, apellido_paterno, apellido_materno))
    count = cursor.fetchone()[0]
    return count > 0

def salario_existe(empleado_id, fecha_inicio, fecha_fin):
    cursor = conn.execute("""
        SELECT COUNT(*) FROM SALARIO
        WHERE empleado_id = ? AND fecha_inicio = ? AND fecha_fin = ?
    """, (empleado_id, fecha_inicio, fecha_fin))
    count = cursor.fetchone()[0]
    return count > 0

def agregar_empleado(nombre, apellido_paterno, apellido_materno, cargo, departamento, fecha_creacion):
    if not empleado_existe(nombre, apellido_paterno, apellido_materno):
        try:
            conn.execute("""
                INSERT INTO EMPLEADOS (nombre, apellido_paterno, apellido_materno, cargo_id, departamento_id, fecha_creacion)
                VALUES (?, ?, ?, (SELECT id FROM CARGOS WHERE nombre = ?), (SELECT id FROM DEPARTAMENTOS WHERE nombre = ?), ?)
            """, (nombre, apellido_paterno, apellido_materno, cargo, departamento, fecha_creacion))
            print(f"Empleado {nombre} {apellido_paterno} {apellido_materno} agregado exitosamente.")
        except sqlite3.Error as e:
            print("Error al agregar empleado:", e)
    else:
        print(f"El empleado {nombre} {apellido_paterno} {apellido_materno} ya existe en la base de datos.")

def agregar_salario(empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion):
    if not salario_existe(empleado_id, fecha_inicio, fecha_fin):
        try:
            conn.execute("""
                INSERT INTO SALARIO (empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion)
                VALUES (?, ?, ?, ?, ?)
            """, (empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion))
            print(f"Salario agregado exitosamente para empleado ID {empleado_id}.")
        except sqlite3.Error as e:
            print("Error al agregar salario:", e)
    else:
        print(f"El salario para empleado ID {empleado_id} ya existe en la base de datos.")

list_empleados = []

try:
    agregar_empleado("Juan", "Gonzalez", "Perez", "Gerente de Ventas", "Ventas", "15-05-2023")
    agregar_empleado("Maria", "Lopez", "Martinez", "Analista de Marketing", "Marketing", "20-06-2023")

    id_juan = conn.execute("""
        SELECT id FROM EMPLEADOS
        WHERE nombre = ? AND apellido_paterno = ? AND apellido_materno = ?
    """, ("Juan", "Gonzalez", "Perez")).fetchone()[0]

    id_maria = conn.execute("""
        SELECT id FROM EMPLEADOS
        WHERE nombre = ? AND apellido_paterno = ? AND apellido_materno = ?
    """, ("Maria", "Lopez", "Martinez")).fetchone()[0]

    agregar_salario(id_juan, 3000, "01-04-2024", "30-04-2025", "01-04-2024")
    agregar_salario(id_maria, 3500, "01-07-2023", "30-04-2024", "01-07-2023")

    conn.commit()
except sqlite3.Error as e:
    print("Error:", e)
finally:
    conn.close()
