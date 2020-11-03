# Definición de funciones

**En Python, la definición de funciones se realiza mediante la instrucción  `def`  más un nombre de función descriptivo -para el cuál, aplican las mismas reglas que para el nombre de las variables- seguido de paréntesis de apertura y cierre.**

**Como toda estructura de control en Python, la definición de la función finaliza con dos puntos (`:`) y el algoritmo que la compone, irá identado con 4 espacios:**

```python
def mi_funcion(): 
    # aquí el algoritmo
```

**Una función, no es ejecutada hasta tanto no sea invocada.** Para invocar una función, simplemente se la llama por su nombre:
```python
def mi_funcion(): 
    print "Hola Mundo" 

mi_funcion()
```
Cuando una función, haga un  **retorno de datos**, éstos, pueden ser asignados a una variable:
```python
def funcion(): 
    return "Hola Mundo" 

frase = funcion() 
print frase
```

## Sobre los parámetros

Un parámetro es un valor que la función espera recibir cuando sea llamada (invocada), a fin de ejecutar acciones en base al mismo. Una función puede esperar uno o más parámetros (que irán separados por una coma) o ninguno.
```python
def mi_funcion(nombre, apellido): 
    # algoritmo
    .
    .
    .
```
Los parámetros, se indican entre los paréntesis, a modo de variables, a fin de poder utilizarlos como tales, dentro de la misma función.

Los parámetros que una función espera, serán utilizados por ésta, dentro de su algoritmo, a modo de  **variables de ámbito local**. Es decir, que los parámetros serán variables locales, a las cuáles solo la función podrá acceder:
```python
def mi_funcion(nombre, apellido): 
    nombre_completo = nombre, apellido 
    print nombre_completo
```
Si quisiéramos acceder a esas variables locales, fuera de la función, obtendríamos un error:
```python
def mi_funcion(nombre, apellido): 
    nombre_completo = nombre, apellido 
    print nombre_completo 

# Retornará el error: NameError: name 'nombre' is not defined
print nombre
```
Al llamar a una función, **siempre se le deben pasar sus argumentos en el mismo orden en el que los espera**. Pero esto puede evitarse, haciendo uso del paso de argumentos como keywords (ver más abajo: _"Keywords como parámetros"_).

## Parámetros por omisión

En Python, también es posible, asignar valores por defecto a los parámetros de las funciones. Esto significa, que la función podrá ser llamada con menos argumentos de los que espera:
```python
def saludar(nombre, mensaje='Hola'): 
    print mensaje, nombre 

saludar('Pepe Grillo') # Imprime: Hola Pepe Grillo
```

## Keywords como parámetros

En Python, también es posible llamar a una función, pasándole los argumentos esperados, como pares de  `claves=valor`:
```python
def saludar(nombre, mensaje='Hola'): 
    print mensaje, nombre

saludar(mensaje="Buen día", nombre="Juancho")
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTYyNjYzNjY1Nyw3NzE4MTQ1OTMsLTIwNj
k5MTY4ODJdfQ==
-->