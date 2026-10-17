import pytest
from src.descuentos import (
    aplicar_descuento,
    calcular_descuento,
    calcular_precio_final,
    descuento_por_volumen,
    descuento_cumulativo,
    descuento_apilado,
)


# ---------- aplicar_descuento ----------
def test_aplicar_descuento_caso_normal():
    # Arrange
    precio, porcentaje = 100, 20
    # Act
    resultado = aplicar_descuento(precio, porcentaje)
    # Assert
    assert resultado == pytest.approx(80)


def test_aplicar_descuento_cero_por_ciento_no_cambia_el_precio():
    # Arrange
    precio, porcentaje = 250, 0
    # Act
    resultado = aplicar_descuento(precio, porcentaje)
    # Assert
    assert resultado == 250


def test_aplicar_descuento_cien_por_ciento_da_cero():
    # Arrange
    precio, porcentaje = 250, 100
    # Act
    resultado = aplicar_descuento(precio, porcentaje)
    # Assert
    assert resultado == 0


def test_aplicar_descuento_porcentaje_decimal():
    # Arrange
    precio, porcentaje = 80, 12.5
    # Act
    resultado = aplicar_descuento(precio, porcentaje)
    # Assert
    assert resultado == pytest.approx(70)


def test_aplicar_descuento_precio_decimal_usa_aproximacion():
    # Arrange
    precio, porcentaje = 19.99, 10
    # Act
    resultado = aplicar_descuento(precio, porcentaje)
    # Assert
    assert resultado == pytest.approx(17.991)


def test_aplicar_descuento_precio_cero_da_cero():
    # Arrange
    precio, porcentaje = 0, 50
    # Act
    resultado = aplicar_descuento(precio, porcentaje)
    # Assert
    assert resultado == 0


def test_aplicar_descuento_precio_negativo_lanza_error():
    # Arrange
    precio, porcentaje = -100, 10
    # Act + Assert
    with pytest.raises(ValueError, match="precio no puede ser negativo"):
        aplicar_descuento(precio, porcentaje)


@pytest.mark.parametrize("porcentaje", [-0.01, 100.01, 150])
def test_aplicar_descuento_porcentaje_fuera_de_rango_lanza_error(porcentaje):
    # Arrange
    precio = 100
    # Act + Assert
    with pytest.raises(ValueError, match="entre 0 y 100"):
        aplicar_descuento(precio, porcentaje)


def test_aplicar_descuento_precio_texto_lanza_type_error():
    # Arrange
    precio, porcentaje = "100", 10
    # Act + Assert
    with pytest.raises(TypeError):
        aplicar_descuento(precio, porcentaje)


def test_aplicar_descuento_porcentaje_none_lanza_type_error():
    # Arrange
    precio, porcentaje = 100, None
    # Act + Assert
    with pytest.raises(TypeError):
        aplicar_descuento(precio, porcentaje)


# ---------- calcular_descuento ----------
def test_calcular_descuento_caso_normal():
    # Arrange
    precio, porcentaje = 200, 15
    # Act
    resultado = calcular_descuento(precio, porcentaje)
    # Assert
    assert resultado == pytest.approx(30)


def test_calcular_descuento_cero_por_ciento_da_cero():
    # Arrange
    precio, porcentaje = 200, 0
    # Act
    resultado = calcular_descuento(precio, porcentaje)
    # Assert
    assert resultado == 0


def test_calcular_descuento_cien_por_ciento_da_el_precio_completo():
    # Arrange
    precio, porcentaje = 75, 100
    # Act
    resultado = calcular_descuento(precio, porcentaje)
    # Assert
    assert resultado == 75


def test_calcular_descuento_precio_decimal_usa_aproximacion():
    # Arrange
    precio, porcentaje = 49.9, 10
    # Act
    resultado = calcular_descuento(precio, porcentaje)
    # Assert
    assert resultado == pytest.approx(4.99)


