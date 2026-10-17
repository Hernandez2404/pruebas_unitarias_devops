import pytest
from src.calculadora import (
    sumar,
    restar,
    multiplicar,
    dividir,
    potencia,
    raiz_cuadrada,
    promedio,
    maximo,
    minimo,
    calcular_area_rectangulo,
    calcular_perimetro_rectangulo,
)


# ---------- sumar ----------
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


def test_sumar_dos_negativos():
    # Arrange
    a, b = -4, -6
    # Act
    resultado = sumar(a, b)
    # Assert
    assert resultado == -10


def test_sumar_con_cero_devuelve_el_mismo_numero():
    # Arrange
    a, b = 42, 0
    # Act
    resultado = sumar(a, b)
    # Assert
    assert resultado == 42


def test_sumar_texto_con_numero_lanza_type_error():
    # Arrange
    a, b = "5", 3
    # Act + Assert
    with pytest.raises(TypeError):
        sumar(a, b)


def test_sumar_none_lanza_type_error():
    # Arrange
    a, b = None, 3
    # Act + Assert
    with pytest.raises(TypeError):
        sumar(a, b)


# ---------- restar ----------
def test_restar_resultado_negativo():
    # Arrange
    a, b = 3, 10
    # Act
    resultado = restar(a, b)
    # Assert
    assert resultado == -7


def test_restar_mismo_numero_da_cero():
    # Arrange
    a, b = 8, 8
    # Act
    resultado = restar(a, b)
    # Assert
    assert resultado == 0


def test_restar_numero_negativo_equivale_a_sumar():
    # Arrange
    a, b = 5, -3
    # Act
    resultado = restar(a, b)
    # Assert
    assert resultado == 8


def test_restar_decimales_usa_aproximacion():
    # Arrange
    a, b = 0.3, 0.1
    # Act
    resultado = restar(a, b)
    # Assert
    assert resultado == pytest.approx(0.2)


def test_restar_texto_lanza_type_error():
    # Arrange
    a, b = "10", 4
    # Act + Assert
    with pytest.raises(TypeError):
        restar(a, b)


# ---------- multiplicar ----------
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


def test_multiplicar_positivo_por_negativo_da_negativo():
    # Arrange
    a, b = 6, -3
    # Act
    resultado = multiplicar(a, b)
    # Assert
    assert resultado == -18


def test_multiplicar_decimales_usa_aproximacion():
    # Arrange
    a, b = 0.1, 3
    # Act
    resultado = multiplicar(a, b)
    # Assert
    assert resultado == pytest.approx(0.3)


def test_multiplicar_numeros_muy_grandes_no_pierde_precision():
    # Arrange
    a, b = 10**20, 10**20
    # Act
    resultado = multiplicar(a, b)
    # Assert
    assert resultado == 10**40


def test_multiplicar_none_lanza_type_error():
    # Arrange
    a, b = None, 5
    # Act + Assert
    with pytest.raises(TypeError):
        multiplicar(a, b)


# ---------- dividir ----------
def test_dividir_exacta():
    # Arrange
    a, b = 10, 4
    # Act
    resultado = dividir(a, b)
    # Assert
    assert resultado == 2.5


def test_dividir_negativo_entre_positivo_da_negativo():
    # Arrange
    a, b = -12, 4
    # Act
    resultado = dividir(a, b)
    # Assert
    assert resultado == -3


def test_dividir_cero_entre_numero_da_cero():
    # Arrange
    a, b = 0, 7
    # Act
    resultado = dividir(a, b)
    # Assert
    assert resultado == 0


def test_dividir_entera_devuelve_float():
    # Arrange
    a, b = 9, 3
    # Act
    resultado = dividir(a, b)
    # Assert  (división real "/", no entera "//")
    assert isinstance(resultado, float)


def test_dividir_por_cero_lanza_error():
    # Arrange
    a, b = 10, 0
    # Act + Assert
    with pytest.raises(ValueError):
        dividir(a, b)


def test_dividir_por_cero_decimal_lanza_error():
    # Arrange
    a, b = 10, 0.0
    # Act + Assert
    with pytest.raises(ValueError):
        dividir(a, b)


def test_dividir_por_cero_mensaje_descriptivo():
    # Arrange
    a, b = 5, 0
    # Act + Assert
    with pytest.raises(ValueError, match="dividir por cero"):
        dividir(a, b)


def test_dividir_texto_lanza_type_error():
    # Arrange
    a, b = "10", 2
    # Act + Assert
    with pytest.raises(TypeError):
        dividir(a, b)


