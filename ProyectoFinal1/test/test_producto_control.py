from datetime import datetime
from model.producto_control import ControlPlagas, ControlFertilizantes

def test_creacion_control_plagas():
    control_plagas = ControlPlagas("ICA-1234", "Control Plagas 1", 30, 25000, 15)
    assert control_plagas.registro_ica == "ICA-1234"
    assert control_plagas.nombre == "Control Plagas 1"
    assert control_plagas.frecuencia_aplicacion == 30
    assert control_plagas.precio == 25000
    assert control_plagas.tipo == "control_plagas"
    assert control_plagas.fecha_ultima_aplicacion is None
    assert control_plagas.periodo_carencia == 15

def test_creacion_control_fertilizantes():
    fecha = datetime.now()
    control_fertilizantes = ControlFertilizantes("ICA-5678", "Control Fertilizantes 1", 7, 12000, fecha)
    assert control_fertilizantes.registro_ica == "ICA-5678"
    assert control_fertilizantes.nombre == "Control Fertilizantes 1"
    assert control_fertilizantes.frecuencia_aplicacion == 7
    assert control_fertilizantes.precio == 12000
    assert control_fertilizantes.tipo == "control_fertilizantes"
    assert control_fertilizantes.fecha_ultima_aplicacion == fecha

