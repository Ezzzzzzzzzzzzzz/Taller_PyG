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
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTAyODgzNjgsMTI4MjY4NDMzMCwtMzA3OD
kyMTg0LC0xNTUzMjA3ODI5XX0=
-->