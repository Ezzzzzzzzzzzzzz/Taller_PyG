# Tomando el control del Teclado y el Mouse
### Ahora que conocemos Pygame, vamos a empezar a hacer cosas con las que podamos jugar y que sean más interactivas. 

Nos estamos centrando en la dinámica del juego en este punto, pero no se preocupe, ¡las practicas posteriores explorarán los aspectos más estéticos del diseño del juego!

![](https://media.giphy.com/media/11y8mcRPyJ4aSk/giphy.gif)

En las dos primeras practicas, nos familiarizamos con los conceptos básicos de dibujar y mover formas de todo tipo, tamaño y color con Pygame. 

### Entonces, vayamos a nuestro primer programa: `keyboard.py`. 

A diferencia del capítulo anterior, no vamos a cortar y cambiar fragmentos de código para afectar el programa. Si copia `keyboard.py` y lo ejecuta en su computadora, se ejecutará tal como pretendemos. 

Esta vez, vamos a recorrer el código línea por línea para comprender exactamente qué hace cada bit para el programa. 

Como muchas cosas en la informática, vamos a empezar desde arriba.

## Keyboard.py

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

# Variables del teclado (keyboard)
leftDown = False
rightDown = False
haveJumped = False

def move():

    global playerX, playerY, playerVX, playerVY, haveJumped, gravity

    # Muevete a la izquierda
    if leftDown:
        #Si ya nos estamos moviendo hacia la derecha, restablezca la velocidad de movimiento e invierta la dirección
        if playerVX > 0.0:
            playerVX = moveSpeed
            playerVX = -playerVX    
        # Asegúrate de que nuestro cuadrado no deje nuestra ventana a la izquierda.
        if playerX > 0:
            playerX += playerVX 

    # Muevete a la derecha
    if rightDown:
        # Si ya nos estamos moviendo hacia la izquierda, restablezca la velocidad de movimiento nuevamente.
        if playerVX < 0.0:
            playerVX = moveSpeed
        # Asegúrate de que nuestro cuadrado no deje nuestra ventana a la derecha.
        if playerX + playerSize < windowWidth:
            playerX += playerVX

    if playerVY > 1.0:
        playerVY = playerVY * 0.9
    else :
        playerVY = 0.0
        haveJumped = False

    # ¿Está nuestro cuadrado en el aire?
    # ¡Mejor agrega algo de gravedad para bajarlo!
    if playerY < windowHeight - playerSize:
        playerY += gravity
        gravity = gravity * 1.1
    else :
        playerY = windowHeight - playerSize
        gravity = 1.0

    playerY -= playerVY

    if playerVX > 0.0 and playerVX < maxSpeed or playerVX < 0.0 and playerVX > -maxSpeed:
        if haveJumped == False:
            playerVX = playerVX * 1.1

# Como quitar el programa
def quitGame():
    pygame.quit()
    sys.exit()

while True:

    surface.fill((0,0,0))

    pygame.draw.rect(surface, (255,0,0), (playerX, playerY, playerSize, playerSize))

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

    move()

    clock.tick(60)
    pygame.display.update()
``` 

> - Las primeras 12 líneas de código deberían resultarle bastante familiares a estas alturas; estas son las variables que hemos usado en las dos partes anteriores para definir cómo debería verse nuestra ventana y cómo queremos interactuar con Pygame y sus métodos.
>
> - La siguiente docena de líneas son variables que usaremos para determinar cómo debería verse nuestro cuadrado controlado por teclado y dónde debería estar. 
>
> - Después de eso, tenemos dos funciones, `move()` y `quitGame()`, que usaremos para movernos y salir del juego. 
> 
> - Finalmente, al igual que en la practica anterior, tenemos nuestro bucle principal donde actualizamos nuestro juego y redibujamos todos nuestros píxeles.

## ¿Cómo sabemos qué teclas se presionan y cuándo? 

En el capítulo anterior, importamos `pygame.events` como `GAME_EVENTS`; ahora podemos usarlo. 

Cada programa de Pygame que escribimos es un gran bucle que se ejecuta para siempre o hasta que salimos del programa. Cada vez que se ejecuta nuestro ciclo, Pygame crea una lista de eventos que han ocurrido desde la última vez que se ejecutó el ciclo.

Esto incluye eventos del sistema, como una señal `QUIT`; *eventos del mouse*, *como un clic con el botón izquierdo*; y *eventos de teclado*, *como cuando se presiona o suelta un botón*. 

Una vez que tenemos la lista de eventos que recibió Pygame, podemos decidir cómo nuestro programa debe responder a esos eventos. **Si el usuario intenta salir, podríamos guardar el progreso del juego y cerrar la ventana en lugar de simplemente salir del programa, o podríamos mover un personaje cada vez que se presione una tecla**. 

Y eso es exactamente lo que hace `keyboard.py`.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1ODkwMjAzMjIsLTEzODkxNjU2NiwtMT
UyMzc5MDMzNywtNTg4NTk2OTY1LDE2ODgxMzY4MjQsODM1NDM1
Njg2LC03ODQ4NzEwMTIsLTc5MTM1MjI0NiwxNDQ3Mzg4OThdfQ
==
-->