def test_calcular_descuento_sumado_al_precio_con_descuento_da_el_original():
    # Arrange
    precio, porcentaje = 120, 35
    # Act
    monto = calcular_descuento(precio, porcentaje)
    precio_con_descuento = aplicar_descuento(precio, porcentaje)
    # Assert
    assert monto + precio_con_descuento == pytest.approx(precio)


def test_calcular_descuento_precio_negativo_lanza_error():
    # Arrange
    precio, porcentaje = -1, 10
    # Act + Assert
    with pytest.raises(ValueError, match="precio no puede ser negativo"):
        calcular_descuento(precio, porcentaje)


@pytest.mark.parametrize("porcentaje", [-5, 101])
def test_calcular_descuento_porcentaje_fuera_de_rango_lanza_error(porcentaje):
    # Arrange
    precio = 100
    # Act + Assert
    with pytest.raises(ValueError, match="entre 0 y 100"):
        calcular_descuento(precio, porcentaje)


def test_calcular_descuento_porcentaje_texto_lanza_type_error():
    # Arrange
    precio, porcentaje = 100, "10"
    # Act + Assert
    with pytest.raises(TypeError):
        calcular_descuento(precio, porcentaje)


# ---------- calcular_precio_final ----------
def test_calcular_precio_final_sin_impuesto_ni_descuento():
    # Arrange
    precio, impuesto, descuento = 100, 0, 0
    # Act
    resultado = calcular_precio_final(precio, impuesto, descuento)
    # Assert
    assert resultado == 100


def test_calcular_precio_final_solo_impuesto():
    # Arrange
    precio, impuesto, descuento = 100, 19, 0
    # Act
    resultado = calcular_precio_final(precio, impuesto, descuento)
    # Assert
    assert resultado == pytest.approx(119)


def test_calcular_precio_final_solo_descuento():
    # Arrange
    precio, impuesto, descuento = 100, 0, 20
    # Act
    resultado = calcular_precio_final(precio, impuesto, descuento)
    # Assert
    assert resultado == pytest.approx(80)


def test_calcular_precio_final_impuesto_sobre_precio_con_descuento():
    # Arrange: 100 con 20 % de descuento = 80; 80 + 19 % de impuesto = 95.2
    precio, impuesto, descuento = 100, 19, 20
    # Act
    resultado = calcular_precio_final(precio, impuesto, descuento)
    # Assert
    assert resultado == pytest.approx(95.2)


def test_calcular_precio_final_descuento_total_no_cobra_impuesto():
    # Arrange: si el producto queda gratis no hay base sobre la cual cobrar impuesto
    precio, impuesto, descuento = 100, 19, 100
    # Act
    resultado = calcular_precio_final(precio, impuesto, descuento)
    # Assert
    assert resultado == pytest.approx(0)


def test_calcular_precio_final_precio_cero_da_cero():
    # Arrange
    precio, impuesto, descuento = 0, 19, 10
    # Act
    resultado = calcular_precio_final(precio, impuesto, descuento)
    # Assert
    assert resultado == 0


def test_calcular_precio_final_precio_negativo_lanza_error():
    # Arrange
    precio, impuesto, descuento = -100, 19, 10
    # Act + Assert
    with pytest.raises(ValueError, match="precio no puede ser negativo"):
        calcular_precio_final(precio, impuesto, descuento)


def test_calcular_precio_final_impuesto_negativo_lanza_error():
    # Arrange
    precio, impuesto, descuento = 100, -19, 10
    # Act + Assert
    with pytest.raises(ValueError, match="impuesto no puede ser negativo"):
        calcular_precio_final(precio, impuesto, descuento)


@pytest.mark.parametrize("descuento", [-1, 101])
def test_calcular_precio_final_descuento_fuera_de_rango_lanza_error(descuento):
    # Arrange
    precio, impuesto = 100, 19
    # Act + Assert
    with pytest.raises(ValueError, match="descuento debe estar entre 0 y 100"):
        calcular_precio_final(precio, impuesto, descuento)


