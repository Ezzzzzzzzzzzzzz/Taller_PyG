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

```

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTgxNDQwMzc4Nyw1MTg5MTgwNjhdfQ==
-->