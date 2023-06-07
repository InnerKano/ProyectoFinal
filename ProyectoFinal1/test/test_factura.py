from datetime import datetime
from model.cliente import Cliente
from model.producto import Producto
from model.factura import Factura

def test_creacion_factura():
    cliente = Cliente(nombre="Juan", cedula="123456")

    producto1 = Producto(nombre="Producto 1", precio=100)
    producto2 = Producto(nombre="Producto 2", precio=200)
    producto3 = Producto(nombre="Producto 3", precio=300)

    fecha = datetime.now()
    factura = Factura(cliente=cliente, productos=[producto1, producto2, producto3], numero=1, fecha=fecha)

    assert factura.cliente == cliente
    assert factura.fecha == fecha
    assert factura.productos == [producto1, producto2, producto3]
    assert factura.valor_total == 600
    assert factura.numero == 1


