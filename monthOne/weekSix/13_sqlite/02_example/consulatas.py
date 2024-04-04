import sqlite3

try:
    conn = sqlite3.connect('02_Restaurante.db')
    """
    SELECT PEDIDOS.id, PLATOS.nombre AS nombre_plato, MESAS.numero AS numero_mesa
    FROM PEDIDOS
    JOIN PLATOS ON PEDIDOS.plato_id = PLATOS.id
    JOIN MESAS ON PEDIDOS.numero_mesa_id = MESAS.id;

    """
except sqlite3.Error as e:
    print("Error al trabajar con la base de datos:", e)
except Exception as e:
    print("General error:", e)
