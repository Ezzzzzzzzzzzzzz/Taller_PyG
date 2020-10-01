# Tomando el control del Teclado y el Mouse
### Ahora que conocemos Pygame, vamos a empezar a hacer cosas con las que podamos jugar y que sean más interactivas. 

Nos estamos centrando en la dinámica del juego en este punto, pero no se preocupe, ¡las practicas posteriores explorarán los aspectos más estéticos del diseño del juego!

![](https://media.giphy.com/media/11y8mcRPyJ4aSk/giphy.gif)

En las dos primeras practicas, nos familiarizamos con los conceptos básicos de dibujar y mover formas de todo tipo, tamaño y color con Pygame. 

### Entonces, vayamos a nuestro primer programa: `keyboard.py`. 

A diferencia del practicas anteriores, no vamos a cortar y cambiar fragmentos de código para afectar el programa. Si copia `keyboard.py` y lo ejecuta en su computadora, se ejecutará tal como pretendemos. 

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

# ¿Cómo sabemos qué teclas se presionan y cuándo? 

En las practicas anterior, importamos `pygame.events` como `GAME_EVENTS`; ahora podemos usarlo. 

Cada programa de Pygame que escribimos es un gran bucle que se ejecuta para siempre o hasta que salimos del programa. Cada vez que se ejecuta nuestro ciclo, Pygame crea una lista de eventos que han ocurrido desde la última vez que se ejecutó el ciclo.

Esto incluye eventos del sistema, como una señal `QUIT`; *eventos del mouse*, *como un clic con el botón izquierdo*; y *eventos de teclado*, *como cuando se presiona o suelta un botón*. 

Una vez que tenemos la lista de eventos que recibió Pygame, podemos decidir cómo nuestro programa debe responder a esos eventos. 

**Si el usuario intenta salir, podríamos guardar el progreso del juego y cerrar la ventana en lugar de simplemente salir del programa, o podríamos mover un personaje cada vez que se presione una tecla**. 

Y eso es exactamente lo que hace `keyboard.py`.

- En la **línea 85**, creamos un bucle **for** que funcionará con cada evento en la lista que Pygame creó para nosotros. 
```python
# Obtenga una lista de todos los eventos que sucedieron desde el último rediseño
    for event in GAME_EVENTS.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                leftDown = True
            if event.key == pygame.K_RIGHT:
                rightDown = True
            if event.key == pygame.K_UP:
                if not haveJumped:
                    haveJumped = True
                    playerVY += jumpHeight
            if event.key == pygame.K_ESCAPE:
                quitGame()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                leftDown = False
                playerVX = moveSpeed
            if event.key == pygame.K_RIGHT:
                rightDown = False
                playerVX = moveSpeed

        if event.type == GAME_GLOBALS.QUIT:
            quitGame()
```
Los eventos están organizados en la lista en el orden en que los recibió Pygame. 

Entonces, por ejemplo, si quisiéramos usar los eventos del teclado para escribir el nombre de nuestro jugador, podríamos confiar en que obtendríamos todas las letras en el orden correcto y no solo una mezcla aleatoria de caracteres. Ahora que tenemos una lista de eventos, podemos trabajar con ellos y verificar si han sucedido ciertos eventos que son relevantes para nuestro juego. 

En `keyboard.py`, buscamos principalmente eventos de teclado; podemos comprobar si un evento es o no un evento de teclado comprobando su propiedad **type** con `event.type`. 

### Si nuestro `event.type` es un evento `pygame.KEYDOWN`, sabemos que se presionó una tecla; si nuestro `event.type` es un evento `pygame.KEYUP`, sabemos que una tecla se ha liberado. 

Buscamos eventos `KEYDOWN` en la **línea 87** y eventos `KEYUP` en la **línea 93**. Primero buscamos eventos `KEYDOWN` porque la lógica lo dicta: **¡tienes que presionar una tecla hacia abajo antes de que vuelva a aparecer!**

Sabemos que tenemos una forma de saber si se presionó una tecla, pero ¿cómo sabemos qué tecla presionó nuestro jugador? Cada evento de clave de Pygame tiene una propiedad **key** que describe qué tecla representa. Si imprimiéramos la propiedad `event.key`, veríamos muchos números, pero estas no son las teclas que presionamos.

Los números que veríamos son códigos clave; son números que están vinculados de forma única a cada tecla de su teclado, y los programadores pueden usarlos para comprobar qué teclas representan. Por ejemplo, la tecla ESC de su teclado es 27, la tecla A es 97 y la tecla RETURN es 13. ¿Significa esto que tenemos que recordar un montón de números aparentemente desconectados cuando escribimos el código del teclado? Afortunadamente, la respuesta es no. Pygame tiene un montón de valores para verificar códigos clave, que son más fáciles de leer y recordar cuando escribimos código.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY1Njk4NDY4MSwtMzM1OTYyMzUyLC0xMT
MwMjY3MTkwLDY4MTcxNzEwMiwxNTY3MDk0MzYwLDYzMzY4ODk3
MiwtOTkxODAyMDAxLDE2MDcxNjQ1MTgsMzMwMzk1OTE3LC0xMz
g5MTY1NjYsLTE1MjM3OTAzMzcsLTU4ODU5Njk2NSwxNjg4MTM2
ODI0LDgzNTQzNTY4NiwtNzg0ODcxMDEyLC03OTEzNTIyNDYsMT
Q0NzM4ODk4XX0=
-->