def test_calcular_precio_final_texto_lanza_type_error():
    # Arrange
    precio, impuesto, descuento = "100", 19, 10
    # Act + Assert
    with pytest.raises(TypeError):
        calcular_precio_final(precio, impuesto, descuento)


# ---------- descuento_por_volumen ----------
@pytest.mark.parametrize(
    "cantidad, esperado",
    [
        (9, 90),       # menos de 10: sin descuento
        (10, 95),      # desde 10: 5 %
        (19, 180.5),
        (20, 180),     # desde 20: 10 %
        (49, 441),
        (50, 425),     # desde 50: 15 %
        (99, 841.5),
        (100, 800),    # desde 100: 20 %
    ],
)
def test_descuento_por_volumen_limites_de_cada_rango(cantidad, esperado):
    # Arrange
    precio_unitario = 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == pytest.approx(esperado)


def test_descuento_por_volumen_cantidad_cero_da_cero():
    # Arrange
    cantidad, precio_unitario = 0, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == 0


def test_descuento_por_volumen_cantidad_muy_grande_mantiene_20_por_ciento():
    # Arrange
    cantidad, precio_unitario = 1000, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == pytest.approx(8000)


def test_descuento_por_volumen_precio_unitario_cero_da_cero():
    # Arrange
    cantidad, precio_unitario = 50, 0
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == 0


def test_descuento_por_volumen_cantidad_negativa_lanza_error():
    # Arrange
    cantidad, precio_unitario = -1, 10
    # Act + Assert
    with pytest.raises(ValueError, match="cantidad no puede ser negativa"):
        descuento_por_volumen(cantidad, precio_unitario)


def test_descuento_por_volumen_precio_unitario_negativo_lanza_error():
    # Arrange
    cantidad, precio_unitario = 10, -5
    # Act + Assert
    with pytest.raises(ValueError, match="precio unitario no puede ser negativo"):
        descuento_por_volumen(cantidad, precio_unitario)


def test_descuento_por_volumen_texto_lanza_type_error():
    # Arrange
    cantidad, precio_unitario = "10", 5
    # Act + Assert
    with pytest.raises(TypeError):
        descuento_por_volumen(cantidad, precio_unitario)


# ---------- descuento_cumulativo ----------
def test_descuento_cumulativo_dos_descuentos():
    # Arrange: 100 - 10 % = 90; 90 - 20 % = 72
    precio, descuentos = 100, [10, 20]
    # Act
    resultado = descuento_cumulativo(precio, descuentos)
    # Assert
    assert resultado == pytest.approx(72)


def test_descuento_cumulativo_un_solo_descuento():
    # Arrange
    precio, descuentos = 100, [25]
    # Act
    resultado = descuento_cumulativo(precio, descuentos)
    # Assert
    assert resultado == pytest.approx(75)


def test_descuento_cumulativo_lista_vacia_devuelve_precio():
    # Arrange
    precio, descuentos = 100, []
    # Act
    resultado = descuento_cumulativo(precio, descuentos)
    # Assert
    assert resultado == 100


def test_descuento_cumulativo_none_devuelve_precio():
    # Arrange
    precio, descuentos = 100, None
    # Act
    resultado = descuento_cumulativo(precio, descuentos)
    # Assert
    assert resultado == 100


def test_descuento_cumulativo_orden_no_altera_el_resultado():
    # Arrange
    precio = 100
    # Act
    resultado_a = descuento_cumulativo(precio, [10, 20])
    resultado_b = descuento_cumulativo(precio, [20, 10])
    # Assert
    assert resultado_a == pytest.approx(resultado_b)


def test_descuento_cumulativo_dos_mitades_no_llegan_a_cero():
    # Arrange: 100 - 50 % = 50; 50 - 50 % = 25
    precio, descuentos = 100, [50, 50]
    # Act
    resultado = descuento_cumulativo(precio, descuentos)
    # Assert
    assert resultado == pytest.approx(25)


