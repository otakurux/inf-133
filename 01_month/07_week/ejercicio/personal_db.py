import sqlite3

db_filename = "personal.db"

table_departamentos = """
    CREATE TABLE DEPARTAMENTOS (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL
    )
"""

table_cargos = """
    CREATE TABLE CARGOS (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        nivel TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL
    )
"""

table_empleados = """
    CREATE TABLE EMPLEADOS (
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
    CREATE TABLE SALARIO (
        id INTEGER PRIMARY KEY,
        empleado_id INTEGER NOT NULL,
        salario REAL NOT NULL,
        fecha_inicio DATE NOT NULL,
        fecha_fin DATE NOT NULL,
        fecha_creacion TEXT NOT NULL,
        FOREIGN KEY (empleado_id) REFERENCES EMPLEADOS(id)
    )
"""

try:
    with sqlite3.connect(db_filename) as conn:
        conn.execute(table_departamentos)
        conn.execute(table_cargos)
        conn.execute(table_empleados)
        conn.execute(table_salarios)
        conn.commit()
except sqlite3.Error as e:
    print("Error al crear la tabla:", e)
