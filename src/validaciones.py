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
