'''
validacion 1 
Esta funcion lo que hace es indentificar si un correo es valido o no 
'''

import re

def validar_correo_seguro():
    email = input("Introduce tu correo electrónico: ")
    patron_correo = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    
    if not re.fullmatch(patron_correo, email):
        print(" Correo inválido: El formato no coincide.")
    elif len(email) > 100:
        print(" Correo inválido: Demasiado largo.")
    else:
        print(" ¡Correo válido!")

# Ejecutar la función
validar_correo_seguro()
'''
validacion 2
Esta funcion lo que hace es identificar si dentro del nombre usuario tiene sea invalido 
'''
import re

def validar_nombre():
    # input() te permite escribir el nombre por teclado en la terminal
    nombre = input("Introduce un nombre: ")
    
    # re.search busca si hay algún número (\d) en cualquier parte del texto
    tiene_numero = re.search(r'\d', nombre)
    
    # Usamos match para evaluar el resultado
    match tiene_numero:
        case None:
            print(" ¡Nombre válido! No contiene números.")
        case _:
            print("Nombre inválido: No se permiten números.")

# Ejecutar la función interactiva
validar_nombre()
'''
validacion 3
'''
def validar_numero_positivo():
    try:
        # Pedimos el número por teclado
        entrada = input("Introduce un número: ")
        
        # Convertimos la entrada a un número decimal (float) 
        # para que acepte tanto enteros como decimales
        numero = float(entrada)
        
        # Usamos match para evaluar el valor del número
        match numero:
            case x if x < 0:
                print(" Número inválido: ¡No se permiten números negativos!")
            case _:
                print("¡Número válido! Es un número positivo o cero.")
                
    except ValueError:
        print(" Error: Debes ingresar un número válido (no letras).")

# Ejecutar la función interactiva
validar_numero_positivo()