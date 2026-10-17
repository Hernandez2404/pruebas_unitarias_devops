import pytest
from src.manipulador_texto import (
    invertir_cadena,
    contar_vocales,
    contar_consonantes,
    es_palindromo,
    eliminar_duplicados,
    capitalizar_palabras,
    convertir_a_titulo,
    reemplazar_subcadena,
    dividir_en_palabras,
    extraer_dominio,
    enmascarar_email,
    normalizar_espacios,
    truncar,
    es_anagrama,
)


# ---------- invertir_cadena ----------
def test_invertir_cadena_palabra():
    # Arrange
    cadena = "hola"
    # Act
    resultado = invertir_cadena(cadena)
    # Assert
    assert resultado == "aloh"


def test_invertir_cadena_con_espacios():
    # Arrange
    cadena = "ab cd"
    # Act
    resultado = invertir_cadena(cadena)
    # Assert
    assert resultado == "dc ba"


def test_invertir_cadena_un_caracter():
    # Arrange
    cadena = "a"
    # Act
    resultado = invertir_cadena(cadena)
    # Assert
    assert resultado == "a"


def test_invertir_cadena_vacia_da_vacia():
    # Arrange
    cadena = ""
    # Act
    resultado = invertir_cadena(cadena)
    # Assert
    assert resultado == ""


def test_invertir_cadena_none_da_vacia():
    # Arrange
    cadena = None
    # Act
    resultado = invertir_cadena(cadena)
    # Assert
    assert resultado == ""


def test_invertir_cadena_numero_lanza_type_error():
    # Arrange
    cadena = 123
    # Act + Assert
    with pytest.raises(TypeError):
        invertir_cadena(cadena)


# ---------- contar_vocales ----------
def test_contar_vocales_palabra_con_todas_las_vocales():
    # Arrange
    cadena = "Murcielago"
    # Act
    resultado = contar_vocales(cadena)
    # Assert
    assert resultado == 5


def test_contar_vocales_cuenta_mayusculas():
    # Arrange
    cadena = "AEIOU"
    # Act
    resultado = contar_vocales(cadena)
    # Assert
    assert resultado == 5


def test_contar_vocales_sin_vocales_da_cero():
    # Arrange
    cadena = "xyz"
    # Act
    resultado = contar_vocales(cadena)
    # Assert
    assert resultado == 0


def test_contar_vocales_vacia_da_cero():
    # Arrange
    cadena = ""
    # Act
    resultado = contar_vocales(cadena)
    # Assert
    assert resultado == 0


def test_contar_vocales_none_da_cero():
    # Arrange
    cadena = None
    # Act
    resultado = contar_vocales(cadena)
    # Assert
    assert resultado == 0


def test_contar_vocales_numero_lanza_type_error():
    # Arrange
    cadena = 123
    # Act + Assert
    with pytest.raises(TypeError):
        contar_vocales(cadena)


# ---------- contar_consonantes ----------
def test_contar_consonantes_frase():
    # Arrange
    cadena = "Hola mundo"
    # Act
    resultado = contar_consonantes(cadena)
    # Assert
    assert resultado == 5


def test_contar_consonantes_ignora_numeros_y_signos():
    # Arrange
    cadena = "abc 123 !?"
    # Act
    resultado = contar_consonantes(cadena)
    # Assert
    assert resultado == 2


def test_contar_consonantes_solo_vocales_da_cero():
    # Arrange
    cadena = "aeiou"
    # Act
    resultado = contar_consonantes(cadena)
    # Assert
    assert resultado == 0


def test_contar_consonantes_vacia_da_cero():
    # Arrange
    cadena = ""
    # Act
    resultado = contar_consonantes(cadena)
    # Assert
    assert resultado == 0


# ---------- es_palindromo ----------
def test_es_palindromo_palabra_simple():
    # Arrange
    cadena = "reconocer"
    # Act
    resultado = es_palindromo(cadena)
    # Assert
    assert resultado is True


def test_es_palindromo_palabra_que_no_lo_es():
    # Arrange
    cadena = "hola"
    # Act
    resultado = es_palindromo(cadena)
    # Assert
    assert resultado is False


def test_es_palindromo_un_caracter():
    # Arrange
    cadena = "a"
    # Act
    resultado = es_palindromo(cadena)
    # Assert
    assert resultado is True


def test_es_palindromo_vacia_da_false():
    # Arrange
    cadena = ""
    # Act
    resultado = es_palindromo(cadena)
    # Assert
    assert resultado is False


