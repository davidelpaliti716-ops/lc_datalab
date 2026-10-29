# Taller de Ejercicios: Lógica de Repetición en DataLab



def contar_edades_validas():
    contador = 0
    print(
        "--- Sistema de Conteo de Edades ---"
        "\nIngresa las edades una por una. (Un número negativo detiene el proceso)."
    )

    while True:
        try:
            edad = int(input("Ingresa una edad: "))

            # Condición de parada (número negativo)
            if edad < 0:
                print("\nNúmero negativo detectado. Finalizando captura...")
                break

            # Incrementamos el contador por cada registro válido
            contador += 1

        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

    print(f"Total de edades válidas ingresadas: {contador}")
    return contador


## 🧩 Reto 2: El Procesador de Lotes (Uso de `for`)
def procesar_sensores():
    print("--- Procesamiento de Lote de Sensores ---")
    
    # range(1, 11) genera números del 1 al 10
    for i in range(1, 11):
        print(f"Sensor {i}: Temperatura procesada")
        
    print("Lote completo")

## 🧩 Reto 3: Validador de Contraseña de Acceso (Simulación `do-while`)
def validar_acceso():
    clave_correcta = "Data2026"
    print("--- Sistema de Seguridad DataLab ---")
    
    while True:
        password = input("Ingrese la contraseña de acceso: ")
        
        if password == clave_correcta:
            print("¡Acceso concedido! Bienvenido a funciones avanzadas.")
            break
        else:
            print("Acceso denegado, intente de nuevo\n")

## 🧩 Reto 4: El Filtro de Datos (Combinación `for` + `if`)
def filtrar_datos():
    valores = [10, 55, 2, 80, 15, 100, 40]
    print("--- Filtro de Valores del Sensor ---")
    
    for valor in valores:
        if valor > 50:
            print(f"Valor válido conservado: {valor}")
        else:
            print("Valor descartado")

