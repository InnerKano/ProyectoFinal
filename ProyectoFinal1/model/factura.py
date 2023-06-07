from datetime import datetime
from model.cliente import Cliente
from model.producto import Producto

class Factura:
    def __init__(self, cliente: Cliente, productos: list[Producto], numero: int, fecha: datetime):
        self.cliente = cliente
        self.fecha = fecha
        self.productos = productos
        self.valor_total = sum(p.precio for p in productos)
        self.numero = numero
