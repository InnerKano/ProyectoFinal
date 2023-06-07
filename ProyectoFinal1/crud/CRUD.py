import sqlite3

conexion = sqlite3.connect('crud/basededatos/agricola.db')
cursor = conexion.cursor()
class Cliente():
    def crear_cliente(cedula, nombre):
        conexion.execute("INSERT INTO clientes (cedula, nombre) VALUES (?, ?)", (cedula, nombre))
        conexion.commit()

    def buscar_cliente(cedula):
        cursor = conexion.execute("SELECT * from clientes WHERE cedula=?", (cedula,))
        resultado = cursor.fetchone()
        if resultado is None:
            return None
        return resultado

    def actualizar_cliente(cedula, nombre):
        conexion.execute("UPDATE clientes SET nombre=? WHERE cedula=?", (nombre, cedula))
        conexion.commit()

    def eliminar_cliente(cedula):
        conexion.execute("DELETE from clientes WHERE cedula=?", (cedula,))
        conexion.commit()

    def buscar_factura_cedula(cedula):
        cursor = conexion.execute("SELECT * from facturas WHERE cedula_cliente=?", (cedula,))
        resultado = cursor.fetchall()
        nombres_columnas = [descripcion[0] for descripcion in cursor.description]
        if resultado is None:
            return None
        return nombres_columnas,resultado
class Pedido():
    def crear_pedido( producto, cedula_cliente, fecha_pedido, opcion):
        conexion.execute("INSERT INTO pedidos ( producto, cedula_cliente, fecha_pedido, opcion) VALUES ( ?, ?, ?, ?)", (producto, cedula_cliente, fecha_pedido, opcion))
        conexion.commit()

    def buscar_pedido(cedula):
        cursor = conexion.execute("SELECT * from pedidos WHERE cedula_cliente=?", (cedula,))
        resultado = cursor.fetchall()
        nombres_columnas = [descripcion[0] for descripcion in cursor.description]
        if resultado is None:
            return None
        return nombres_columnas,resultado

    def pagar_pedido(id):
        cursor =  conexion.execute("SELECT * from pedidos WHERE id=?", (id,))
        resultado = cursor.fetchone() 
        if resultado is None:
            return None          
        pedido = resultado[1]
        opcion = resultado[4]
        if opcion == 1: 
            cursor = conexion.execute("SELECT * from productos_control WHERE registro_ica=?", (pedido,))
        elif opcion == 2:
            cursor = conexion.execute("SELECT * from antibioticos WHERE nombre_producto=?", (pedido,))
            print(cursor)
        resultado_pedido = cursor.fetchone() 
        valor = resultado_pedido[3]
        conexion.execute("INSERT INTO facturas (cedula_cliente, fecha_factura, producto, valor_total) VALUES (?, ?, ?, ?)", ( resultado[2], resultado[3], pedido, valor))
        conexion.execute("DELETE from pedidos WHERE id=?", (id,))
        conexion.commit()

    def actualizar_pedido(id, cedula_cliente, fecha_pedido):
        conexion.execute("UPDATE pedidos SET cedula_cliente=?, fecha_pedido=? WHERE id=?", (cedula_cliente, fecha_pedido, id))
        conexion.commit()

    def eliminar_pedido(id):
        conexion.execute("DELETE from pedidos WHERE id=?", (id,))
        conexion.commit()

    def crear_producto_control(registro_ica, nombre_producto, frecuencia_aplicacion, valor_producto):
        conexion.execute("INSERT INTO productos_control (registro_ica, nombre_producto, frecuencia_aplicacion, valor_producto) VALUES (?, ?, ?, ?)", (registro_ica, nombre_producto, frecuencia_aplicacion, valor_producto))
    conexion.commit()

    def leer_productos_control():
        cursor.execute("SELECT * FROM productos_control")
        productos = cursor.fetchall()
        nombres_columnas = [descripcion[0] for descripcion in cursor.description]
        return nombres_columnas, productos  # Devolver la lista de resultados

    def actualizar_producto_control(producto_control):
        conexion.execute("UPDATE productos_control SET registro_ica = ?, nombre_producto = ?, frecuencia_aplicacion = ?, valor_producto = ? WHERE id = ?", (producto_control.registro_ica, producto_control.nombre_producto, producto_control.frecuencia_aplicacion, producto_control.valor_producto, producto_control.id))
    conexion.commit()

    def borrar_producto_control(id):
        conexion.execute("DELETE FROM productos_control WHERE id = ?", (id,))
    conexion.commit()


    def crear_antibiotico(nombre_producto, dosis, tipo_animal, precio):
        conexion.execute("INSERT INTO antibioticos (nombre_producto, dosis, tipo_animal, precio) VALUES (?, ?, ?, ?)", (nombre_producto, dosis, tipo_animal, precio))
        conexion.commit()

    def leer_antibioticos():
        cursor.execute("SELECT * FROM antibioticos")
        antibioticos = cursor.fetchall()
        nombres_columnas = [descripcion[0] for descripcion in cursor.description]
        return nombres_columnas, antibioticos  # Devolver la lista de resultados

    def actualizar_antibiotico(antibiotico):
        conexion.execute("UPDATE antibioticos SET nombre_producto = ?, dosis = ?, tipo_animal = ?, precio = ? WHERE id = ?", (antibiotico.nombre_producto, antibiotico.dosis, antibiotico.tipo_animal, antibiotico.precio, antibiotico.id))
        conexion.commit()

    def borrar_antibiotico(id):
        conexion.execute("DELETE FROM antibioticos WHERE id = ?", (id,))
        conexion.commit()