# ---------- potencia ----------
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


def test_potencia_base_negativa_exponente_par_da_positivo():
    # Arrange
    base, exponente = -3, 2
    # Act
    resultado = potencia(base, exponente)
    # Assert
    assert resultado == 9


def test_potencia_base_negativa_exponente_impar_da_negativo():
    # Arrange
    base, exponente = -2, 3
    # Act
    resultado = potencia(base, exponente)
    # Assert
    assert resultado == -8


def test_potencia_exponente_fraccionario_equivale_a_raiz():
    # Arrange
    base, exponente = 9, 0.5
    # Act
    resultado = potencia(base, exponente)
    # Assert
    assert resultado == pytest.approx(3)


def test_potencia_cero_elevado_a_cero_da_uno():
    # Arrange
    base, exponente = 0, 0
    # Act
    resultado = potencia(base, exponente)
    # Assert
    assert resultado == 1


# ---------- raiz_cuadrada ----------
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


def test_raiz_cuadrada_de_decimal():
    # Arrange
    numero = 2.25
    # Act
    resultado = raiz_cuadrada(numero)
    # Assert
    assert resultado == pytest.approx(1.5)


def test_raiz_cuadrada_no_exacta_usa_aproximacion():
    # Arrange
    numero = 2
    # Act
    resultado = raiz_cuadrada(numero)
    # Assert
    assert resultado == pytest.approx(1.41421356)


def test_raiz_cuadrada_negativo_lanza_error():
    # Arrange
    numero = -4
    # Act + Assert
    with pytest.raises(ValueError):
        raiz_cuadrada(numero)


def test_raiz_cuadrada_negativo_decimal_lanza_error():
    # Arrange
    numero = -0.25
    # Act + Assert
    with pytest.raises(ValueError):
        raiz_cuadrada(numero)


def test_raiz_cuadrada_texto_lanza_type_error():
    # Arrange
    numero = "16"
    # Act + Assert
    with pytest.raises(TypeError):
        raiz_cuadrada(numero)


# ---------- promedio ----------
def test_promedio_lista_de_enteros():
    # Arrange
    lista = [2, 4, 6, 8]
    # Act
    resultado = promedio(lista)
    # Assert
    assert resultado == 5


def test_promedio_un_solo_elemento_devuelve_ese_elemento():
    # Arrange
    lista = [7]
    # Act
    resultado = promedio(lista)
    # Assert
    assert resultado == 7


def test_promedio_con_negativos():
    # Arrange
    lista = [-10, 0, 10, 20]
    # Act
    resultado = promedio(lista)
    # Assert
    assert resultado == 5


def test_promedio_decimales_usa_aproximacion():
    # Arrange
    lista = [0.1, 0.2, 0.3]
    # Act
    resultado = promedio(lista)
    # Assert
    assert resultado == pytest.approx(0.2)


def test_promedio_lista_vacia_lanza_error():
    # Arrange
    lista = []
    # Act + Assert
    with pytest.raises(ValueError, match="vacía"):
        promedio(lista)


def test_promedio_none_lanza_error():
    # Arrange
    lista = None
    # Act + Assert
    with pytest.raises(ValueError):
        promedio(lista)


def test_promedio_con_texto_lanza_type_error():
    # Arrange
    lista = [1, "2", 3]
    # Act + Assert
    with pytest.raises(TypeError):
        promedio(lista)


# ---------- maximo ----------
def test_maximo_lista_desordenada():
    # Arrange
    lista = [3, 9, 1, 7]
    # Act
    resultado = maximo(lista)
    # Assert
    assert resultado == 9


def test_maximo_en_la_primera_posicion():
    # Arrange
    lista = [10, 3, 2]
    # Act
    resultado = maximo(lista)
    # Assert
    assert resultado == 10


def test_maximo_todos_negativos():
    # Arrange
    lista = [-5, -2, -9]
    # Act
    resultado = maximo(lista)
    # Assert
    assert resultado == -2


def test_maximo_un_solo_elemento():
    # Arrange
    lista = [4]
    # Act
    resultado = maximo(lista)
    # Assert
    assert resultado == 4


def test_maximo_con_repetidos():
    # Arrange
    lista = [5, 8, 8, 2]
    # Act
    resultado = maximo(lista)
    # Assert
    assert resultado == 8


def test_maximo_decimales():
    # Arrange
    lista = [1.5, 2.75, 2.7]
    # Act
    resultado = maximo(lista)
    # Assert
    assert resultado == 2.75


