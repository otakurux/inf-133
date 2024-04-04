import sqlite3

conn = sqlite3.connect("instituto.db")

# TABLAS

# conn.execute(
#     """
#     CREATE TABLE CARRERAS
#     (id INTEGER PRIMARY KEY,
#     nombre TEXT NOT NULL,
#     duracion INTEGER NOT NULL);
#     """
# )

# conn.execute(
#     """
#     CREATE TABLE ESTUDIANTES
#     (id INTEGER PRIMARY KEY,
#     nombre TEXT NOT NULL,
#     apellido TEXT NOT NULL,
#     fecha_nacimiento DATE NOT NULL);
#     """
# )

# conn.execute(
#     """
#     CREATE TABLE MATRICULACION
#     (id INTEGER PRIMARY KEY,
#     estudiante_id INTEGER NOT NULL,
#     carrera_id INTEGER NOT NULL,
#     fecha TEXT NOT NULL,
#     FOREIGN KEY (estudiante_id) REFERENCES ESTUDIANTES(id),
#     FOREIGN KEY (carrera_id) REFERENCES CARRERAS(id));
#     """
# )

conn.execute(
    """
    INSERT INTO CARRERAS (nombre, duracion) 
    VALUES ('Ingeniería en Informatica', 5)
    """
)
conn.execute(
    """
    INSERT INTO CARRERAS (nombre, duracion) 
    VALUES ('Licenciatura en Administración', 4)
    """
)


print("CARRERAS:")
cursor = conn.execute("SELECT * FROM CARRERAS")
for row in cursor:
    print(row)

# CARRERAS:
# (1, 'Ingeniería en Informatica', 5)
# (2, 'Licenciatura en Administración', 4)
# Crear tablas de estudiantes


conn.execute(
    """
    INSERT INTO ESTUDIANTES (nombre, apellido, fecha_nacimiento) 
    VALUES ('Juan', 'Perez', '2000-05-15')
    """
)
conn.execute(
    """
    INSERT INTO ESTUDIANTES (nombre, apellido, fecha_nacimiento) 
    VALUES ('María', 'Lopez', '1999-08-20')
    """
)

print("\nESTUDIANTES:")
cursor = conn.execute("SELECT * FROM ESTUDIANTES")
for row in cursor:
    print(row)

# ESTUDIANTES:
# (1, 'Juan', 'Perez', '2000-05-15')
# (2, 'María', 'Lopez', '1999-08-20')


conn.execute(
    """
    INSERT INTO MATRICULACION (estudiante_id, carrera_id, fecha) 
    VALUES (1, 1, '2024-01-15')
    """
)
conn.execute(
    """
    INSERT INTO MATRICULACION (estudiante_id, carrera_id, fecha) 
    VALUES (2, 2, '2024-01-20')
    """
)

conn.execute(
    """
    INSERT INTO MATRICULACION (estudiante_id, carrera_id, fecha)
    VALUES (1, 2, '2024-01-25')
    """
)

print("\nMATRICULACION:")
cursor = conn.execute(
    """
    SELECT ESTUDIANTES.nombre, ESTUDIANTES.apellido, CARRERAS.nombre, MATRICULACION.fecha 
    FROM MATRICULACION
    JOIN ESTUDIANTES ON MATRICULACION.estudiante_id = ESTUDIANTES.id 
    JOIN CARRERAS ON MATRICULACION.carrera_id = CARRERAS.id
    """
)
for row in cursor:
    print(row)

# MATRICULACION:
# ('Juan', 'Perez', 'Ingeniería en Informatica', '2024-01-15')
# ('María', 'Lopez', 'Licenciatura en Administración', '2024-01-20')
# ('Juan', 'Perez', 'Licenciatura en Administración', '2024-01-25')    

conn.execute(
    """
    DELETE FROM MATRICULACION
    WHERE id = 3
    """
)

print("\nMATRICULACION:")
cursor = conn.execute(
    "SELECT * FROM MATRICULACION"
)

for row in cursor:
    print(row)

# MATRICULACION:
# (1, 1, 1, '2024-01-15')
# (2, 2, 2, '2024-01-20')

conn.execute(
    """
    UPDATE MATRICULACION
    SET fecha = '2024-01-30'
    WHERE id = 2
    """
)
print("\nMATRICULACION:")
cursor = conn.execute(
    "SELECT * FROM MATRICULACION"
)
for row in cursor:
    print(row)


# MATRICULACION:
# (1, 1, 1, '2024-01-15')
# (2, 2, 2, '2024-01-30')
conn.commit()
conn.close()