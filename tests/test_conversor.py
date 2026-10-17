import pytest
from src.conversor import (
    celsius_a_fahrenheit,
    fahrenheit_a_celsius,
    celsius_a_kelvin,
    kelvin_a_celsius,
    metros_a_kilometros,
    kilometros_a_metros,
    libras_a_kilogramos,
    kilogramos_a_libras,
    galones_a_litros,
    litros_a_galones,
    millas_a_kilometros,
    kilometros_a_millas,
    pies_a_metros,
    metros_a_pies,
    onzas_a_gramos,
    gramos_a_onzas,
)


# ---------- celsius_a_fahrenheit ----------
def test_celsius_a_fahrenheit_punto_de_congelacion():
    # Arrange
    celsius = 0
    # Act
    resultado = celsius_a_fahrenheit(celsius)
    # Assert
    assert resultado == 32


def test_celsius_a_fahrenheit_punto_de_ebullicion():
    # Arrange
    celsius = 100
    # Act
    resultado = celsius_a_fahrenheit(celsius)
    # Assert
    assert resultado == 212


def test_celsius_a_fahrenheit_menos_cuarenta_es_igual_en_ambas_escalas():
    # Arrange
    celsius = -40
    # Act
    resultado = celsius_a_fahrenheit(celsius)
    # Assert
    assert resultado == -40


def test_celsius_a_fahrenheit_decimal_usa_aproximacion():
    # Arrange
    celsius = 37.5
    # Act
    resultado = celsius_a_fahrenheit(celsius)
    # Assert
    assert resultado == pytest.approx(99.5)


def test_celsius_a_fahrenheit_cero_absoluto():
    # Arrange
    celsius = -273.15
    # Act
    resultado = celsius_a_fahrenheit(celsius)
    # Assert
    assert resultado == pytest.approx(-459.67)


def test_celsius_a_fahrenheit_none_lanza_type_error():
    # Arrange
    celsius = None
    # Act + Assert
    with pytest.raises(TypeError):
        celsius_a_fahrenheit(celsius)


# ---------- fahrenheit_a_celsius ----------
def test_fahrenheit_a_celsius_punto_de_congelacion():
    # Arrange
    fahrenheit = 32
    # Act
    resultado = fahrenheit_a_celsius(fahrenheit)
    # Assert
    assert resultado == 0


def test_fahrenheit_a_celsius_punto_de_ebullicion():
    # Arrange
    fahrenheit = 212
    # Act
    resultado = fahrenheit_a_celsius(fahrenheit)
    # Assert
    assert resultado == 100


def test_fahrenheit_a_celsius_menos_cuarenta_es_igual_en_ambas_escalas():
    # Arrange
    fahrenheit = -40
    # Act
    resultado = fahrenheit_a_celsius(fahrenheit)
    # Assert
    assert resultado == -40


def test_fahrenheit_a_celsius_temperatura_corporal_usa_aproximacion():
    # Arrange
    fahrenheit = 98.6
    # Act
    resultado = fahrenheit_a_celsius(fahrenheit)
    # Assert
    assert resultado == pytest.approx(37)


def test_fahrenheit_a_celsius_texto_lanza_type_error():
    # Arrange
    fahrenheit = "50"
    # Act + Assert
    with pytest.raises(TypeError):
        fahrenheit_a_celsius(fahrenheit)


# ---------- celsius_a_kelvin ----------
def test_celsius_a_kelvin_cero_celsius():
    # Arrange
    celsius = 0
    # Act
    resultado = celsius_a_kelvin(celsius)
    # Assert
    assert resultado == pytest.approx(273.15)


def test_celsius_a_kelvin_punto_de_ebullicion():
    # Arrange
    celsius = 100
    # Act
    resultado = celsius_a_kelvin(celsius)
    # Assert
    assert resultado == pytest.approx(373.15)


def test_celsius_a_kelvin_cero_absoluto_da_cero():
    # Arrange
    celsius = -273.15
    # Act
    resultado = celsius_a_kelvin(celsius)
    # Assert
    assert resultado == pytest.approx(0)


