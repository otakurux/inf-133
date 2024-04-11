import sqlite3

db_filename = "personal.db"
conn = sqlite3.connect(db_filename)

def listar_empleados_salarios():
    try:
        cursor = conn.execute("""
            SELECT E.nombre, E.apellido_paterno, E.apellido_materno, S.salario
            FROM EMPLEADOS E
            JOIN SALARIO S ON E.id = S.empleado_id
        """)

        print("\nEmpleados y sus salarios:")
        for row in cursor.fetchall():
            print(f"{row[0]} {row[1]} {row[2]} - Salario: {row[3]} USD")

    except sqlite3.Error as e:
        print("Error al listar empleados y salarios:", e)

def listar_empleados_departamento_cargo():
    try:
        cursor = conn.execute("""
            SELECT E.nombre, E.apellido_paterno, E.apellido_materno, D.nombre AS departamento, C.nombre AS cargo
            FROM EMPLEADOS E
            JOIN DEPARTAMENTOS D ON E.departamento_id = D.id
            JOIN CARGOS C ON E.cargo_id = C.id
        """)

        print("\nEmpleados, departamento y cargo:")
        for row in cursor.fetchall():
            print(f"{row[0]} {row[1]} {row[2]} - Departamento: {row[3]}, Cargo: {row[4]}")

    except sqlite3.Error as e:
        print("Error al listar empleados, departamento y cargo:", e)

def listar_empleados_departamento_cargo_salario():
    try:
        cursor = conn.execute("""
            SELECT E.nombre, E.apellido_paterno, E.apellido_materno, D.nombre AS departamento, C.nombre AS cargo, S.salario
            FROM EMPLEADOS E
            JOIN DEPARTAMENTOS D ON E.departamento_id = D.id
            JOIN CARGOS C ON E.cargo_id = C.id
            JOIN SALARIO S ON E.id = S.empleado_id
        """)

        print("\nEmpleados, departamento, cargo y salario:")
        for row in cursor.fetchall():
            print(f"{row[0]} {row[1]} {row[2]} - Departamento: {row[3]}, Cargo: {row[4]}, Salario: {row[5]} USD")

    except sqlite3.Error as e:
        print("Error al listar empleados, departamento, cargo y salario:", e)

try:
    listar_empleados_salarios()
    listar_empleados_departamento_cargo()
    listar_empleados_departamento_cargo_salario()

except sqlite3.Error as e:
    print("Error al ejecutar las consultas:", e)
finally:
    conn.close()