def test_maximo_lista_vacia_lanza_error():
    # Arrange
    lista = []
    # Act + Assert
    with pytest.raises(ValueError):
        maximo(lista)


def test_maximo_mezcla_texto_y_numero_lanza_type_error():
    # Arrange
    lista = [1, "a"]
    # Act + Assert
    with pytest.raises(TypeError):
        maximo(lista)


# ---------- minimo ----------
def test_minimo_todos_positivos():
    # Arrange
    lista = [3, 7, 5]
    # Act
    resultado = minimo(lista)
    # Assert
    assert resultado == 3


def test_minimo_un_solo_elemento_positivo():
    # Arrange
    lista = [5]
    # Act
    resultado = minimo(lista)
    # Assert
    assert resultado == 5


def test_minimo_decimales_positivos():
    # Arrange
    lista = [2.5, 1.5, 3.0]
    # Act
    resultado = minimo(lista)
    # Assert
    assert resultado == 1.5


def test_minimo_todos_negativos():
    # Arrange
    lista = [-3, -8, -1]
    # Act
    resultado = minimo(lista)
    # Assert
    assert resultado == -8


def test_minimo_mezcla_positivos_y_negativos():
    # Arrange
    lista = [4, -2, 9]
    # Act
    resultado = minimo(lista)
    # Assert
    assert resultado == -2


def test_minimo_con_cero():
    # Arrange
    lista = [0, 4, 2]
    # Act
    resultado = minimo(lista)
    # Assert
    assert resultado == 0


def test_minimo_lista_vacia_lanza_error():
    # Arrange
    lista = []
    # Act + Assert
    with pytest.raises(ValueError):
        minimo(lista)


def test_minimo_mezcla_texto_y_numero_lanza_type_error():
    # Arrange
    lista = [1, "a"]
    # Act + Assert
    with pytest.raises(TypeError):
        minimo(lista)


# ---------- calcular_area_rectangulo ----------
def test_calcular_area_rectangulo_valores_positivos():
    # Arrange
    base, altura = 5, 3
    # Act
    resultado = calcular_area_rectangulo(base, altura)
    # Assert
    assert resultado == 15


def test_calcular_area_rectangulo_decimales_usa_aproximacion():
    # Arrange
    base, altura = 2.5, 4.2
    # Act
    resultado = calcular_area_rectangulo(base, altura)
    # Assert
    assert resultado == pytest.approx(10.5)


def test_calcular_area_rectangulo_base_cero_da_cero():
    # Arrange
    base, altura = 0, 10
    # Act
    resultado = calcular_area_rectangulo(base, altura)
    # Assert
    assert resultado == 0


def test_calcular_area_rectangulo_base_negativa_lanza_error():
    # Arrange
    base, altura = -5, 3
    # Act + Assert
    with pytest.raises(ValueError):
        calcular_area_rectangulo(base, altura)


def test_calcular_area_rectangulo_altura_negativa_lanza_error():
    # Arrange
    base, altura = 5, -3
    # Act + Assert
    with pytest.raises(ValueError):
        calcular_area_rectangulo(base, altura)


def test_calcular_area_rectangulo_texto_lanza_type_error():
    # Arrange
    base, altura = "5", 3
    # Act + Assert
    with pytest.raises(TypeError):
        calcular_area_rectangulo(base, altura)


# ---------- calcular_perimetro_rectangulo ----------
def test_calcular_perimetro_rectangulo_valores_positivos():
    # Arrange
    base, altura = 5, 3
    # Act
    resultado = calcular_perimetro_rectangulo(base, altura)
    # Assert
    assert resultado == 16


def test_calcular_perimetro_rectangulo_decimales_usa_aproximacion():
    # Arrange
    base, altura = 1.5, 2.25
    # Act
    resultado = calcular_perimetro_rectangulo(base, altura)
    # Assert
    assert resultado == pytest.approx(7.5)


def test_calcular_perimetro_rectangulo_ambos_cero_da_cero():
    # Arrange
    base, altura = 0, 0
    # Act
    resultado = calcular_perimetro_rectangulo(base, altura)
    # Assert
    assert resultado == 0


@pytest.mark.parametrize("base, altura", [(-1, 5), (5, -1), (-2, -3)])
def test_calcular_perimetro_rectangulo_medida_negativa_lanza_error(base, altura):
    # Arrange: base y altura vienen del parametrize
    # Act + Assert
    with pytest.raises(ValueError):
        calcular_perimetro_rectangulo(base, altura)
