
# SHAPES & PATHS con PYGAME
### Vamos a aprender a hacer un juego desde cero. En las primeras practicas, aprendemos los conceptos básicos.

En este curso, vamos a aprender a hacer juegos con Pygame. Examinaremos los controles de dibujo, animación, teclado y mouse, sonido y física. Cada capítulo se sumará a nuestro conocimiento del desarrollo de juegos, lo que nos permitirá comprender los juegos que jugamos y crear casi cualquier cosa que pueda imaginar nuestra imaginación.

**Este curso no es para principiantes de programación, pero no está lejos de eso: vamos a suponer que ha escrito algunos programas simples de Python (o similares) en el pasado, y que puede hacer cosas como crear archivos y moverse por el sistema de archivos sin demasiada dificultad**.

En la primera practica, veremos cómo dibujar y colorear varias formas en una ventana. No se trata de Grand Theft Auto V, sin duda, pero dibujar formas es el primer paso para construir casi cualquier cosa.

Para comenzar, abra su editor de texto preferido *(sublime text, gedit, blog de notas, etc.)*, cree un nuevo archivo, inserte el siguiente código y guárdelo como `hello.py`

```python 
import pygame 

pygame.init()

window = pygame.display.set_mode((500,300))

while True:
	pygame.draw.rect(window, (255,0,0), (0,0,50,30))

	pygame.display.update()
```

Ejecutemos ese código y veamos qué hace. En su ventana de terminal, ingrese `python3 hello.py`

Si todo ha ido bien, se abrirá una nueva ventana que le mostrará un cuadrado rojo sobre un fondo negro en la esquina superior izquierda de la ventana. 

![https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica1/hello_py001.JPG](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica1/hello_py001.JPG)

**Acabamos de crear nuestro primer programa Pygame: vamos a verlo.**

## Entendiendo `hello.py`
Las primeras dos líneas de nuestro primer programa son muy simples: **todo lo que hemos hecho es decirle a Python que queremos usar Pygame.** 

> `import pygame` **carga todo el código Pygame en nuestro script, por lo que no tenemos que escribir todo ese código nosotros mismos.** Pygame está diseñado para facilitar la creación de juegos y software interactivo.

>`pygame.init()` **le dice a Pygame que estamos listos para comenzar a usarlo.**

Veamos la tercera línea de código:
```python
window = pygame.display.set_mode((500,300))
```
**window** es el parámetro que vamos a usar para decirle a nuestro programa Pygame cómo debería verse cuando se ejecuta; cada parámetro afecta la forma y el tamaño de la ventana de la aplicación. Tenga en cuenta que aquí, el ancho siempre viene antes que la altura.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTI0MjUzNDEwMiwtNzk0ODgxNjEyXX0=
-->