# Sentencia else if `elif`
Esta estructura `elif` es una estructura consecuente de la sentencia  `if`, en la cual se evalúan diferentes casos.

En Python no existe una orden `switch` o `case`, sino que se deben realizar enlazando varios casos con `elif`.

```python
if(condición 1):
	sentencia 1
elif(condición 2):
	sentencia 2
elif(condición 3):
	sentencia 3
.
.
.
else:
	sentencia n
```
La estructura `elif` se evalúa así: 

Si se cumple el primer caso **(condición 1)**, se ejecuta lo que se encuentra en la **sentencia 1** y **si no se cumple se examina secuencialmente los siguientes casos (condiciones) hasta llegar al último elif**. Si ninguna condición es verdadera entonces se ejecutara la sentencia **n** que corresponde al último **else**. 

![](https://media.giphy.com/media/YqbMIoq0b2cZIn1FUi/giphy.gif)																																								
El siguiente ejemplo se muestra cómo funciona:
```python
a = 10
b = 5
c = 11
 
if(a < b):
	print(“a es menor que b”)
elif(a == b):
	print(“a es igual que b”)
elif(a > c):
	print(“a es mayor que c”)
else:
	print(“Ningún caso es verdadero”)
```
En este ejemplo podemos observar que las condiciones son falsas porque así lo hemos hecho, pero primero se evalúa la **condición 1** que es **a < b** y si no se cumple sigue con la **condición 2** que es **a == b** hasta llegar a una **condición verdadera** que es el último **else** ya que las anteriores han sido falsas.
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjkxNzYzNTI2LDIxMzAwMTgzXX0=
-->