def test_celsius_a_kelvin_decimal_usa_aproximacion():
    # Arrange
    celsius = 25.5
    # Act
    resultado = celsius_a_kelvin(celsius)
    # Assert
    assert resultado == pytest.approx(298.65)


def test_celsius_a_kelvin_texto_lanza_type_error():
    # Arrange
    celsius = "10"
    # Act + Assert
    with pytest.raises(TypeError):
        celsius_a_kelvin(celsius)


# ---------- kelvin_a_celsius ----------
def test_kelvin_a_celsius_punto_de_congelacion():
    # Arrange
    kelvin = 273.15
    # Act
    resultado = kelvin_a_celsius(kelvin)
    # Assert
    assert resultado == pytest.approx(0)


def test_kelvin_a_celsius_punto_de_ebullicion():
    # Arrange
    kelvin = 373.15
    # Act
    resultado = kelvin_a_celsius(kelvin)
    # Assert
    assert resultado == pytest.approx(100)


def test_kelvin_a_celsius_cero_absoluto_es_valido():
    # Arrange
    kelvin = 0
    # Act
    resultado = kelvin_a_celsius(kelvin)
    # Assert
    assert resultado == pytest.approx(-273.15)


@pytest.mark.parametrize("kelvin", [-0.01, -100])
def test_kelvin_a_celsius_bajo_cero_absoluto_lanza_error(kelvin):
    # Arrange: no existen temperaturas por debajo de 0 K
    # Act + Assert
    with pytest.raises(ValueError):
        kelvin_a_celsius(kelvin)


def test_kelvin_a_celsius_texto_lanza_type_error():
    # Arrange
    kelvin = "300"
    # Act + Assert
    with pytest.raises(TypeError):
        kelvin_a_celsius(kelvin)


# ---------- metros_a_kilometros ----------
def test_metros_a_kilometros_valor_conocido():
    # Arrange
    metros = 1500
    # Act
    resultado = metros_a_kilometros(metros)
    # Assert
    assert resultado == pytest.approx(1.5)


def test_metros_a_kilometros_cero_da_cero():
    # Arrange
    metros = 0
    # Act
    resultado = metros_a_kilometros(metros)
    # Assert
    assert resultado == 0


def test_metros_a_kilometros_negativo_lanza_error():
    # Arrange
    metros = -0.01
    # Act + Assert
    with pytest.raises(ValueError, match="distancia no puede ser negativa"):
        metros_a_kilometros(metros)


def test_metros_a_kilometros_texto_lanza_type_error():
    # Arrange
    metros = "100"
    # Act + Assert
    with pytest.raises(TypeError):
        metros_a_kilometros(metros)


# ---------- kilometros_a_metros ----------
def test_kilometros_a_metros_valor_conocido():
    # Arrange
    kilometros = 2.5
    # Act
    resultado = kilometros_a_metros(kilometros)
    # Assert
    assert resultado == pytest.approx(2500)


def test_kilometros_a_metros_cero_da_cero():
    # Arrange
    kilometros = 0
    # Act
    resultado = kilometros_a_metros(kilometros)
    # Assert
    assert resultado == 0


def test_kilometros_a_metros_negativo_lanza_error():
    # Arrange
    kilometros = -3
    # Act + Assert
    with pytest.raises(ValueError, match="distancia no puede ser negativa"):
        kilometros_a_metros(kilometros)


# ---------- libras_a_kilogramos ----------
def test_libras_a_kilogramos_valor_conocido():
    # Arrange
    libras = 10
    # Act
    resultado = libras_a_kilogramos(libras)
    # Assert
    assert resultado == pytest.approx(4.53592)


def test_libras_a_kilogramos_cero_da_cero():
    # Arrange
    libras = 0
    # Act
    resultado = libras_a_kilogramos(libras)
    # Assert
    assert resultado == 0


