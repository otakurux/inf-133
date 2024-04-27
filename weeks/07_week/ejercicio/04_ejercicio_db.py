import sqlite3

db_filename = "personal.db"
conn = sqlite3.connect(db_filename)

def actualizar_cargo(empleado_id, nuevo_cargo):
    try:
        conn.execute("""
            UPDATE EMPLEADOS
            SET cargo_id = (SELECT id FROM CARGOS WHERE nombre = ?)
            WHERE id = ?
        """, (nuevo_cargo, empleado_id))
        conn.commit()
        print(f"Cargo actualizado exitosamente para empleado ID {empleado_id}.")
    except sqlite3.Error as e:
        print("Error al actualizar cargo:", e)

def obtener_id_empleado(nombre, apellido_paterno, apellido_materno):
    try:
        id_empleado = conn.execute("""
            SELECT id FROM EMPLEADOS
            WHERE nombre = ? AND apellido_paterno = ? AND apellido_materno = ?
        """, (nombre, apellido_paterno, apellido_materno)).fetchone()[0]
        return id_empleado
    except sqlite3.Error as e:
        print("Error al obtener ID del empleado:", e)
        return None

def actualizar_salario(empleado_id, nuevo_salario, fecha_inicio, fecha_fin, fecha_creacion):
    try:
        if empleado_id is not None and nuevo_salario is not None and fecha_inicio is not None and fecha_fin is not None and fecha_creacion is not None:
            conn.execute("""
                UPDATE SALARIO
                SET salario = ?, fecha_creacion = ?
                WHERE empleado_id = ? AND fecha_inicio = ? AND fecha_fin = ?
            """, (nuevo_salario, fecha_creacion, empleado_id, fecha_inicio, fecha_fin))
            conn.commit()
            print(f"Salario actualizado exitosamente para empleado ID {empleado_id}.")
        else:
            print(f"No se encontró un registro de salario para empleado ID {empleado_id} en el periodo dado.")
    except sqlite3.Error as e:
        print("Error al actualizar salario:", e)

try:
    id_maria = obtener_id_empleado("Ma", "Lopez", "Martinez")
    actualizar_cargo(id_maria, "Representante de Ventas")
    actualizar_salario(id_maria, 3600, "01-07-2023", "30-04-2024", "01-04-2024")
except sqlite3.Error as e:
    print("Error:", e)
finally:
    conn.close()
