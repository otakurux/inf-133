SELECT PEDIDOS.id, PLATOS.nombre AS nombre_plato, MESAS.numero AS numero_mesa
FROM PEDIDOS
JOIN PLATOS ON PEDIDOS.plato_id = PLATOS.id
JOIN MESAS ON PEDIDOS.numero_mesa_id = MESAS.id;
