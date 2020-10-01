# Tomando el control del Teclado y el Mouse
### Ahora que conocemos Pygame, vamos a empezar a hacer cosas con las que podamos jugar y que sean más interactivas. 

Nos estamos centrando en la dinámica del juego en este punto, pero no se preocupe, ¡las practicas posteriores explorarán los aspectos más estéticos del diseño del juego!

![](https://media.giphy.com/media/11y8mcRPyJ4aSk/giphy.gif)

En las dos primeras practicas, nos familiarizamos con los conceptos básicos de dibujar y mover formas de todo tipo, tamaño y color con Pygame. 

### Entonces, vayamos a nuestro primer programa: `keyboard.py`. 

A diferencia del capítulo anterior, no vamos a cortar y cambiar fragmentos de código para afectar el programa. Si copia `keyboard.py` y lo ejecuta en su computadora, se ejecutará tal como pretendemos. 

Esta vez, vamos a recorrer el código línea por línea para comprender exactamente qué hace cada bit para el programa. 

Como muchas cosas en la informática, vamos a empezar desde arriba.

 - Las primeras **12 líneas** de código deberían resultarle bastante familiares a estas alturas; estas son las variables que hemos usado en las dos partes anteriores para definir cómo debería verse nuestra ventana y cómo queremos interactuar con Pygame y sus métodos.
```python
import pygame, sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

# Variables de Pygame
pygame.init()
clock = pygame.time.Clock()

windowWidth = 800
windowHeight = 800

surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Pygame Keyboard!')
```

- La siguiente docena de líneas son variables que usaremos para determinar cómo debería verse nuestro cuadrado controlado por teclado y dónde debería estar. 
```python
# Variables del cuadrado
playerSize = 20
playerX = (windowWidth / 2) - (playerSize / 2)
playerY = windowHeight - playerSize
playerVX = 1.0
playerVY = 0.0
jumpHeight = 25.0
moveSpeed = 1.0
maxSpeed = 10.0
gravity = 1.0
```
 - Después de eso, tenemos dos funciones, `move()` y `quitGame()`, que usaremos para movernos y salir del juego. 
```python
def move():
	# Instrucciones de como nos movemos

def quitGame():
	# Instrucciones para salir del programa
```
 - Finalmente, al igual que en la practica anterior, tenemos nuestro bucle principal donde actualizamos nuestro juego y redibujamos todos nuestros píxeles.

```python
while True:
	. 
	. 
	.
```



<!--stackedit_data:
eyJoaXN0b3J5IjpbLTk5MTgwMjAwMSwxNjA3MTY0NTE4LDMzMD
M5NTkxNywtMTM4OTE2NTY2LC0xNTIzNzkwMzM3LC01ODg1OTY5
NjUsMTY4ODEzNjgyNCw4MzU0MzU2ODYsLTc4NDg3MTAxMiwtNz
kxMzUyMjQ2LDE0NDczODg5OF19
-->