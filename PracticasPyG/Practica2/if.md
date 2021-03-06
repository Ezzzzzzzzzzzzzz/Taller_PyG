# Sentencia "if"

La sentencia **if** _permite tomar una decisión para ejecutar una acción u otra_, esta decisión es del tipo booleana ya sea verdadero o falso y la sintaxis es la siguiente.
```python 
if(condición):
	sentencia 1
else:
	sentencia 2
```
## if
Donde la **condición** es una expresión lógica o relacional y **sentencia 1** y **sentencia 2** representan el código que quieren que se ejecute.

![](http://robolution.mx/clases/programacion/prpgramacion1.png)

## if & else
Una sentencia **if** se ejecuta de la forma siguiente:
1. Se evalúa la expresión condición.
2. Si el resultado de la evaluación de la condición es verdadera se ejecutará la **sentencia 1**.
3. Si el resultado de la condición es falso se ejecutara la **sentencia 2**.
4. Si el resultado de la condición es falso y no se ha puesto la cláusula **else**, la **sentencia 1 será ignorada**.
![](http://robolution.mx/clases/programacion/prpgramacion2.png)

A continuación se exponen algunos ejemplos de cómo se utiliza la sentencia **if**.

```python
a = 5 
b = 4

if(a < b):
	print(“a es menor que b”)
else:
	print(“a no es menor que b”)
```
En este ejemplo, la condición esta impuesta por una expresión de relación. Si al evaluar la condición se cumple que **a es menor que b** (lo cual es falso), entonces **imprimirá** un mensaje el cual es **“a es menor que b”**, **como sabemos que la condición es falsa se ejecuta la sentencia dos que imprime el mensaje “a no es menor que b”**. 

![](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica3/IFELSE.JPG)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyOTMyODM5OTYsMjUxMjk2MTA2LDY3NT
g2ODI2N119
-->