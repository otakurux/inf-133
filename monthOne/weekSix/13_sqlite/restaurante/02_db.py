import sqlite3

try:
    conn = sqlite3.connect("Restaurante.db")

    create_platos_table = """
    CREATE TABLE IF NOT EXISTS PLATOS (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        precio INTEGER NOT NULL,
        categoria TEXT NOT NULL
    );
    """

    create_mesas_table = """
    CREATE TABLE IF NOT EXISTS MESAS (
        id INTEGER PRIMARY KEY,
        numero INTEGER NOT NULL
    );
    """

    create_pedidos_table = """
    CREATE TABLE IF NOT EXISTS PEDIDOS (
        id INTEGER PRIMARY KEY,
        plato_id INTEGER NOT NULL,
        numero_mesa_id INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        fecha TEXT NOT NULL,
        FOREIGN KEY (plato_id) REFERENCES PLATOS(id),
        FOREIGN KEY (numero_mesa_id) REFERENCES MESAS(id)
    );
    """

    conn.execute(create_platos_table)
    conn.execute(create_mesas_table)
    conn.execute(create_pedidos_table)

    conn.execute("INSERT OR IGNORE INTO PLATOS (nombre, precio, categoria) VALUES (?, ?, ?)", ('pique macho', 56, 'almuerzo'))
    conn.execute("INSERT OR IGNORE INTO PLATOS (nombre, precio, categoria) VALUES (?, ?, ?)", ('helado', 56, 'postre'))
    conn.execute("INSERT OR IGNORE INTO MESAS (numero) VALUES (?)", (1,))
    conn.execute("INSERT OR IGNORE INTO MESAS (numero) VALUES (?)", (2,))

    conn.execute("INSERT INTO PEDIDOS (plato_id, numero_mesa_id, cantidad, fecha) VALUES (?, ?, ?, ?)", (1, 1, 4, '2024-01-15'))
    conn.execute("INSERT INTO PEDIDOS (plato_id, numero_mesa_id, cantidad, fecha) VALUES (?, ?, ?, ?)", (2, 2, 6, '2024-01-16'))

    print("\nPlatos:")
    platos_cursor = conn.execute("SELECT * FROM PLATOS")
    for plato in platos_cursor:
        print(plato)

    print("\nMesas:")
    mesas_cursor = conn.execute("SELECT * FROM MESAS")
    for mesa in mesas_cursor:
        print(mesa)

    print("\nPedidos:")
    pedidos_cursor = conn.execute("SELECT * FROM PEDIDOS")
    for pedido in pedidos_cursor:
        print(pedido)

    conn.commit()
    
    conn.close()

except sqlite3.Error as e:
    print("Error al trabajar con la base de datos:", e)
except Exception as e:
    print("Error general:", e)
