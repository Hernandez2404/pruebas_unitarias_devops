import pytest
from unittest.mock import patch, mock_open, call
from src.csv_parser import (
    parse_csv_line,
    leer_csv_como_lista,
    csv_a_diccionarios,
    validar_csv,
    extraer_columna,
    filtrar_por_columna,
    contar_filas,
    contar_columnas,
)


# ---------- parse_csv_line ----------
def test_parse_csv_line_linea_normal():
    # Arrange
    linea = "a,b,c"
    # Act
    resultado = parse_csv_line(linea)
    # Assert
    assert resultado == ["a", "b", "c"]


def test_parse_csv_line_vacia_da_lista_vacia():
    # Arrange
    linea = ""
    # Act
    resultado = parse_csv_line(linea)
    # Assert
    assert resultado == []


def test_parse_csv_line_none_da_lista_vacia():
    # Arrange
    linea = None
    # Act
    resultado = parse_csv_line(linea)
    # Assert
    assert resultado == []


def test_parse_csv_line_un_solo_campo():
    # Arrange
    linea = "solo"
    # Act
    resultado = parse_csv_line(linea)
    # Assert
    assert resultado == ["solo"]


def test_parse_csv_line_conserva_campos_vacios():
    # Arrange
    linea = "a,,c"
    # Act
    resultado = parse_csv_line(linea)
    # Assert
    assert resultado == ["a", "", "c"]


def test_parse_csv_line_coma_final_crea_campo_vacio():
    # Arrange
    linea = "a,b,"
    # Act
    resultado = parse_csv_line(linea)
    # Assert
    assert resultado == ["a", "b", ""]


def test_parse_csv_line_comillas_protegen_la_coma_interna():
    # Arrange: la coma dentro de las comillas es parte del valor, no un separador
    linea = 'Ana,"Bogotá, Colombia",30'
    # Act
    resultado = parse_csv_line(linea)
    # Assert
    assert resultado == ["Ana", "Bogotá, Colombia", "30"]


def test_parse_csv_line_comillas_escapadas():
    # Arrange: en CSV una comilla dentro de un campo entre comillas se escribe doble ("")
    linea = 'id,"dijo ""hola""",ok'
    # Act
    resultado = parse_csv_line(linea)
    # Assert
    assert resultado == ["id", 'dijo "hola"', "ok"]


def test_parse_csv_line_numero_lanza_type_error():
    # Arrange
    linea = 123
    # Act + Assert
    with pytest.raises(TypeError):
        parse_csv_line(linea)


# ---------- leer_csv_como_lista ----------
def test_leer_csv_como_lista_contenido_normal():
    # Arrange
    contenido = "a,b\nc,d"
    # Act
    resultado = leer_csv_como_lista(contenido)
    # Assert
    assert resultado == [["a", "b"], ["c", "d"]]


def test_leer_csv_como_lista_una_sola_linea():
    # Arrange
    contenido = "x,y"
    # Act
    resultado = leer_csv_como_lista(contenido)
    # Assert
    assert resultado == [["x", "y"]]


def test_leer_csv_como_lista_ignora_salto_de_linea_final():
    # Arrange
    contenido = "a,b\nc,d\n"
    # Act
    resultado = leer_csv_como_lista(contenido)
    # Assert
    assert resultado == [["a", "b"], ["c", "d"]]


def test_leer_csv_como_lista_vacio_da_lista_vacia():
    # Arrange
    contenido = ""
    # Act
    resultado = leer_csv_como_lista(contenido)
    # Assert
    assert resultado == []


def test_leer_csv_como_lista_none_da_lista_vacia():
    # Arrange
    contenido = None
    # Act
    resultado = leer_csv_como_lista(contenido)
    # Assert
    assert resultado == []


def test_leer_csv_como_lista_numero_lanza_attribute_error():
    # Arrange
    contenido = 123
    # Act + Assert
    with pytest.raises(AttributeError):
        leer_csv_como_lista(contenido)


# ---------- csv_a_diccionarios ----------
def test_csv_a_diccionarios_con_cabecera():
    # Arrange
    contenido = "nombre,edad\nAna,30\nLuis,25"
    # Act
    resultado = csv_a_diccionarios(contenido)
    # Assert
    assert resultado == [
        {"nombre": "Ana", "edad": "30"},
        {"nombre": "Luis", "edad": "25"},
    ]


def test_csv_a_diccionarios_solo_cabecera_da_lista_vacia():
    # Arrange
    contenido = "nombre,edad"
    # Act
    resultado = csv_a_diccionarios(contenido)
    # Assert
    assert resultado == []


def test_csv_a_diccionarios_vacio_da_lista_vacia():
    # Arrange
    contenido = ""
    # Act
    resultado = csv_a_diccionarios(contenido)
    # Assert
    assert resultado == []


