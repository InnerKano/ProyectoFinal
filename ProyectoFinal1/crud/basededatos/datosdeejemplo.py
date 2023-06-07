import sqlite3

# Conectarse a la base de datos
conexion = sqlite3.connect('crud/basededatos/agricola.db')

cursor = conexion.cursor()

# Agregar datos a la tabla de clientes
clientes = [
    ('Juan Perez', '1001'),
    ('Maria Rodriguez', '1002'),
    ('Pedro Gonzalez', '1003'),
    ('Luisa Martinez', '1004'),
    ('Carlos Garcia', '1005')
]

for cliente in clientes:
    cursor.execute("INSERT INTO clientes (nombre, cedula) VALUES (?, ?)", cliente)
# Agregar datos a la tabla de pedidos
pedidos = [    ('ICF-123','1001', '2023-05-10',1),
               ('ICF-456','1002', '2023-05-11',1),
                ('Antibiotico 5','1003', '2023-05-12',2),
                ('Antibiotico 2','1004', '2023-05-12',2),    
                ('ICF-135','1005', '2023-05-13',1)]

for pedido in pedidos:
    cursor.execute("INSERT INTO pedidos (producto, cedula_cliente, fecha_pedido, opcion) VALUES ( ?, ?, ?, ?)", pedido)

# Agregar datos a la tabla de productos de control
productos_control = [
    ('ICF-123', 'Fertilizante 1', 'Cada 15 días', 15000),
    ('ICF-456', 'Fertilizante 2', 'Cada 30 días', 20000),
    ('ICP-789', 'Control de Plagas 1', 'Cada 7 días', 5000),
    ('ICP-246', 'Control de Plagas 2', 'Cada 15 días', 8000),
    ('ICC-135', 'Control de Cosecha 1', 'Cada 15 días', 10000)
]

for producto in productos_control:
    cursor.execute("INSERT INTO productos_control (registro_ica, nombre, frecuencia_aplicacion, valor) VALUES (?, ?, ?, ?)", producto)

# Agregar datos a la tabla de antibioticos
antibioticos = [
    ('Antibiotico 1', 400, 'Bovinos', 50000),
    ('Antibiotico 2', 500, 'Porcinos', 60000),
    ('Antibiotico 3', 600, 'Bovinos', 70000),
    ('Antibiotico 4', 550, 'Caprinos', 55000),
    ('Antibiotico 5', 450, 'Porcinos', 65000)
]

for antibiotico in antibioticos:
    cursor.execute("INSERT INTO antibioticos (nombre_producto, dosis, tipo_animal, precio) VALUES (?, ?, ?, ?)", antibiotico)

# Agregar datos a la tabla de facturas
facturas = [
    ('1001', '2022-01-01','Antibiotico 1', 50000),
    ('1001', '2022-02-01','ICF-123', 15000),
    ('1003', '2022-03-01','Antibiotico 3', 700000),
    ('1004', '2022-04-01','ICF-123', 15000),
    ('1005', '2022-05-01','Antibiotico 5', 65000)
]

for factura in facturas:
    cursor.execute("INSERT INTO facturas (cedula_cliente,fecha_factura, producto, valor_total) VALUES ( ?, ?, ?, ?)", factura)

# Guardar los cambios en la base de datos
conexion.commit()

conexion.close()