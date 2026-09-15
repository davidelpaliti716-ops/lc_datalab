"""DataLab - Semana 1
Primera implementación del proyecto integrador.
"""

def main():
    print("=== DataLab | Semana 1 ===")
    print("Primera versión del procesamiento de un registro.")

    registro_id = input("Ingrese el identificador del registro: ")
    valor = float(input("Ingrese el valor del registro: "))

    # Regla inicial de ejemplo:
    # un valor >= 50 se considera "alto"; de lo contrario, "normal".
    # Esta regla deberá corresponder al algoritmo diseñado por el estudiante.
    if valor >= 50:
        clasificacion = "ALTO"
    else:
        clasificacion = "NORMAL"

    print("\nResultado")
    print(f"Registro: {registro_id}")
    print(f"Valor: {valor}")
    print(f"Clasificación: {clasificacion}")
    
    print("DataLab | Semana 2")
    print("Procesamientos de registros con multiples condiciones.")
    
    registro_id = input("Ingrese el indentificador del registro:")
    valor = float(input("ingrese el valor del registro: "))
    # Regla de negocio amnpliada usando if, elif y else:
    if valor <10:
        clasificacion= "BAJO"
    elif valor ==10:
        clasificacion = "LIMITE"
    elif 10 < valor <= 50:
        clasificacion = "NORMAL"
    else:
        clasificacion="ALTO"
        
    print ("---Resultado---")
    print(f"Registro:{registro_id}")
    print(f"Valor: {valor}")
    print(f"Clasificacion: {clasificacion}")


if __name__ == "__main__":
    main()
