import sqlite3

conn = sqlite3.connect("01_Restaurante.db")

conn.execute(
    """
    CREATE TABLE PLATOS
    (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        precio INTEGER NOT NULL,
        categoria TEXT NOT NULL
    );
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria)
    VALUES ('pique macho', 56, ' almuerzo')
    """
)

conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria)
    VALUES ('helado', 56, ' postre')
    """
)



conn.execute(
    """
    CREATE TABLE MESAS
    (
        id INTEGER PRIMARY KEY,
        numero INTEGER NOT NULL 
    );
    """
)

conn.execute(
    """
    INSERT INTO MESAS (numero)
    VALUES (1)
    """
)

print("\nMesas:")
cursor = conn.execute("SELECT * FROM MESAS")
for row in cursor:
    print(row)

conn.execute(
    """
    CREATE TABLE PEDIDOS
    (
        id INTEGER PRIMARY KEY,
        plato TEXT NOT NULL,
        numero_mesa INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        fecha TEXT NOT NULL,
        FOREIGN KEY (plato) REFERENCES PLATOS(id),
        FOREIGN KEY (numero_mesa) REFERENCES MESAS(id)
    );
    """
)

conn.execute(
    """
    INSERT INTO PEDIDOS (plato, numero_mesa, cantidad, fecha)
    VALUES (1, 1, 4, '2024-01-15')
    """
)

conn.execute(
    """
    INSERT INTO PEDIDOS (plato, numero_mesa, cantidad, fecha)
    VALUES (2, 2, 6, '2024-01-16')
    """
)

print("platos:")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)

print("\npedidos:")
cursor = conn.execute("SELECT * FROM PEDIDOS")
for row in cursor:
    print(row)

conn.commit()

conn.close()