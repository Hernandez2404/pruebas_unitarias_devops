import pytest
from src.calculadora import sumar, restar, multiplicar, dividir, potencia, raiz_cuadrada


def test_sumar_positivos():
    # Arrange
    a, b = 7, 5
    # Act
    resultado = sumar(a, b)
    # Assert
    assert resultado == 12


def test_sumar_decimales_usa_aproximacion():
    # Arrange
    a, b = 0.1, 0.2
    # Act
    resultado = sumar(a, b)
    # Assert
    assert resultado == pytest.approx(0.3)


def test_restar_resultado_negativo():
    # Arrange
    a, b = 3, 10
    # Act
    resultado = restar(a, b)
    # Assert
    assert resultado == -7


def test_multiplicar_por_cero():
    # Arrange
    a, b = 125, 0
    # Act
    resultado = multiplicar(a, b)
    # Assert
    assert resultado == 0


def test_multiplicar_dos_negativos_da_positivo():
    # Arrange
    a, b = -4, -5
    # Act
    resultado = multiplicar(a, b)
    # Assert
    assert resultado == 20


def test_dividir_exacta():
    # Arrange
    a, b = 10, 4
    # Act
    resultado = dividir(a, b)
    # Assert
    assert resultado == 2.5


def test_dividir_por_cero_lanza_error():
    # Arrange
    a, b = 10, 0
    # Act + Assert
    with pytest.raises(ValueError):
        dividir(a, b)


def test_potencia_exponente_cero_da_uno():
    # Arrange
    base, exponente = 9, 0
    # Act
    resultado = potencia(base, exponente)
    # Assert
    assert resultado == 1


def test_potencia_exponente_negativo():
    # Arrange
    base, exponente = 2, -2
    # Act
    resultado = potencia(base, exponente)
    # Assert
    assert resultado == pytest.approx(0.25)


def test_potencia_cero_con_exponente_negativo_lanza_value_error():
    # Arrange
    base, exponente = 0, -1
    # Act + Assert
    with pytest.raises(ValueError):
        potencia(base, exponente)


def test_raiz_cuadrada_numero_positivo():
    # Arrange
    numero = 16
    # Act
    resultado = raiz_cuadrada(numero)
    # Assert
    assert resultado == 4


def test_raiz_cuadrada_de_cero():
    # Arrange
    numero = 0
    # Act
    resultado = raiz_cuadrada(numero)
    # Assert
    assert resultado == 0


def test_raiz_cuadrada_negativo_lanza_error():
    # Arrange
    numero = -4
    # Act + Assert
    with pytest.raises(ValueError):
        raiz_cuadrada(numero)
