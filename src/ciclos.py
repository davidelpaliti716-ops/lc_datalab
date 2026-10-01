from validaciones import validar_nombre

for i in range(5):
    nombre = input(f"Ingrese el nombre {i + 1}: ")

    if validar_nombre(nombre):
        print("Nombre válido")
    else:
        print("Nombre inválido")

from validaciones import validar_correo

for i in range(5):
    correo = input(f"Ingrese el correo {i + 1}: ")

    if validar_correo(correo):
        print("Correo válido")
    else:
        print("Correo inválido")