def test_es_palindromo_ignora_mayusculas():
    # Arrange
    cadena = "Oso"
    # Act
    resultado = es_palindromo(cadena)
    # Assert
    assert resultado is True


def test_es_palindromo_frase_ignora_espacios_y_mayusculas():
    # Arrange
    cadena = "Anita lava la tina"
    # Act
    resultado = es_palindromo(cadena)
    # Assert
    assert resultado is True


def test_es_palindromo_frase_que_no_lo_es():
    # Arrange
    cadena = "hola mundo"
    # Act
    resultado = es_palindromo(cadena)
    # Assert
    assert resultado is False


# ---------- eliminar_duplicados ----------
def test_eliminar_duplicados_conserva_el_orden():
    # Arrange
    cadena = "programacion"
    # Act
    resultado = eliminar_duplicados(cadena)
    # Assert
    assert resultado == "progamcin"


def test_eliminar_duplicados_sin_repetidos_no_cambia():
    # Arrange
    cadena = "abc"
    # Act
    resultado = eliminar_duplicados(cadena)
    # Assert
    assert resultado == "abc"


def test_eliminar_duplicados_todos_iguales():
    # Arrange
    cadena = "aaaa"
    # Act
    resultado = eliminar_duplicados(cadena)
    # Assert
    assert resultado == "a"


def test_eliminar_duplicados_distingue_mayusculas():
    # Arrange
    cadena = "Aa"
    # Act
    resultado = eliminar_duplicados(cadena)
    # Assert
    assert resultado == "Aa"


def test_eliminar_duplicados_vacia_da_vacia():
    # Arrange
    cadena = ""
    # Act
    resultado = eliminar_duplicados(cadena)
    # Assert
    assert resultado == ""


# ---------- capitalizar_palabras ----------
def test_capitalizar_palabras_frase():
    # Arrange
    cadena = "hola mundo"
    # Act
    resultado = capitalizar_palabras(cadena)
    # Assert
    assert resultado == "Hola Mundo"


def test_capitalizar_palabras_normaliza_espacios():
    # Arrange
    cadena = "hola   mundo"
    # Act
    resultado = capitalizar_palabras(cadena)
    # Assert
    assert resultado == "Hola Mundo"


def test_capitalizar_palabras_resto_en_minuscula():
    # Arrange
    cadena = "hOLA mUNDO"
    # Act
    resultado = capitalizar_palabras(cadena)
    # Assert
    assert resultado == "Hola Mundo"


def test_capitalizar_palabras_vacia_da_vacia():
    # Arrange
    cadena = ""
    # Act
    resultado = capitalizar_palabras(cadena)
    # Assert
    assert resultado == ""


def test_capitalizar_palabras_numero_lanza_attribute_error():
    # Arrange
    cadena = 123
    # Act + Assert
    with pytest.raises(AttributeError):
        capitalizar_palabras(cadena)


# ---------- convertir_a_titulo ----------
def test_convertir_a_titulo_frase_con_enie():
    # Arrange
    cadena = "el señor de los anillos"
    # Act
    resultado = convertir_a_titulo(cadena)
    # Assert
    assert resultado == "El Señor De Los Anillos"


def test_convertir_a_titulo_conserva_espacios():
    # Arrange
    cadena = "hola  mundo"
    # Act
    resultado = convertir_a_titulo(cadena)
    # Assert
    assert resultado == "Hola  Mundo"


def test_convertir_a_titulo_vacia_da_vacia():
    # Arrange
    cadena = ""
    # Act
    resultado = convertir_a_titulo(cadena)
    # Assert
    assert resultado == ""


# ---------- reemplazar_subcadena ----------
def test_reemplazar_subcadena_todas_las_apariciones():
    # Arrange
    cadena, vieja, nueva = "a-b-c", "-", "+"
    # Act
    resultado = reemplazar_subcadena(cadena, vieja, nueva)
    # Assert
    assert resultado == "a+b+c"


def test_reemplazar_subcadena_con_maximo_de_reemplazos():
    # Arrange
    cadena, vieja, nueva = "a-b-c", "-", "+"
    # Act
    resultado = reemplazar_subcadena(cadena, vieja, nueva, max_reemplazos=1)
    # Assert
    assert resultado == "a+b-c"


