# Bucles "while" de Python (iteración indefinida)
**La iteración significa ejecutar el mismo bloque de código una y otra vez, potencialmente muchas veces.** Una estructura de programación que implementa la iteración se llama bucle.

En programación, hay dos tipos de iteración, indefinida y definida:

 - Con la **iteración indefinida**, el número de veces que se ejecuta el ciclo no se especifica explícitamente de antemano. Más bien, el bloque designado se ejecuta repetidamente siempre que se cumpla alguna condición.
 - Con la **iteración definida**, el número de veces que se ejecutará el bloque designado se especifica explícitamente en el momento en que comienza el ciclo.

## Ciclo `while` 
Veamos cómo se usa la instrucción `while` de Python para construir bucles. Empezaremos de forma sencilla y embelleceremos sobre la marcha.

El formato de un bucle `while` rudimentario se muestra a continuación:
```python
while <cond>:
	<declaración(es)>
```
`<declaración(es)>` representa el bloque que se ejecutará repetidamente, a menudo denominado cuerpo del bucle. Esto se denota con sangría, como en una declaración `if`.

La condición de control, <cond>, normalmente involucra una o más variables que se inicializan antes de iniciar el ciclo y luego se modifican en algún lugar del cuerpo del ciclo.

**Cuando se encuentra un bucle `while`, <cond> se evalúa primero en contexto booleano. Si es cierto (True), se ejecuta el cuerpo del bucle. Luego, <cond> se vuelve a comprobar y, si sigue siendo cierto (True), el cuerpo se ejecuta de nuevo. Esto continúa hasta que <cond> se vuelve falso (False), momento en el que la ejecución del programa procede a la primera instrucción más allá del cuerpo del bucle.**

Considerando este bucle:
```python
n = 5
while n > 0:
	n -= 1
	print(n)

# Interprete
>>> 4
>>> 3
>>> 2
>>> 1
>>> 0
```
Esto es lo que sucede en este ejemplo:

- `n` es inicialmente `5`. La expresión en el encabezado de la instrucción `while` en la línea 2 es `n> 0`, lo cual es **verdadero** (`True`), por lo que se ejecuta el cuerpo del ciclo. Dentro del cuerpo del bucle en la línea 3, n se reduce en 1 a un valor de 4 y luego se imprime.

- Cuando el cuerpo del bucle ha terminado, la ejecución del programa vuelve a la parte superior del bucle en la línea 2 y la expresión se evalúa nuevamente. Sigue siendo **cierto**, por lo que el cuerpo se ejecuta de nuevo y se imprime 3.

- Esto continúa hasta que `n` se convierte en `0`. En ese punto, cuando se prueba la expresión, es **falsa (False) y el ciclo termina**. La ejecución se reanudaría en la primera declaración que sigue al cuerpo del bucle, pero no hay ninguna en este caso.

Tenga en cuenta que la expresión de control del ciclo `while` se prueba primero, antes de que suceda cualquier otra cosa. Si es falso para empezar, el cuerpo del bucle nunca se ejecutará en absoluto:
```python
n = 0
while n > 0:
	n -= 1
	print(n)
```
En el ejemplo anterior, cuando se encuentra el bucle, `n` es `0`. La expresión de control `n> 0` ya es **falsa (False), por lo que el cuerpo del bucle nunca se ejecuta.**

Aquí hay otro ciclo `while` que involucra una lista, en lugar de una comparación numérica:
```python
a = ['foo', 'bar', 'baz']
while a:
	print(a.pop(-1))

# Interprete
>>> baz
>>> bar
>>> foo	
```
**Cuando una lista se evalúa en contexto booleano, es verdadera si tiene elementos y falsa si está vacía.** En este ejemplo, a es verdadero siempre que tenga elementos. Una vez que todos los elementos se han eliminado con el método `.pop()` y **la lista está vacía, a es falso y el ciclo termina.**

## Las declaraciones de Python `break` y `continue`
En cada ejemplo que ha visto hasta ahora, todo el cuerpo del ciclo `while` se ejecuta en cada iteración. Python proporciona dos palabras clave que terminan prematuramente una iteración de bucle:

- **La declaración `break` de Python termina inmediatamente un ciclo por completo**. La ejecución del programa procede a la primera instrucción que sigue al cuerpo del bucle.

La instrucción continue de Python termina inmediatamente la iteración del ciclo actual. La ejecución salta a la parte superior del ciclo y la expresión de control se vuelve a evaluar para determinar si el ciclo se ejecutará de nuevo o terminará.

La distinción entre romper y continuar se demuestra en el siguiente diagrama
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyOTA2NDU4NzEsNTE4OTE4MDY4XX0=
-->