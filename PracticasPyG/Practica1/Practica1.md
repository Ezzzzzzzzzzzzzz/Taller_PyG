
# SHAPES (formas) & PATHS (trayectorias) con PYGAME
## Vamos a aprender a hacer un juego desde cero. En las primeras practicas, aprendemos los conceptos básicos.

En este curso, vamos a aprender a hacer juegos con **Pygame**. Examinaremos los controles de dibujo, animación, teclado y mouse, sonido y física. Cada capítulo se sumará a nuestro conocimiento del desarrollo de juegos, lo que nos permitirá comprender los juegos que jugamos y crear casi cualquier cosa que pueda imaginar nuestra imaginación.

**Este curso no es para principiantes de programación, pero no está lejos de eso: vamos a suponer que ha escrito algunos programas simples de Python (o similares) en el pasado, y que puede hacer cosas como crear archivos y moverse por el sistema de archivos sin demasiada dificultad**.

![](https://media.giphy.com/media/aNqEFrYVnsS52/giphy.gif)

# hello.py

En la primera practica, veremos cómo dibujar y colorear varias formas en una ventana. No se trata de [**Grand Theft Auto V**](https://www.rockstargames.com/V/es), sin duda, pero dibujar formas es el primer paso para construir casi cualquier cosa.

Para comenzar, abra su editor de texto preferido *(sublime text, gedit, blog de notas, etc.)*, cree un nuevo archivo, inserte el siguiente código y guárdelo como `hello.py`

```python 
import pygame 

pygame.init()

window = pygame.display.set_mode((500, 400))

while True:
	pygame.draw.rect(window,(255, 0, 0), (0, 0, 50, 30))

	pygame.display.update()
```

Ejecutemos ese código y veamos qué hace. En su ventana de terminal, ingrese `python3 hello.py`

Si todo ha ido bien, se abrirá una nueva ventana que le mostrará un cuadrado rojo sobre un fondo negro en la esquina superior izquierda de la ventana. 

![https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica1/hello_py001.JPG](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica1/hello_py001.JPG)

**Acabamos de crear nuestro primer programa Pygame: vamos a verlo.**

# Entendiendo `hello.py`
Las primeras dos líneas de nuestro primer programa son muy simples: **todo lo que hemos hecho es decirle a Python que queremos usar Pygame.** 

> `import pygame` **carga todo el código Pygame en nuestro script, por lo que no tenemos que escribir todo ese código nosotros mismos.** Pygame está diseñado para facilitar la creación de juegos y software interactivo.

>`pygame.init()` **le dice a Pygame que estamos listos para comenzar a usarlo.**

Veamos la tercera línea de código:
```python
window = pygame.display.set_mode((500, 400))
```
`window` es el parámetro que vamos a usar para decirle a nuestro programa Pygame cómo debería verse cuando se ejecuta; cada parámetro afecta la forma y el tamaño de la ventana de la aplicación. Tenga en cuenta que aquí, el ancho siempre viene antes que la altura. `window` también es el parámetro que usaremos para indicar a otras líneas de código la superficie en la que deben dibujar formas y establecer colores. Con `window`, llamamos a la función `set_mode` del módulo de visualización de Pygame: este último es responsable de cómo se comporta la ventana y la superficie del juego *(un término informal para los píxeles que manipularemos)*. 
![https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica1/pygame.display.JPG](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica1/pygame.display.JPG)

En este caso, la ventana de la aplicación tiene 500 píxeles de ancho por 400 píxeles de alto. **Si pasamos números que son más grandes, la ventana del juego será más grande; Si pasamos números que son más pequeños, la ventana del juego será más pequeña.**

Las siguientes líneas son donde hacemos que nuestro programa dibuje formas en esa ventana. **Cuando los programas se ejecutan, ejecutan su código, y cuando terminan, se cierran.** Eso está bien a menos que, por supuesto, desee que su programa sea interactivo, o que dibuje o anime formas con el tiempo, que es exactamente lo que necesitamos de un juego.

Entonces, para evitar que nuestro programa salga, hacemos un **ciclo** `while` y colocamos todo nuestro código dentro. El **ciclo** `while` nunca terminará porque **True** siempre es **True**, por lo que podemos seguir ejecutando nuestro programa y dibujando nuestras formas todo el tiempo que queramos.

**Lo primero que hacemos en nuestro ciclo `while` es dibujar un rectángulo.** Un rectángulo es la forma más simple que podemos dibujar en Pygame:
```python
pygame.draw.rect(window, (255, 0, 0), (0, 0, 50, 30))
```
Luego, le dijimos a Pygame qué color queríamos que fuera nuestro rectángulo pasándolo a través de una **tupla (una lista especial de números)** que representa la cantidad de **rojo**, **verde** y **azul** que debería tener el color final. Usamos rojo, verde y azul, ya que estos son los tres colores que combina su pantalla para crear cada tono que pueda ver en ella. 
>`0` significa que nada de ese color debe usarse en la forma.
>
>`255` significa que la cantidad máxima de color debe estar en esa forma.

Le dijimos a nuestro rectángulo que debería ser el color `(255, 0, 0)`, que es **rojo puro**. 

Si le hubiéramos dicho que fuera `(255, 0, 255)`, habría sido de un color **púrpura brillante**, porque se dibuja con la cantidad máxima de rojo y la cantidad máxima de azul. 

Si le hubiéramos dicho a nuestro rectángulo que se coloreara `(100, 100, 100)`, sería un **gris oscuro**, porque todos los colores serían iguales.

Después de pasar por un color para que nuestro rectángulo sea, tenemos que decirle a dónde debe ir y qué tan grande debe ser. 

Hacemos esto pasando una **tupla de cuatro números**. 
>**El primer** número es una **coordenada X**, *que establece qué tan lejos del lado izquierdo de la ventana debe estar el borde izquierdo de nuestro rectángulo*. 
>
>**El segundo** número es una **coordenada Y**; *esto le dice al rectángulo qué tan lejos de la parte superior de nuestra ventana debe quedar el borde superior*. 
>
>**El tercer** número *da el ancho de nuestro rectángulo*. 
>
>**El cuarto** número *define su altura*.

Nuestra última línea en `hello.py` es agradable y simple: 
```python
pygame.display.update()
```
Le dice a Pygame que hemos terminado de dibujar formas por el momento y que ahora puede actualizar la ventana. Esto evita que  tenga que dibujar y volver a dibujar la pantalla para cada forma que hemos creado; en cambio, puede hacer que todos se dibujen de una vez.



<!--stackedit_data:
eyJoaXN0b3J5IjpbMjE0NzIyNjQxNCwtMTQ1NjgyNDI4MiwxOD
A3MjYwNTE4LC02MzU0NDE3NTQsLTE4OTQ4NDM5OTQsMzkzMDE3
ODk4LDE2NTg4OTIwMjMsMTcxMjUyNTA1OSwzNTM5MTYzNjUsLT
EwMjM1MjcyNzgsLTIwNjUwMjk5MzAsLTc5NDg4MTYxMl19
-->