def test_csv_a_diccionarios_fila_incompleta_completa_con_vacio():
    # Arrange: a la fila de Luis le falta la edad; cada diccionario debe tener todas las cabeceras
    contenido = "nombre,edad\nAna,30\nLuis"
    # Act
    resultado = csv_a_diccionarios(contenido)
    # Assert
    assert resultado == [
        {"nombre": "Ana", "edad": "30"},
        {"nombre": "Luis", "edad": ""},
    ]


def test_csv_a_diccionarios_valores_conservan_tipo_texto():
    # Arrange
    contenido = "producto,precio\nlapiz,1500"
    # Act
    resultado = csv_a_diccionarios(contenido)
    # Assert
    assert resultado[0]["precio"] == "1500"


# ---------- validar_csv ----------
def test_validar_csv_mismo_numero_de_columnas_es_valido():
    # Arrange
    contenido = "a,b\nc,d"
    # Act
    resultado = validar_csv(contenido)
    # Assert
    assert resultado is True


def test_validar_csv_una_sola_linea_es_valido():
    # Arrange
    contenido = "a,b,c"
    # Act
    resultado = validar_csv(contenido)
    # Assert
    assert resultado is True


def test_validar_csv_distinto_numero_de_columnas_es_invalido():
    # Arrange
    contenido = "a,b\nc"
    # Act
    resultado = validar_csv(contenido)
    # Assert
    assert resultado is False


def test_validar_csv_vacio_es_invalido():
    # Arrange
    contenido = ""
    # Act
    resultado = validar_csv(contenido)
    # Assert
    assert resultado is False


def test_validar_csv_none_es_invalido():
    # Arrange
    contenido = None
    # Act
    resultado = validar_csv(contenido)
    # Assert
    assert resultado is False


# ---------- extraer_columna ----------
def test_extraer_columna_caso_normal():
    # Arrange
    contenido, indice = "a,b\nc,d", 1
    # Act
    resultado = extraer_columna(contenido, indice)
    # Assert
    assert resultado == ["b", "d"]


def test_extraer_columna_fila_corta_devuelve_vacio():
    # Arrange
    contenido, indice = "a,b\nc", 1
    # Act
    resultado = extraer_columna(contenido, indice)
    # Assert
    assert resultado == ["b", ""]


def test_extraer_columna_indice_fuera_de_rango_devuelve_vacios():
    # Arrange
    contenido, indice = "a,b\nc,d", 5
    # Act
    resultado = extraer_columna(contenido, indice)
    # Assert
    assert resultado == ["", ""]


def test_extraer_columna_contenido_vacio_da_lista_vacia():
    # Arrange
    contenido, indice = "", 0
    # Act
    resultado = extraer_columna(contenido, indice)
    # Assert
    assert resultado == []


# ---------- filtrar_por_columna ----------
def test_filtrar_por_columna_devuelve_filas_que_coinciden():
    # Arrange
    contenido = "Ana,Manizales\nLuis,Bogota\nEva,Manizales"
    # Act
    resultado = filtrar_por_columna(contenido, 1, "Manizales")
    # Assert
    assert resultado == [["Ana", "Manizales"], ["Eva", "Manizales"]]


def test_filtrar_por_columna_sin_coincidencias_da_lista_vacia():
    # Arrange
    contenido = "Ana,Manizales\nLuis,Bogota"
    # Act
    resultado = filtrar_por_columna(contenido, 1, "Cali")
    # Assert
    assert resultado == []


def test_filtrar_por_columna_distingue_mayusculas():
    # Arrange
    contenido = "Ana,Manizales"
    # Act
    resultado = filtrar_por_columna(contenido, 1, "manizales")
    # Assert
    assert resultado == []


def test_filtrar_por_columna_ignora_filas_cortas():
    # Arrange
    contenido = "Ana,Manizales\nLuis"
    # Act
    resultado = filtrar_por_columna(contenido, 1, "Manizales")
    # Assert
    assert resultado == [["Ana", "Manizales"]]


def test_filtrar_por_columna_contenido_vacio_da_lista_vacia():
    # Arrange
    contenido = ""
    # Act
    resultado = filtrar_por_columna(contenido, 0, "x")
    # Assert
    assert resultado == []


# ---------- contar_filas ----------
def test_contar_filas_caso_normal():
    # Arrange
    contenido = "a\nb\nc"
    # Act
    resultado = contar_filas(contenido)
    # Assert
    assert resultado == 3


def test_contar_filas_no_cuenta_salto_de_linea_final():
    # Arrange
    contenido = "a\nb\n"
    # Act
    resultado = contar_filas(contenido)
    # Assert
    assert resultado == 2


def test_contar_filas_vacio_da_cero():
    # Arrange
    contenido = ""
    # Act
    resultado = contar_filas(contenido)
    # Assert
    assert resultado == 0


