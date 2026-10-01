<<<<<<< HEAD
# Solucion de preguntas
# Analisis del ejercicio 1
## ¿Cuantas veces se ejecuta?
>Se ejecuta 5 veces (exactamente una vez por cada iteración del ciclo for range(5)).
## ¿Cuántas veces se ejecuta el if?
>Se ejecuta 5 veces (una vez por cada vuelta del ciclo para evaluar el resultado que retorna la función validar_nombre()).
## ¿Qué parte cambia en cada iteración?
>El valor de i, que va tomando los valores de 0, 1, 2, 3 y 4.

>El número del mensaje al usuario (i + 1), que cambia visualmente de 1 a 5 en cada turno.

>El valor de la variable nombre, ya que el usuario ingresa un texto diferente (o un nombre distinto) en cada repetición.
## ¿Qué parte permanece igual?
>La estructura del ciclo (for i in range(5):), que siempre repite el mismo bloque cinco veces.

>La llamada a la función (validar_nombre(nombre)), que se ejecuta de la misma forma en cada vuelta.

><La lógica condicional y los mensajes (" Nombre válido" y " Nombre inválido"), que se imprimen bajo la misma regla estructural sin importar cuántas veces corra el ciclo.
## ¿Que problema resuelve un ciclo?
>Resuelve el problema de la repeticion manual de codigo. Sin un ciclo, tendrías que escribir o copiar la misma instruccion una y otra vez (por ejemplo, escribir input() diez veces). El ciclo automatiza la repeticion de un bloque de codigo tantas veces como sea necesario de forma limpia y eficiente.
## ¿Por que range(5) produce 5 iteraciones?
>Porque en Python, range() comienza a contar por defecto desde el número 0 y genera números secuenciales menores que el número que le pasas como límite. Por lo tanto, range(5) genera los valores 0, 1, 2, 3, 4, lo que suma exactamente cinco elementos (cinco vueltas o iteraciones).
## ¿Qué diferencia existe entre una función y un ciclo?
>Un ciclo (for) se encarga de repetir una o varias instrucciones de manera consecutiva.

>>Una función se encarga de agrupar una tarea específica (un bloque con nombre y lógica propia) para poder ejecutarla y reutilizarla las veces que se necesite, sin importar si es dentro o fuera de un ciclo.
## ¿Por qué una validación debería ser una función reutilizable?
>Porque evita que tengas que escribir la misma lógica de comprobación (como revisar si un correo tiene @) en diferentes partes del programa. Si la regla cambia en el futuro, solo debes modificarla en un solo lugar (dentro de la función) en lugar de buscar por todo el código.
## ¿Por qué separar las validaciones en un módulo?
>Para mantener el código ordenado y aplicar el principio de responsabilidad única. Si colocas todas las funciones de validación en un archivo independiente (como validaciones.py), el archivo principal (main.py) queda más limpio, es más fácil de mantener y cualquier otro programa puede importar esas reglas sin duplicar código.
## ¿Qué función cumplen los contadores?
>Sirven para ir registrando y sumando cantidades a medida que el programa avanza (por ejemplo, llevar la cuenta exacta de cuántos registros fueron válidos y cuántos inválidos dentro de un ciclo).
## ¿Qué diferencia existe entre procesar un registro y procesar muchos registros?
>Procesar un registro implica evaluar una sola entrada de datos de forma aislada. Procesar muchos registros requiere combinar la validación con un ciclo para automatizar el flujo, permitiendo recopilar resultados de un conjunto completo de datos y calcular indicadores globales (como totales y porcentajes de calidad).
## ¿Qué ocurre si cambia una regla de validación?
>Si la validación está bien diseñada y centralizada en una función dentro de un módulo, solo necesitas actualizar el código en un único sitio. Automáticamente, todo el programa y los ciclos que utilicen esa función adoptarán la nueva regla sin romperse.
## ¿Por qué no conviene copiar y pegar una validación?
>Porque si copias y pegas el mismo código de validación en varios lugares, creas redundancia. Si descubres un error o necesitas cambiar la regla de negocio, tendrías que corregir manualmente cada fragmento copiado, lo que aumenta el riesgo de cometer errores u olvidar alguna sección.
## ¿Cómo contribuye esta arquitectura al crecimiento de DataLab?
>Permite que el sistema sea escalable y modular. A medida que DataLab crezca y necesite procesar cientos de datos, conectar bases de datos o generar reportes complejos, tener las funciones separadas en módulos y la lógica de repetición organizada facilitará añadir nuevas características sin que el código se vuelva imposible de mantener.
=======
1. ¿Cuántas veces se ejecuta `validar_nombre()`?
> 5
2. ¿Cuántas veces se ejecuta el `if`?
>5
3. ¿Qué parte cambia en cada iteración?
>los numeros
4. ¿Qué parte permanece igual?
>ingrese el nombre 

>>>>>>> 830c261552f72c1972e3c0cdae76c8f7272b5906
