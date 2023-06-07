from model.producto import Producto

def test_producto_init():
    p = Producto("Arroz", 2500)
    assert p.nombre == "Arroz"
    assert p.precio == 2500