def test_libras_a_kilogramos_negativo_lanza_error():
    # Arrange
    libras = -1
    # Act + Assert
    with pytest.raises(ValueError, match="peso no puede ser negativo"):
        libras_a_kilogramos(libras)


def test_libras_a_kilogramos_none_lanza_type_error():
    # Arrange
    libras = None
    # Act + Assert
    with pytest.raises(TypeError):
        libras_a_kilogramos(libras)


# ---------- kilogramos_a_libras ----------
def test_kilogramos_a_libras_valor_conocido():
    # Arrange
    kilogramos = 45.3592
    # Act
    resultado = kilogramos_a_libras(kilogramos)
    # Assert
    assert resultado == pytest.approx(100)


def test_kilogramos_a_libras_cero_da_cero():
    # Arrange
    kilogramos = 0
    # Act
    resultado = kilogramos_a_libras(kilogramos)
    # Assert
    assert resultado == 0


def test_kilogramos_a_libras_negativo_lanza_error():
    # Arrange
    kilogramos = -2
    # Act + Assert
    with pytest.raises(ValueError, match="peso no puede ser negativo"):
        kilogramos_a_libras(kilogramos)


# ---------- galones_a_litros ----------
def test_galones_a_litros_valor_conocido():
    # Arrange
    galones = 2
    # Act
    resultado = galones_a_litros(galones)
    # Assert
    assert resultado == pytest.approx(7.57082)


def test_galones_a_litros_cero_da_cero():
    # Arrange
    galones = 0
    # Act
    resultado = galones_a_litros(galones)
    # Assert
    assert resultado == 0


def test_galones_a_litros_negativo_lanza_error():
    # Arrange
    galones = -1
    # Act + Assert
    with pytest.raises(ValueError, match="volumen no puede ser negativo"):
        galones_a_litros(galones)


# ---------- litros_a_galones ----------
def test_litros_a_galones_valor_conocido():
    # Arrange
    litros = 37.8541
    # Act
    resultado = litros_a_galones(litros)
    # Assert
    assert resultado == pytest.approx(10)


def test_litros_a_galones_cero_da_cero():
    # Arrange
    litros = 0
    # Act
    resultado = litros_a_galones(litros)
    # Assert
    assert resultado == 0


def test_litros_a_galones_negativo_lanza_error():
    # Arrange
    litros = -0.5
    # Act + Assert
    with pytest.raises(ValueError, match="volumen no puede ser negativo"):
        litros_a_galones(litros)


# ---------- millas_a_kilometros ----------
def test_millas_a_kilometros_valor_conocido():
    # Arrange
    millas = 10
    # Act
    resultado = millas_a_kilometros(millas)
    # Assert
    assert resultado == pytest.approx(16.0934)


def test_millas_a_kilometros_cero_da_cero():
    # Arrange
    millas = 0
    # Act
    resultado = millas_a_kilometros(millas)
    # Assert
    assert resultado == 0


def test_millas_a_kilometros_negativo_lanza_error():
    # Arrange
    millas = -5
    # Act + Assert
    with pytest.raises(ValueError, match="distancia no puede ser negativa"):
        millas_a_kilometros(millas)


# ---------- kilometros_a_millas ----------
def test_kilometros_a_millas_valor_conocido():
    # Arrange
    kilometros = 16.0934
    # Act
    resultado = kilometros_a_millas(kilometros)
    # Assert
    assert resultado == pytest.approx(10)


def test_kilometros_a_millas_da_menos_millas_que_kilometros():
    # Arrange: una milla es más larga que un kilómetro
    kilometros = 100
    # Act
    resultado = kilometros_a_millas(kilometros)
    # Assert
    assert resultado < kilometros


def test_kilometros_a_millas_cero_da_cero():
    # Arrange
    kilometros = 0
    # Act
    resultado = kilometros_a_millas(kilometros)
    # Assert
    assert resultado == 0


def test_kilometros_a_millas_negativo_lanza_error():
    # Arrange
    kilometros = -1
    # Act + Assert
    with pytest.raises(ValueError, match="distancia no puede ser negativa"):
        kilometros_a_millas(kilometros)


