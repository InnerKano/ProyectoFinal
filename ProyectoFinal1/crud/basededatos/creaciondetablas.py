import sqlite3

conexion = sqlite3.connect('crud/basededatos/agricola.db')


conexion.execute('''CREATE TABLE clientes
             (cedula INT PRIMARY KEY     NOT NULL,
             nombre           TEXT    NOT NULL);''')

conexion.execute('''CREATE TABLE pedidos
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             producto TEXT NOT NULL,
             cedula_cliente INT NOT NULL,
             fecha_pedido TEXT NOT NULL,
             opcion INT    NOT NULL);''')


conexion.execute('''CREATE TABLE productos_control
             (registro_ica TEXT PRIMARY KEY     NOT NULL,
             nombre TEXT NOT NULL,
             frecuencia_aplicacion TEXT NOT NULL,
             valor FLOAT NOT NULL);''')

conexion.execute('''CREATE TABLE antibioticos
             (nombre_producto TEXT PRIMARY KEY     NOT NULL,
             dosis TEXT NOT NULL,
             tipo_animal TEXT NOT NULL,
             precio FLOAT NOT NULL);''')

conexion.execute('''CREATE TABLE facturas
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             cedula_cliente INTEGER NOT NULL,
             fecha_factura TEXT NOT NULL,
             producto TEXT NOT NULL,
             valor_total FLOAT NOT NULL,
             FOREIGN KEY(cedula_cliente) REFERENCES clientes(cedula));''')
