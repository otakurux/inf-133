import sqlite3

conn = sqlite3.connect("personal.db")

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

# try:
#     conn.execute(table_cargos)
#     conn.execute(table_departamentos)
#     conn.execute(table_empleados)
#     conn.execute(table_salarios)
# except sqlite3.OperationalError as e:
#         print("Error al crear la tabla:", e)

def create_departamento(nombre, fecha_creacion):
    conn.execute("INSERT OR IGNORE INTO DEPARTAMENTOS (nombre, fecha_creacion) VALUES (?, ?)", (nombre, fecha_creacion))

def create_cargo(nombre, nivel, fecha_creacion):
    conn.execute("INSERT OR IGNORE INTO CARGOS (nombre, nivel, fecha_creacion) VALUES (?, ?, ?)", (nombre, nivel, fecha_creacion))

# Crear dos nuevos departamentos, uno llamado "Ventas" creado el
# 10-04-2020 y otro llamado "Marketing" creado el 11-04-2020.
# ● Crear tres nuevos cargos: "Gerente de Ventas" de nivel "Senior"
# creado el 10-04-2020, "Analista de Marketing" de nivel "Junior"
# creado el 11-04-2020, y "Representante de Ventas" de nivel "Junior"
# creado el 12-04-2020.

try:
    create_departamento("ventas", "10-04-2020")
    create_departamento("Marketing", "11-04-2020")
except sqlite3.OperationalError as e:
        print("Error al agregar:", e)

conn.commit()

conn.close()

# falta