# ---------- pies_a_metros ----------
def test_pies_a_metros_valor_conocido():
    # Arrange
    pies = 10
    # Act
    resultado = pies_a_metros(pies)
    # Assert
    assert resultado == pytest.approx(3.048)


def test_pies_a_metros_cero_da_cero():
    # Arrange
    pies = 0
    # Act
    resultado = pies_a_metros(pies)
    # Assert
    assert resultado == 0


def test_pies_a_metros_negativo_lanza_error():
    # Arrange
    pies = -6
    # Act + Assert
    with pytest.raises(ValueError, match="distancia no puede ser negativa"):
        pies_a_metros(pies)


# ---------- metros_a_pies ----------
def test_metros_a_pies_valor_conocido():
    # Arrange
    metros = 3.048
    # Act
    resultado = metros_a_pies(metros)
    # Assert
    assert resultado == pytest.approx(10)


def test_metros_a_pies_cero_da_cero():
    # Arrange
    metros = 0
    # Act
    resultado = metros_a_pies(metros)
    # Assert
    assert resultado == 0


def test_metros_a_pies_negativo_lanza_error():
    # Arrange
    metros = -2
    # Act + Assert
    with pytest.raises(ValueError, match="distancia no puede ser negativa"):
        metros_a_pies(metros)


# ---------- onzas_a_gramos ----------
def test_onzas_a_gramos_valor_conocido():
    # Arrange
    onzas = 2
    # Act
    resultado = onzas_a_gramos(onzas)
    # Assert
    assert resultado == pytest.approx(56.699)


def test_onzas_a_gramos_cero_da_cero():
    # Arrange
    onzas = 0
    # Act
    resultado = onzas_a_gramos(onzas)
    # Assert
    assert resultado == 0


def test_onzas_a_gramos_negativo_lanza_error():
    # Arrange
    onzas = -3
    # Act + Assert
    with pytest.raises(ValueError, match="peso no puede ser negativo"):
        onzas_a_gramos(onzas)


# ---------- gramos_a_onzas ----------
def test_gramos_a_onzas_valor_conocido():
    # Arrange
    gramos = 28.3495
    # Act
    resultado = gramos_a_onzas(gramos)
    # Assert
    assert resultado == pytest.approx(1)


def test_gramos_a_onzas_cero_da_cero():
    # Arrange
    gramos = 0
    # Act
    resultado = gramos_a_onzas(gramos)
    # Assert
    assert resultado == 0


def test_gramos_a_onzas_negativo_lanza_error():
    # Arrange
    gramos = -10
    # Act + Assert
    with pytest.raises(ValueError, match="peso no puede ser negativo"):
        gramos_a_onzas(gramos)


def test_gramos_a_onzas_texto_lanza_type_error():
    # Arrange
    gramos = "500"
    # Act + Assert
    with pytest.raises(TypeError):
        gramos_a_onzas(gramos)


# ---------- conversiones de ida y vuelta ----------
@pytest.mark.parametrize(
    "ida, vuelta",
    [
        (celsius_a_fahrenheit, fahrenheit_a_celsius),
        (celsius_a_kelvin, kelvin_a_celsius),
        (metros_a_kilometros, kilometros_a_metros),
        (libras_a_kilogramos, kilogramos_a_libras),
        (galones_a_litros, litros_a_galones),
        (millas_a_kilometros, kilometros_a_millas),
        (pies_a_metros, metros_a_pies),
        (onzas_a_gramos, gramos_a_onzas),
    ],
    ids=[
        "celsius-fahrenheit",
        "celsius-kelvin",
        "metros-kilometros",
        "libras-kilogramos",
        "galones-litros",
        "millas-kilometros",
        "pies-metros",
        "onzas-gramos",
    ],
)
def test_conversion_ida_y_vuelta_devuelve_el_valor_original(ida, vuelta):
    # Arrange
    valor = 42.5
    # Act
    resultado = vuelta(ida(valor))
    # Assert
    assert resultado == pytest.approx(valor)
