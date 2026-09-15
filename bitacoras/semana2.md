# Semana 2

## ¿Que entrada recibe Datalab?

>Piensa en la entrada como la informacion que el usuario le entrega al guardia al llegar.
>>En el mundo real, el visitante le dice al guardia su edad o su estatura para poder entrar al parque de diversiones.

>>En nuestro programa de DataLab, la entrada es el dato crudo que el programa lee (por ejemplo, un numero que representa los puntos de un estudiante, la temperatura de un sensor o el precio de un producto)

## ¿Que condiciones debe evaluar?
>Una vez que el guardia tiene la infornmacion (la entrada), tiene que hacerle preguntas a ese dato para tomar desiciones. Aqui entra (if, elif, else)

>Siguiendo con el ejemplo, el guardia tiene un manual de reglas que dice:
>>Si la estatura es mayor a 1.40 metros, puede pasar a la montaña rusa principal.

>> Si mide entre 1.00 y 1.40 metros, puede pasar a los carruseles

>> Si no cumple ninguna de las anteriores, debe esperar en la zona infantil

>En programacion, las reglas traducen estas logicas humanas en preguntas claras que la computadora puede evaluar paso a paso
## ¿Que clasificacion o resultado debe producir?
>La salida es la accion final o el letrero que el guardia levanta despues de evaluar las reglas.
>>Para el visitante, la salida es recibir una manilla de un color especifico o de ir a un juego determinado
>>Para DataLab, la salida es el resultado impreso en la pantalla (Ejemplo: "Aprobado", "Riesgo alto, "Cliente VIP") o el dato procesado.


# Diseñar la  solucion        

>Inicio del Algoritmo DataLab
 >   Mostrar mensaje de bienvenida ("=== DataLab | Semana 2 ===")
  >  Leer e inicializar la variable "registro_id" (Texto)
   > Leer e inicializar la variable "valor" (Número decimal)

   > Si valor < 10 entonces:
       > asignar clasificacion = "BAJO"
   > Sino, si valor == 10 entonces:
       > asignar clasificacion = "LÍMITE"
   > Sino, si valor > 10 y valor <= 50 entonces:
       > asignar clasificacion = "NORMAL"
   > Sino:
       > asignar clasificacion = "ALTO"
   > Fin Si

   > Imprimir resultados en pantalla (ID, Valor y Clasificación)
>Fin del Algoritmo
## Diagrama de flujo 
>Inicio ➔ Lectura de datos (registro_id y valor).

>Condición 1: ¿valor < 10?

>Sí ➔ Clasificación = "BAJO" ➔ Ir a Impresión.

>No ➔ Pasar a la siguiente condición.

>Condición 2: ¿valor == 10?

>Sí ➔ Clasificación = "LÍMITE" ➔ Ir a Impresión.

>No ➔ Pasar a la siguiente condición.

>Condición 3: ¿10 < valor <= 50?

>Sí ➔ Clasificación = "NORMAL" ➔ Ir a Impresión.

>No (Caso contrario) ➔ Clasificación = "ALTO" ➔ Ir a Impresión.

>Impresión de Resultados ➔ Fin.
# Impliementar estructuras 
>DataLab - Semana 2
>Implementación de estructuras condicionales múltiples (if, elif, else).



>def main():
   > print("=== DataLab | Semana 2 ===")
   > print("Procesamiento de registros con reglas de decisión.\n")
    
# Entradas del sistema

   >  registro_id = input("Ingrese el identificador del registro: ")
   > valor = float(input("Ingrese el valor del registro: "))
    
# Estructura condicional múltiple (if - elif - else)

   > if valor < 10:
      >  clasificacion = "BAJO"
   > elif valor == 10:
   >     clasificacion = "LÍMITE"
   > elif 10 < valor <= 50:
       > clasificacion = "NORMAL"
   > else:
       > clasificacion = "ALTO"
        
# Salidas del sistema

   > print("\n--- Resultado ---")
   > print(f"Registro: {registro_id}")
   > print(f"Valor: {valor}")
   > print(f"Clasificación: {clasificacion}")

>if _name_ == "_main_":
  >  main()
## Explicacion del comportamiento segun los valores ingresados 
>El valor está por debajo del límite: Cuando ingresas un número menor a 10 (por ejemplo, 4), la primera condición (valor < 10) se evalúa como verdadera. El programa asigna inmediatamente la clasificación "BAJO" y se salta todas las demás evaluaciones posteriores.

>EL valor se encuentra exactamente en un límite: Cuando ingresas el número exacto del umbral (por ejemplo, 10), la primera condición falla, pero la segunda (valor == 10) se cumple. Esto activa el bloque elif correspondiente, clasificándolo como "LÍMITE", permitiendo controlar de forma precisa las fronteras del sistema.

>El valor está dentro del rango esperado: Cuando ingresas un número que cumple con el intervalo intermedio (por ejemplo, 25), el programa pasa por alto las condiciones anteriores y evalúa el rango válido (10 < valor <= 50), asignando la categoría "NORMAL".

>El valor supera el límite establecido: Cuando el número ingresado es superior al tope máximo permitido (por ejemplo, 80), ninguna de las condiciones anteriores (if o elif) resulta verdadera. Por lo tanto, el flujo del programa cae por defecto en la instrucción else, catalogando el registro como "ALTO".
# Realizar pruebas 
>Caso Bajo:

>Dato de entrada: valor = 5

>Comportamiento esperado: Entra en la primera condición (< 10).

>Resultado impreso: Clasificación: BAJO.

>Caso de Límite (Frontera):

>Dato de entrada: valor = 10

>Comportamiento esperado: Evalúa y acierta en el límite exacto (== 10).

>Resultado impreso: Clasificación: LÍMITE.

>Caso Normal:

>Dato de entrada: valor = 30

>Comportamiento esperado: Se ubica dentro del rango intermedio definido.

>Resultado impreso: Clasificación: NORMAL.

>Caso Alto:

>Dato de entrada: valor = 65

>Comportamiento esperado: Supera los límites anteriores y activa la salida por defecto.

>Resultado impreso: Clasificación: ALTO.