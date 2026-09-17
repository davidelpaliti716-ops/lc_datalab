'''
validacion 1
Esta validacion se encarga de decirte si los numeros que digites son validos (que comiencen por 3 y que tengan 10 digitos)
'''

import re

def validar_telefono(numero):
    # Convierte a string por si se pasa un entero
    patron = r"^3\d{9}$"
    if re.match(patron, str(numero)):
        return True
    return False

# Ejemplos de prueba
telefonos = ["3001234567", "3123456789", "2001234567", "300123456", "30012345678", "300ABC4567"]

for tel in telefonos:
    es_valido = validar_telefono(tel)
    print(f"Teléfono: {tel} -> {'Válido' if es_valido else 'Inválido'}")


'''
validacion 2
En esta validacion solo se permite subir archivos de pdf, jpg, png, jpeg
'''
def es_archivo_permitido(nombre_archivo):
    # Extensiones que vamos a aceptar
    extensiones_permitidas = ('.pdf', '.jpg', '.png', '.jpeg')
    
    # Convertimos a minúsculas por si viene como .PDF o .JPG
    archivo_min = nombre_archivo.lower()
    
    # Verificamos si termina en alguna de las extensiones
    return archivo_min.endswith(extensiones_permitidas)

# Ejemplos de prueba
print(es_archivo_permitido("documento.pdf"))   # True
print(es_archivo_permitido("FOTO.JPG"))        # True
print(es_archivo_permitido("script.exe"))      # False
print(es_archivo_permitido("archivo.txt"))      # False

 
