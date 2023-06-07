from model.antibiotico import Antibiotico
import pytest

def test_creacion_antibiotico():
    #Antibiotico con un nombre, precio, dosis y tipo de animal específicos
    antibiotico = Antibiotico(nombre="Antibiotico A", precio=10.0, dosis=5, tipo_animal="Perro")
    assert antibiotico.nombre == "Antibiotico A"
    assert antibiotico.precio == 10.0
    assert antibiotico.dosis == 5
    assert antibiotico.tipo_animal == "Perro"

def test_creacion_antibiotico_sin_nombre():
    #excepción si no se proporciona un nombre
    with pytest.raises(TypeError):
        Antibiotico(precio=10.0, dosis=5, tipo_animal="Perro")

def test_creacion_antibiotico_sin_precio():
    #excepción si no se proporciona un precio
    with pytest.raises(TypeError):
        Antibiotico(nombre="Antibiotico A", dosis=5, tipo_animal="Perro")

def test_creacion_antibiotico_sin_dosis():
    # Verificamos que se lance una excepción si no se proporciona una dosis
    with pytest.raises(TypeError):
        Antibiotico(nombre="Antibiotico A", precio=10.0, tipo_animal="Perro")

def test_creacion_antibiotico_sin_tipo_animal():
    #excepción si no se proporciona un tipo de animal
    with pytest.raises(TypeError):
        Antibiotico(nombre="Antibiotico A", precio=10.0, dosis=5)

def test_cambio_nombre():
    #Cambiar el nombre de un antibiotico después de crear la instancia
    antibiotico = Antibiotico(nombre="Antibiotico A", precio=10.0, dosis=5, tipo_animal="Perro")
    antibiotico.nombre = "Antibiotico B"
    assert antibiotico.nombre == "Antibiotico B"

def test_cambio_precio():
    # Cambiar el precio de un antibiotico después de crear la instancia
    antibiotico = Antibiotico(nombre="Antibiotico A", precio=10.0, dosis=5, tipo_animal="Perro")
    antibiotico.precio = 20.0
    assert antibiotico.precio == 20.0

def test_cambio_dosis():
    # Cambiar la dosis de un antibiotico después de crear la instancia
    antibiotico = Antibiotico(nombre="Antibiotico A", precio=10.0, dosis=5, tipo_animal="Perro")
    antibiotico.dosis = 10
    assert antibiotico.dosis == 10

def test_cambio_tipo_animal():
    # Verificamos que se pueda cambiar el tipo de animal de un antibiotico después de crear la instancia
    antibiotico = Antibiotico(nombre="Antibiotico A", precio=10.0, dosis=5, tipo_animal="Perro")
    antibiotico.tipo_animal = "Gato"
    assert antibiotico.tipo_animal == "Gato"
