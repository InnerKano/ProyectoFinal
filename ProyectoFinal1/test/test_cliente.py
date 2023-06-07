from model.cliente import Cliente
import pytest

def test_creacion_cliente():
    #Cliente con un nombre y una cédula
    cliente = Cliente(nombre="Juan", cedula="123456")
    assert cliente.nombre == "Juan"
    assert cliente.cedula == "123456"

def test_creacion_cliente_sin_nombre():
    #excepción si no se proporciona un nombre
    with pytest.raises(TypeError):
        Cliente(cedula="123456")

def test_creacion_cliente_sin_cedula():
    #excepción si no se proporciona una cédula
    with pytest.raises(TypeError):
        Cliente(nombre="Juan")

def test_cambio_nombre():
    #cambiar el nombre de un cliente después de crear la instancia
    cliente = Cliente(nombre="Juan", cedula="123456")
    cliente.nombre = "Kevin"
    assert cliente.nombre == "Kevin"

def test_cambio_cedula():
    #cambiar la cédula de un cliente después de crear la instancia
    cliente = Cliente(nombre="Juan", cedula="123456")
    cliente.cedula = "789012"
    assert cliente.cedula == "789012"