def test_reemplazar_subcadena_maximo_cero_no_cambia():
    # Arrange
    cadena, vieja, nueva = "a-b-c", "-", "+"
    # Act
    resultado = reemplazar_subcadena(cadena, vieja, nueva, max_reemplazos=0)
    # Assert
    assert resultado == "a-b-c"


def test_reemplazar_subcadena_no_encontrada_no_cambia():
    # Arrange
    cadena, vieja, nueva = "hola", "x", "y"
    # Act
    resultado = reemplazar_subcadena(cadena, vieja, nueva)
    # Assert
    assert resultado == "hola"


def test_reemplazar_subcadena_vacia_da_vacia():
    # Arrange
    cadena, vieja, nueva = "", "a", "b"
    # Act
    resultado = reemplazar_subcadena(cadena, vieja, nueva)
    # Assert
    assert resultado == ""


# ---------- dividir_en_palabras ----------
def test_dividir_en_palabras_frase_simple():
    # Arrange
    cadena = "hola mundo cruel"
    # Act
    resultado = dividir_en_palabras(cadena)
    # Assert
    assert resultado == ["hola", "mundo", "cruel"]


def test_dividir_en_palabras_una_palabra():
    # Arrange
    cadena = "hola"
    # Act
    resultado = dividir_en_palabras(cadena)
    # Assert
    assert resultado == ["hola"]


def test_dividir_en_palabras_vacia_da_lista_vacia():
    # Arrange
    cadena = ""
    # Act
    resultado = dividir_en_palabras(cadena)
    # Assert
    assert resultado == []


def test_dividir_en_palabras_none_da_lista_vacia():
    # Arrange
    cadena = None
    # Act
    resultado = dividir_en_palabras(cadena)
    # Assert
    assert resultado == []


def test_dividir_en_palabras_multiples_espacios():
    # Arrange
    cadena = "hola   mundo"
    # Act
    resultado = dividir_en_palabras(cadena)
    # Assert
    assert resultado == ["hola", "mundo"]


def test_dividir_en_palabras_ignora_puntuacion():
    # Arrange
    cadena = "¡Hola, mundo!"
    # Act
    resultado = dividir_en_palabras(cadena)
    # Assert
    assert resultado == ["Hola", "mundo"]


def test_dividir_en_palabras_tabulaciones_y_saltos_de_linea():
    # Arrange
    cadena = "hola\tmundo\nadiós"
    # Act
    resultado = dividir_en_palabras(cadena)
    # Assert
    assert resultado == ["hola", "mundo", "adiós"]


def test_dividir_en_palabras_numero_lanza_attribute_error():
    # Arrange
    cadena = 123
    # Act + Assert
    with pytest.raises(AttributeError):
        dividir_en_palabras(cadena)


# ---------- extraer_dominio ----------
def test_extraer_dominio_email_valido():
    # Arrange
    email = "andres@unal.edu.co"
    # Act
    resultado = extraer_dominio(email)
    # Assert
    assert resultado == "unal.edu.co"


def test_extraer_dominio_sin_arroba_da_vacio():
    # Arrange
    email = "andres.unal.edu.co"
    # Act
    resultado = extraer_dominio(email)
    # Assert
    assert resultado == ""


def test_extraer_dominio_dos_arrobas_da_vacio():
    # Arrange
    email = "a@b@c.com"
    # Act
    resultado = extraer_dominio(email)
    # Assert
    assert resultado == ""


def test_extraer_dominio_vacio_da_vacio():
    # Arrange
    email = ""
    # Act
    resultado = extraer_dominio(email)
    # Assert
    assert resultado == ""


def test_extraer_dominio_none_da_vacio():
    # Arrange
    email = None
    # Act
    resultado = extraer_dominio(email)
    # Assert
    assert resultado == ""


# ---------- enmascarar_email ----------
def test_enmascarar_email_oculta_el_centro_del_usuario():
    # Arrange
    email = "andres@unal.edu.co"
    # Act
    resultado = enmascarar_email(email)
    # Assert
    assert resultado == "a****s@unal.edu.co"


def test_enmascarar_email_usuario_de_tres_letras():
    # Arrange
    email = "ana@x.co"
    # Act
    resultado = enmascarar_email(email)
    # Assert
    assert resultado == "a*a@x.co"


def test_enmascarar_email_usuario_de_dos_letras_no_cambia():
    # Arrange
    email = "ab@x.co"
    # Act
    resultado = enmascarar_email(email)
    # Assert
    assert resultado == "ab@x.co"


