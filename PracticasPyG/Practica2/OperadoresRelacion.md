# Booleanos
El tipo **booleano de Python** es uno de los [tipos de datos integrados](https://realpython.com/python-data-types/) de Python . Se usa para representar el valor de verdad de una expresión. Por ejemplo, la expresión `1 <= 2`es `True`, mientras que la expresión `0 == 1`es `False`. Comprender cómo se comportan los valores booleanos de Python es importante para programar bien en Python.

# Operadores de relación

Los **operadores de relación** o de **comparación** permiten evaluar la **igualdad** y la **magnitud**. El resultado de una operación de relación es un valor **booleano verdadero o falso** (**1** o **0**). 

Los operadores de relación son los siguientes:

Operador   |    Operación
:-------:  |  :---------:
__<__         |  El primer operando **menor que** el segundo.
__>__          | El primer operando **mayor que** el segundo.
__<=__         | El primer operando **menor o igual que** el segundo.
__>=__        | El primer operando **mayor o igual que** el segundo.
__!=__         | El primer operando **distinto que** el segundo.
__==__         | El primer operando **igual que** el segundo.

Los operandos tienen que ser de un tipo primitivo. Por ejemplo:

```python
r = 10
t = 0 
y = 0

y = r == t 	# y = 0 (falso) porque r no es igual a t
y = r > t 	# y = 1 (verdadero) porque r es mayor que t
y = r != t 	# y = 1 (verdadero) porque r no es igual a t
```
Un operador de relación equivale a una pregunta relativa sobre como son dos operandos entre sí. Por ejemplo, la expresión **r == t** equivale a la pregunta **¿x es exactamente igual a y?** Una **respuesta si** equivale a un valor **verdadero (1)** y una **respuesta no** equivale a un valor **falso (0)**.


# Operadores lógicos
El **resultado de una operación lógica** (**AND**, **OR**, **XOR** y **NOT**) es un valor **booleano verdadero o falso ( 1 o 0)**. Las expresiones que dan como resultado valores booleanos pueden combinarse para formar expresiones booleanas utilizando los operadores lógicos indicados a continuación. 

_Los operandos deben ser expresiones que den un resultado **verdadero** o **falso**._

Operador     |     Operación
:-------:    | :--------:
**and**    |  **AND** Da como resultado **verdadero** si al evaluar cada uno de los operandos el **resultado es verdadero**. **Si uno de ellos es falso**, el resultado es **falso**. **Si el primer operando es falso, el segundo operando no es evaluado**.
**or**    | **OR** El resultado **es falso** si al evaluar cada uno de los operandos el resultado es falso. **Si uno de ellos es verdadero**, el resultado **es verdadero**. **Si el primer operando es verdadero, el segundo operando no es evaluado.**
**not**    |  **NOT** El resultado de aplicar este operador es falso si al evaluar su operando el resultado es verdadero, y verdadero en caso contrario.

El resultado de una operación lógica es de tipo **int** o **booleana**. 

Por ejemplo:
```python
o = 10
p = 0
q = 0
q = (o != 0) and (p != 0) # q = 0 (falso)
r = not q 	# r = 1 (verdadero)
g = not r 	# g = 0 (falso)
q = (o != 0) or (p != 0) # q = 0 (verdadero)
```
Los operandos del operador **and** son: **o != 0** y **p != 0**. El resultado de la expresión **o != 0 es verdadero** porque **o** vale **10** y **p != 0 es falso** porque **p** es **0**. Por lo tanto, **el resultado de verdadero and falso es falso**.

# Tablas de verdad

## AND
La función de la puerta lógica **AND** es la multiplicación, y viene representada de la siguiente manera:

![](https://aristoteles2pc.files.wordpress.com/2011/03/and-ok.jpg?w=147&zoom=2)

Para comprender mejor el funcionamiento de esta puerta lógica, nos podemos servir de la tabla de verdad:

![](https://aristoteles2pc.files.wordpress.com/2011/03/tabla-de-verdad.png?w=225&h=296&zoom=2)

## OR 
La función de la puerta lógica **OR** es la suma, y viene representada de la siguiente manera:

![](https://aristoteles2pc.files.wordpress.com/2011/03/orok.jpg?w=140&zoom=2)

Y la tabla de verdad de la puerta OR es la siguiente:

![](https://aristoteles2pc.files.wordpress.com/2011/03/or1.png)

## NOT

La función de la puerta lógica **NOT** es la inversa, es decir, lo que aparece en la salida es lo contrario de lo que aparece en la entrada.  
Se representa de la siguiente manera:

![](https://aristoteles2pc.files.wordpress.com/2011/03/notok1.jpg?w=138&zoom=2)

Viendo esta tabla de verdad comprenderemos mucho mejor e funcionamiento de la puerta lógica NOT:

![](https://aristoteles2pc.files.wordpress.com/2011/03/not1.png)
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjg0NjE5NDAwLC00MTE1NDEwNjksLTUzNz
I4NDExMywxNzM2NTUwNjEwLDEyODI2ODQzMzAsLTMwNzg5MjE4
NCwtMTU1MzIwNzgyOV19
-->