
import sqlite3

try:
    conn = sqlite3.connect("02_Restaurante.db")

    create_dishes_table = """
    CREATE TABLE IF NOT EXISTS PLATOS (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price INTEGER NOT NULL,
        category TEXT NOT NULL
    );
    """

    create_tables_table = """
    CREATE TABLE IF NOT EXISTS MESAS (
        id INTEGER PRIMARY KEY,
        number INTEGER NOT NULL
    );
    """

    create_orders_table = """
    CREATE TABLE IF NOT EXISTS PEDIDOS (
        id INTEGER PRIMARY KEY,
        dish_id INTEGER NOT NULL,
        table_number_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        date TEXT NOT NULL,
        FOREIGN KEY (dish_id) REFERENCES PLATOS(id),
        FOREIGN KEY (table_number_id) REFERENCES MESAS(id)
    );
    """

    try:
        conn.execute(create_dishes_table)
        conn.execute(create_tables_table)
        conn.execute(create_orders_table)
    except sqlite3.OperationalError as e:
        print("Error al crear la tabla:", e)

    conn.execute("INSERT OR IGNORE INTO PLATOS (name, price, category) VALUES (?, ?, ?)", ('pique macho', 56, 'almuerzo'))
    conn.execute("INSERT OR IGNORE INTO PLATOS (name, price, category) VALUES (?, ?, ?)", ('ice cream', 56, 'dessert'))
    conn.execute("INSERT OR IGNORE INTO MESAS (number) VALUES (?)", (1,))
    conn.execute("INSERT OR IGNORE INTO MESAS (number) VALUES (?)", (2,))

    conn.execute("INSERT INTO PEDIDOS (dish_id, table_number_id, quantity, date) VALUES (?, ?, ?, ?)", (1, 1, 4, '2024-01-15'))
    conn.execute("INSERT INTO PEDIDOS (dish_id, table_number_id, quantity, date) VALUES (?, ?, ?, ?)", (2, 2, 6, '2024-01-16'))

    print("\nDishes:")
    dishes_cursor = conn.execute("SELECT * FROM PLATOS")
    for dish in dishes_cursor:
        print(dish)

    print("\nTables:")
    tables_cursor = conn.execute("SELECT * FROM MESAS")
    for table in tables_cursor:
        print(table)

    print("\nOrders:")
    orders_cursor = conn.execute("SELECT * FROM PEDIDOS")
    for order in orders_cursor:
        print(order)

    conn.commit()
    conn.close()

except sqlite3.Error as e:
    print("Error al trabajar con la base de datos:", e)
except Exception as e:
    print("General error:", e)
