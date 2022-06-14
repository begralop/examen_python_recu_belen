import pytest
import main as m

def test_get_name_description():

    diccionario = m.read_data("stops.csv", "stops_data.csv")

    # Testeo que el nombre recibido es correcto
    name = "Pla del Reial"
    name_ok, description_ok = m.get_name_description("1021", diccionario)
    assert name_ok == name

def test_search_by_lon():

    diccionario = m.read_data("stops.csv", "stops_data.csv")
    clave = "1096"
    clave_ok= m.search_by_lon("728257.03", diccionario)
    assert clave_ok == clave


def test_valuerror_get_name_description():
    diccionario = m.read_data("stops.csv", "stops_data.csv")

    # Testeo que el nombre recibido es correcto
    name = "Pla del Reial"
    name_ok, description_ok = m.get_name_description("1021", diccionario)

    with pytest.raises(ValueError):
        m.get_name_description("111111", diccionario)

def test_valueerror_search_by_lon():

    diccionario = m.read_data("stops.csv", "stops_data.csv")
    clave = "1096"
    clave_ok= m.search_by_lon("728257.03", diccionario)

    with pytest.raises(ValueError):
        m.search_by_lon("728222257.22", diccionario)