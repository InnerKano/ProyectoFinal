from model.producto import Producto
from datetime import datetime

class ProductoControl(Producto):
    def __init__(self, nombre: str, precio: float, registro_ica: str, frecuencia_aplicacion: int, tipo: str, fecha_ultima_aplicacion: datetime):
        super().__init__(nombre, precio)
        self.registro_ica = registro_ica
        self.frecuencia_aplicacion = frecuencia_aplicacion
        self.tipo = tipo
        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion

class ControlPlagas(ProductoControl):
    def __init__(self, ica, nombre, frecuencia_aplicacion, valor, periodo_carencia):
        super().__init__(nombre, valor, ica, frecuencia_aplicacion, "control_plagas", None)
        self.periodo_carencia = periodo_carencia

class ControlFertilizantes(ProductoControl):
    def __init__(self, ica, nombre, frecuencia_aplicacion, valor, fecha_ultima_aplicacion):
        super().__init__(nombre, valor, ica, frecuencia_aplicacion, "control_fertilizantes", fecha_ultima_aplicacion)
