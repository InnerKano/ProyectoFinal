from datetime import datetime
from model.cliente import Cliente
from model.producto import Producto

class Pedido:
    def __init__(self, cliente: Cliente, fecha: datetime, productos: list[Producto]):
        self.cliente = cliente
        self.fecha = fecha
        self.productos = productos