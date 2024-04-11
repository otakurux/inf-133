import sqlite3

db_filename = "personal.db"
conn = sqlite3.connect(db_filename)

new_departamentos = [
    ("Ventas", "10-04-2020"),
    ("Marketing", "11-04-2020")
]

new_cargos = [
    ("Gerente de Ventas", "Senior", "10-04-2020"),
    ("Analista de Marketing", "Junior", "11-04-2020"),
    ("Representante de Ventas", "Junior", "12-04-2020")
]

try:
    for nombre_dep, fecha_creacion_dep in new_departamentos:
        cursor = conn.execute("SELECT id FROM DEPARTAMENTOS WHERE nombre = ?", (nombre_dep,))
        if cursor.fetchone() is None:
            conn.execute("INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion) VALUES (?, ?)",
                         (nombre_dep, fecha_creacion_dep))
        else:
            print(f"El departamento '{nombre_dep}' ya existe en la base de datos y no se agregara.")

    for nombre_cargo, nivel_cargo, fecha_creacion_cargo in new_cargos:
        cursor = conn.execute("SELECT id FROM CARGOS WHERE nombre = ?", (nombre_cargo,))
        if cursor.fetchone() is None:
            conn.execute("INSERT INTO CARGOS (nombre, nivel, fecha_creacion) VALUES (?, ?, ?)",
                         (nombre_cargo, nivel_cargo, fecha_creacion_cargo))
        else:
            print(f"El cargo '{nombre_cargo}' ya existe en la base de datos y no se agregara.")

    nombre_departamento = "ventas"
    conn.execute("DELETE FROM DEPARTAMENTOS WHERE nombre = ?", (nombre_departamento,))

    conn.commit()
    print("Se han agregado los nuevos departamentos y cargos.")
except sqlite3.Error as e:
    print("Error al agregar los nuevos departamentos y cargos:", e)
finally:
    conn.close()
