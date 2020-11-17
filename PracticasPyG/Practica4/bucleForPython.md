# Bucles For en Python

En Python existen muchos objetos como por ejemplo las  [cadenas de texto (strings)](https://www.programaenpython.com/fundamentos/strings-en-python), las  [listas](https://www.programaenpython.com/fundamentos/listas-en-python), los  [diccionarios](https://www.programaenpython.com/fundamentos/diccionarios-en-python), y las  [tuplas](https://www.programaenpython.com/fundamentos/tuplas-en-python)  que son «iterables». Esto significa que podemos iterar sobre sus elementos: cada uno de los caracteres de una cadena de texto, cada uno de los elemento de una lista, etc. Esta operación se realiza con un bloque de código llamado bucle  **for** que indica las operaciones a realizar en cada iteración.

## Estructura básica de un bucle For

En lenguajes como C, C++ y Java entre otros, los bucles  _for_  se realizan mediante una variable de control y constan de tres partes:

-   Inicialización: es donde se asigna el valor inicial a la variable de control.
-   Condición de terminación: es una expresión booleana en realación a la variable de control que determina al final de cada iteración si se termina el bucle.
-   Iteración: determina el cambio que se realiza a la variable de control al final de cada iteración.

Este tipo de bucles se expresa de la siguiente forma:
```java 
// Código Java
for(i=0; i<10; i++)  {
// Hacer algo
}
```
En este bloque de código  **i**  es la variable de control, la cual:

-   Se ha inicializado con valor 0.
-   Continúa iterando mientras su valor sea mas pequeño que 10.
-   Al final de cada iteración incrementa su valor en 1.

En Python, en cambio, no se especifica ninguna variable de control para realizar bucles for. En lugar de ello se itera sobre una colección de objetos.

```python
# Python
for elemento in iterable:
# Hacer algo con el elemento
```
En este caso, en cada nueva iteración el «elemento» toma el valor del siguiente elemento del objeto «iterable». Además como ocurre con las [sentencias if](https://www.programaenpython.com/fundamentos/sentencias-condicionales-en-python), se requiere el uso de los dos puntos (:) al final de la sentencia y el cuerpo del bucle se tiene que indentar.

## Iterar una lista

Para recorrer los elementos de una lista con un bucle  _for_, hay que dar un nombre a la variable que va tomando los elementos de la lista en cada iteración. En el siguiente ejemplo se itera sobre los elementos de la lista «mi_lista» mediante la variable «n».
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5ODczNTgzNjIsNDE0MzgxMjAwLC00NT
Y5MzEwNjddfQ==
-->