from datetime import datetime
from model.cliente import Cliente
from model.producto import Producto
from model.pedido import Pedido
import pytest

def test_creacion_pedido():
    #Pedido con un cliente, fecha y lista de productos específicos
    cliente = Cliente(nombre="Juan", cedula="123456")
    fecha = datetime.now()
    producto1 = Producto(nombre="Leche", precio=1.5)
    producto2 = Producto(nombre="Pan", precio=0.5)
    productos = [producto1, producto2]
    pedido = Pedido(cliente=cliente, fecha=fecha, productos=productos)
    assert pedido.cliente == cliente
    assert pedido.fecha == fecha
    assert pedido.productos == productos

def test_creacion_pedido_sin_cliente():
    #excepción si no se proporciona un cliente
    with pytest.raises(TypeError):
        fecha = datetime.now()
        producto1 = Producto(nombre="Leche", precio=1.5)
        producto2 = Producto(nombre="Pan", precio=0.5)
        productos = [producto1, producto2]
        Pedido(fecha=fecha, productos=productos)

def test_creacion_pedido_sin_fecha():
    #excepción si no se proporciona una fecha
    with pytest.raises(TypeError):
        cliente = Cliente(nombre="Juan", cedula="123456")
        producto1 = Producto(nombre="Leche", precio=1.5)
        producto2 = Producto(nombre="Pan", precio=0.5)
        productos = [producto1, producto2]
        Pedido(cliente=cliente, productos=productos)

def test_creacion_pedido_sin_productos():
    #excepción si no se proporcionan productos
    with pytest.raises(TypeError):
        cliente = Cliente(nombre="Juan", cedula="123456")
        fecha = datetime.now()
        Pedido(cliente=cliente, fecha=fecha)
