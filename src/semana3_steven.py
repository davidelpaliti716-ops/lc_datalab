''' 
validacion 1 
La validacion pregunta la edad, si es menor de edad (1-17) tiene el acceso restringido y si es mayor de edad(+18) ya tiene el acceso 
'''

try:
  edad = int(input("Por favor, ingresa tu edad: "))

  if 1 <= edad <= 17:
    print("Menor de edad. Acceso restringido ")
  elif edad >= 18:
    print("Mayor de edad. Acceso permitido ")
  else:
    print("Por favor, ingresa una edad mayor a 0.")

except ValueError:
  print("Error: Por favor ingresa un número válido.")

'''
validacion 2 
Esta validacion se encarga de registrar el genero de alguna persona, ya sea masculino, femenino u otro
'''
# Programa para registrar el género

print("--- Registro de Género ---")
print("Opciones: Masculino, Femenino, Otro")

# .strip() quita espacios extra y .lower() pasa todo a minúsculas
genero = input("Por favor, ingresa tu género: ").strip().lower()

if genero in ["masculino", "m"]:
  print("Género registrado: Masculino ")
elif genero in ["femenino", "f"]:
  print("Género registrado: Femenino ")
elif genero in ["otro", "o"]:
  print("Género registrado: Otro ")
else:
  print("⚠️ Lo siento, no reconozco esa opción. Intenta escribir 'Masculino', 'Femenino' u 'Otro'.")