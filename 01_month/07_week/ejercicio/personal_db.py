import sqlite3

db_filename = "personal.db"
conn = sqlite3.connect(db_filename)

table_departamentos = """
    CREATE TABLE IF NOT EXISTS DEPARTAMENTOS (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL
    )
"""

table_cargos = """
    CREATE TABLE IF NOT EXISTS CARGOS (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        nivel TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL
    )
"""

table_empleados = """
    CREATE TABLE IF NOT EXISTS EMPLEADOS (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellido_paterno TEXT NOT NULL,
        apellido_materno TEXT NOT NULL,
        cargo_id INTEGER NOT NULL,
        departamento_id INTEGER NOT NULL,
        fecha_creacion TEXT NOT NULL,
        FOREIGN KEY (cargo_id) REFERENCES CARGOS(id),
        FOREIGN KEY (departamento_id) REFERENCES DEPARTAMENTOS(id)
    )
"""

table_salarios = """
    CREATE TABLE IF NOT EXISTS SALARIO (
        id INTEGER PRIMARY KEY,
        empleado_id INTEGER NOT NULL,
        salario REAL NOT NULL,
        fecha_inicio DATE NOT NULL,
        fecha_fin DATE NOT NULL,
        fecha_creacion TEXT NOT NULL,
        FOREIGN KEY (empleado_id) REFERENCES EMPLEADOS(id)
    )
"""

tables_to_create = [table_cargos, table_departamentos, table_empleados, table_salarios]

try:
    for table_query in tables_to_create:
        conn.execute(table_query)
    conn.commit()
    print("Exito al crear las tablas:")
except sqlite3.OperationalError as e:
    print("Error al crear las tablas:", e)
except sqlite3.Error as e:
    print("Error de SQLite:", e)
finally:
    conn.close()