def test_enmascarar_email_sin_arroba_da_vacio():
    # Arrange
    email = "andres.unal.edu.co"
    # Act
    resultado = enmascarar_email(email)
    # Assert
    assert resultado == ""


def test_enmascarar_email_dos_arrobas_da_vacio():
    # Arrange
    email = "a@b@c.com"
    # Act
    resultado = enmascarar_email(email)
    # Assert
    assert resultado == ""


# ---------- normalizar_espacios ----------
def test_normalizar_espacios_quita_espacios_extra():
    # Arrange
    cadena = "  hola   mundo  "
    # Act
    resultado = normalizar_espacios(cadena)
    # Assert
    assert resultado == "hola mundo"


def test_normalizar_espacios_tabulaciones_y_saltos_de_linea():
    # Arrange
    cadena = "hola\t\tmundo\n"
    # Act
    resultado = normalizar_espacios(cadena)
    # Assert
    assert resultado == "hola mundo"


def test_normalizar_espacios_texto_ya_normalizado_no_cambia():
    # Arrange
    cadena = "hola mundo"
    # Act
    resultado = normalizar_espacios(cadena)
    # Assert
    assert resultado == "hola mundo"


def test_normalizar_espacios_solo_espacios_da_vacia():
    # Arrange
    cadena = "    "
    # Act
    resultado = normalizar_espacios(cadena)
    # Assert
    assert resultado == ""


def test_normalizar_espacios_vacia_da_vacia():
    # Arrange
    cadena = ""
    # Act
    resultado = normalizar_espacios(cadena)
    # Assert
    assert resultado == ""


# ---------- truncar ----------
def test_truncar_cadena_larga_agrega_sufijo():
    # Arrange
    cadena, longitud = "Hola mundo cruel", 10
    # Act
    resultado = truncar(cadena, longitud)
    # Assert
    assert resultado == "Hola mu..."


def test_truncar_resultado_no_supera_la_longitud():
    # Arrange
    cadena, longitud = "Texto bastante largo", 8
    # Act
    resultado = truncar(cadena, longitud)
    # Assert
    assert len(resultado) == longitud


def test_truncar_longitud_exacta_no_cambia():
    # Arrange
    cadena, longitud = "Hola", 4
    # Act
    resultado = truncar(cadena, longitud)
    # Assert
    assert resultado == "Hola"


def test_truncar_cadena_corta_no_cambia():
    # Arrange
    cadena, longitud = "Hola", 10
    # Act
    resultado = truncar(cadena, longitud)
    # Assert
    assert resultado == "Hola"


def test_truncar_sufijo_personalizado():
    # Arrange
    cadena, longitud, sufijo = "Hola mundo", 5, "~"
    # Act
    resultado = truncar(cadena, longitud, sufijo)
    # Assert
    assert resultado == "Hola~"


def test_truncar_vacia_da_vacia():
    # Arrange
    cadena, longitud = "", 5
    # Act
    resultado = truncar(cadena, longitud)
    # Assert
    assert resultado == ""


# ---------- es_anagrama ----------
def test_es_anagrama_palabras_anagramas():
    # Arrange
    cadena1, cadena2 = "roma", "amor"
    # Act
    resultado = es_anagrama(cadena1, cadena2)
    # Assert
    assert resultado is True


def test_es_anagrama_ignora_mayusculas():
    # Arrange
    cadena1, cadena2 = "Roma", "Amor"
    # Act
    resultado = es_anagrama(cadena1, cadena2)
    # Assert
    assert resultado is True


def test_es_anagrama_ignora_espacios():
    # Arrange
    cadena1, cadena2 = "la roma", "mora la"
    # Act
    resultado = es_anagrama(cadena1, cadena2)
    # Assert
    assert resultado is True


def test_es_anagrama_palabras_distintas():
    # Arrange
    cadena1, cadena2 = "hola", "chao"
    # Act
    resultado = es_anagrama(cadena1, cadena2)
    # Assert
    assert resultado is False


def test_es_anagrama_distinta_longitud():
    # Arrange
    cadena1, cadena2 = "rana", "ranas"
    # Act
    resultado = es_anagrama(cadena1, cadena2)
    # Assert
    assert resultado is False


def test_es_anagrama_cadena_vacia_da_false():
    # Arrange
    cadena1, cadena2 = "", "amor"
    # Act
    resultado = es_anagrama(cadena1, cadena2)
    # Assert
    assert resultado is False
