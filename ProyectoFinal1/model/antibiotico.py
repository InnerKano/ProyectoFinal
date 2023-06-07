from model.producto import Producto

class Antibiotico(Producto):
    def __init__(self, nombre: str, precio: float, dosis: int, tipo_animal: str):
        super().__init__(nombre, precio)
        self.dosis = dosis
        self.tipo_animal = tipo_animal
