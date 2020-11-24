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
Here’s what’s happening in this example:

-   `n`  is initially  `5`. The expression in the  `while`  statement header on line 2 is  `n > 0`, which is true, so the loop body executes. Inside the loop body on line 3,  `n`  is decremented by  `1`  to  `4`, and then printed.
    
-   When the body of the loop has finished, program execution returns to the top of the loop at line 2, and the expression is evaluated again. It is still true, so the body executes again, and  `3`  is printed.
    
-   This continues until  `n`  becomes  `0`. At that point, when the expression is tested, it is false, and the loop terminates. Execution would resume at the first statement following the loop body, but there isn’t one in this case.
    

Note that the controlling expression of the  `while`  loop is tested first, before anything else happens. If it’s false to start with, the loop body will never be executed at all:
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg1NTc5MDM2Myw1MTg5MTgwNjhdfQ==
-->