def test_descuento_cumulativo_con_cien_por_ciento_da_cero():
    # Arrange
    precio, descuentos = 100, [30, 100]
    # Act
    resultado = descuento_cumulativo(precio, descuentos)
    # Assert
    assert resultado == 0


def test_descuento_cumulativo_precio_negativo_lanza_error():
    # Arrange
    precio, descuentos = -100, [10]
    # Act + Assert
    with pytest.raises(ValueError, match="precio no puede ser negativo"):
        descuento_cumulativo(precio, descuentos)


@pytest.mark.parametrize("descuentos", [[10, 120], [-5], [10, -0.5]])
def test_descuento_cumulativo_descuento_fuera_de_rango_lanza_error(descuentos):
    # Arrange
    precio = 100
    # Act + Assert
    with pytest.raises(ValueError, match="Cada descuento debe estar entre 0 y 100"):
        descuento_cumulativo(precio, descuentos)


def test_descuento_cumulativo_texto_en_la_lista_lanza_type_error():
    # Arrange
    precio, descuentos = 100, [10, "20"]
    # Act + Assert
    with pytest.raises(TypeError):
        descuento_cumulativo(precio, descuentos)


# ---------- descuento_apilado ----------
def test_descuento_apilado_suma_los_porcentajes():
    # Arrange: 10 % + 20 % = 30 % sobre 100
    precio, descuentos = 100, [10, 20]
    # Act
    resultado = descuento_apilado(precio, descuentos)
    # Assert
    assert resultado == pytest.approx(70)


def test_descuento_apilado_un_solo_descuento():
    # Arrange
    precio, descuentos = 100, [25]
    # Act
    resultado = descuento_apilado(precio, descuentos)
    # Assert
    assert resultado == pytest.approx(75)


def test_descuento_apilado_lista_vacia_devuelve_precio():
    # Arrange
    precio, descuentos = 100, []
    # Act
    resultado = descuento_apilado(precio, descuentos)
    # Assert
    assert resultado == 100


def test_descuento_apilado_none_devuelve_precio():
    # Arrange
    precio, descuentos = 100, None
    # Act
    resultado = descuento_apilado(precio, descuentos)
    # Assert
    assert resultado == 100


def test_descuento_apilado_suma_exacta_de_cien_da_cero():
    # Arrange
    precio, descuentos = 100, [60, 40]
    # Act
    resultado = descuento_apilado(precio, descuentos)
    # Assert
    assert resultado == 0


def test_descuento_apilado_descuenta_mas_que_cumulativo():
    # Arrange
    precio, descuentos = 100, [10, 20]
    # Act
    apilado = descuento_apilado(precio, descuentos)
    cumulativo = descuento_cumulativo(precio, descuentos)
    # Assert  (70 apilado contra 72 cumulativo)
    assert apilado < cumulativo


def test_descuento_apilado_suma_mayor_a_cien_queda_en_cero():
    # Arrange: 60 % + 50 % = 110 %; el descuento total se limita al 100 %
    precio, descuentos = 100, [60, 50]
    # Act
    resultado = descuento_apilado(precio, descuentos)
    # Assert
    assert resultado == 0


def test_descuento_apilado_precio_negativo_lanza_error():
    # Arrange
    precio, descuentos = -100, [10]
    # Act + Assert
    with pytest.raises(ValueError, match="precio no puede ser negativo"):
        descuento_apilado(precio, descuentos)


@pytest.mark.parametrize("descuentos", [[150, -60], [-10, 30]])
def test_descuento_apilado_descuento_individual_fuera_de_rango_lanza_error(descuentos):
    # Arrange: la suma queda entre 0 y 100, pero cada descuento por sí solo es inválido
    precio = 100
    # Act + Assert
    with pytest.raises(ValueError):
        descuento_apilado(precio, descuentos)


def test_descuento_apilado_texto_en_la_lista_lanza_type_error():
    # Arrange
    precio, descuentos = 100, [10, "20"]
    # Act + Assert
    with pytest.raises(TypeError):
        descuento_apilado(precio, descuentos)
