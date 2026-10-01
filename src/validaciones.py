"""
validaciones_basicas.py

Material de apoyo - Lógica Computacional
Semana 04 - Ciclos for y range()

Propósito
---------
Este archivo contiene validaciones básicas que pueden reutilizarse
cuando se procesan diferentes datasets.

La idea es que los estudiantes:
1. Entiendan la lógica de cada validación.
2. Reutilicen las funciones en lugar de copiar código.
3. Amplíen las funciones cuando aparezcan nuevas necesidades.
4. Combinen estas funciones con ciclos for para procesar múltiples registros.

IMPORTANTE
----------
No se utilizan librerías externas. Solamente:
- if / elif / else
- match / case
- funciones
- expresiones regulares mediante el módulo estándar re
- operaciones básicas de cadenas y números
"""

import re


# ============================================================
# 1. VALIDACIONES BÁSICAS DE TEXTO
# ============================================================

def validar_cadena_no_vacia(texto):
    """
    Verifica que una cadena tenga contenido.

    strip() elimina espacios al inicio y al final.
    """
    if texto is None:
        return False

    return texto.strip() != ""


def validar_longitud(texto, minimo, maximo):
    """
    Verifica que la longitud de una cadena esté dentro de un rango.

    Ejemplo:
        validar_longitud("Python", 3, 10) -> True
    """
    if texto is None:
        return False

    longitud = len(texto.strip())

    return minimo <= longitud <= maximo


# ============================================================
# 2. EXPRESIONES REGULARES
# ============================================================

"""
¿Qué es una expresión regular?

Una expresión regular, o REGEX, es una forma de describir un patrón
que debe cumplir un texto.

Ejemplos sencillos:

    ^texto$
    ^[0-9]+$
    ^[A-Za-z]+$

Algunos símbolos importantes:

    ^       Inicio del texto
    $       Final del texto
    []      Conjunto de caracteres permitidos
    +       Uno o más caracteres
    ?       Cero o un carácter
    \\d      Un dígito
    \\s      Un espacio
    \\w      Letra, número o "_"
    .       Cualquier carácter (en muchos patrones)

En este material utilizamos expresiones regulares sencillas.
El objetivo es comprender el concepto, no memorizar patrones complejos.
"""


# ============================================================
# 3. CORREO ELECTRÓNICO
# ============================================================

def validar_correo(correo):
    """
    Validación básica de correo electrónico.

    Ejemplos válidos:
        usuario@gmail.com
        nombre.apellido@universidad.edu.co

    Ejemplos inválidos:
        usuario
        usuario@
        @gmail.com
        usuario@gmail
    """

    if not validar_cadena_no_vacia(correo):
        return False

    patron = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    return re.match(patron, correo.strip()) is not None


# ============================================================
# 4. NOMBRES DE PERSONAS
# ============================================================

def validar_nombre(nombre):
    """
    Verifica que un nombre contenga solamente letras y espacios.

    Se incluyen letras con tildes y Ñ propias del español.

    Ejemplos válidos:
        Ana
        Juan Pérez
        María José
        José Rodríguez

    Ejemplos inválidos:
        Juan123
        Ana_123
        4567
    """

    if not validar_cadena_no_vacia(nombre):
        return False

    patron = (
        r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü]+"
        r"( [A-Za-zÁÉÍÓÚáéíóúÑñÜü]+)*$"
    )

    return re.match(patron, nombre.strip()) is not None