def test_contar_filas_none_da_cero():
    # Arrange
    contenido = None
    # Act
    resultado = contar_filas(contenido)
    # Assert
    assert resultado == 0


# ---------- contar_columnas ----------
def test_contar_columnas_caso_normal():
    # Arrange
    contenido = "a,b,c\nd,e,f"
    # Act
    resultado = contar_columnas(contenido)
    # Assert
    assert resultado == 3


def test_contar_columnas_una_sola_columna():
    # Arrange
    contenido = "a\nb"
    # Act
    resultado = contar_columnas(contenido)
    # Assert
    assert resultado == 1


def test_contar_columnas_vacio_da_cero():
    # Arrange
    contenido = ""
    # Act
    resultado = contar_columnas(contenido)
    # Assert
    assert resultado == 0


# ---------- mocking: archivo simulado con mock_open ----------
# open() se reemplaza por un mock: el contenido "se lee" desde memoria y nunca se toca el disco.
def test_csv_a_diccionarios_desde_archivo_simulado():
    # Arrange
    contenido = "nombre,edad\nAna,30\nLuis,25\n"
    with patch("builtins.open", mock_open(read_data=contenido)):
        # Act
        with open("clientes.csv", encoding="utf-8") as archivo:
            resultado = csv_a_diccionarios(archivo.read())
    # Assert
    assert resultado == [
        {"nombre": "Ana", "edad": "30"},
        {"nombre": "Luis", "edad": "25"},
    ]


def test_archivo_simulado_se_abre_con_la_ruta_pedida():
    # Arrange
    with patch("builtins.open", mock_open(read_data="a,b\nc,d")) as open_falso:
        # Act
        with open("datos/ventas.csv", encoding="utf-8") as archivo:
            contar_filas(archivo.read())
    # Assert
    open_falso.assert_called_once_with("datos/ventas.csv", encoding="utf-8")


def test_contar_filas_desde_archivo_simulado():
    # Arrange
    contenido = "id,producto\n1,lapiz\n2,cuaderno\n3,borrador\n"
    with patch("builtins.open", mock_open(read_data=contenido)):
        # Act
        with open("inventario.csv", encoding="utf-8") as archivo:
            resultado = contar_filas(archivo.read())
    # Assert
    assert resultado == 4


def test_archivo_simulado_vacio_da_lista_vacia():
    # Arrange
    with patch("builtins.open", mock_open(read_data="")):
        # Act
        with open("vacio.csv", encoding="utf-8") as archivo:
            resultado = leer_csv_como_lista(archivo.read())
    # Assert
    assert resultado == []


# ---------- mocking: aislar dependencias internas con patch ----------
# Se reemplaza una función del módulo para probar otra sin depender de ella.
def test_leer_csv_como_lista_llama_parse_csv_line_por_cada_linea():
    # Arrange
    contenido = "a,b\nc,d\ne,f"
    with patch("src.csv_parser.parse_csv_line", return_value=["x"]) as parse_falso:
        # Act
        leer_csv_como_lista(contenido)
    # Assert
    assert parse_falso.call_args_list == [call("a,b"), call("c,d"), call("e,f")]


def test_csv_a_diccionarios_usa_las_filas_de_leer_csv_como_lista():
    # Arrange: el parsing queda fuera; solo se prueba la construcción de diccionarios
    filas_simuladas = [["id", "producto"], ["1", "lapiz"]]
    with patch("src.csv_parser.leer_csv_como_lista", return_value=filas_simuladas) as leer_falso:
        # Act
        resultado = csv_a_diccionarios("contenido cualquiera")
    # Assert
    assert resultado == [{"id": "1", "producto": "lapiz"}]
    leer_falso.assert_called_once_with("contenido cualquiera")


def test_extraer_columna_con_filas_simuladas():
    # Arrange
    filas_simuladas = [["a", "b"], ["c"]]
    with patch("src.csv_parser.leer_csv_como_lista", return_value=filas_simuladas):
        # Act
        resultado = extraer_columna("contenido cualquiera", 1)
    # Assert
    assert resultado == ["b", ""]


def test_filtrar_por_columna_con_filas_simuladas():
    # Arrange
    filas_simuladas = [["Ana", "Manizales"], ["Luis", "Bogota"], ["Eva", "Manizales"]]
    with patch("src.csv_parser.leer_csv_como_lista", return_value=filas_simuladas):
        # Act
        resultado = filtrar_por_columna("contenido cualquiera", 1, "Bogota")
    # Assert
    assert resultado == [["Luis", "Bogota"]]


def test_contar_columnas_delega_en_parse_csv_line():
    # Arrange
    with patch("src.csv_parser.parse_csv_line", return_value=["a", "b", "c", "d"]) as parse_falso:
        # Act
        resultado = contar_columnas("primera linea\nsegunda linea")
    # Assert
    assert resultado == 4
    parse_falso.assert_called_once_with("primera linea")
