# ¿Cómo sabemos qué teclas se presionan y cuándo? 

En las practicas anterior, importamos `pygame.events` como `GAME_EVENTS`; ahora podemos usarlo. 

Cada programa de Pygame que escribimos es un gran bucle que se ejecuta para siempre o hasta que salimos del programa. Cada vez que se ejecuta nuestro ciclo, Pygame crea una lista de eventos que han ocurrido desde la última vez que se ejecutó el ciclo.

Esto incluye eventos del sistema, como una señal `QUIT`; *eventos del mouse*, *como un clic con el botón izquierdo*; y *eventos de teclado*, *como cuando se presiona o suelta un botón*. 

Una vez que tenemos la lista de eventos que recibió Pygame, podemos decidir cómo nuestro programa debe responder a esos eventos. 

**Si el usuario intenta salir, podríamos guardar el progreso del juego y cerrar la ventana en lugar de simplemente salir del programa, o podríamos mover un personaje cada vez que se presione una tecla**. 

Y eso es exactamente lo que hace `keyboard.py`.

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

<!--stackedit_data:
eyJoaXN0b3J5IjpbMjAzNTYzMTgzNywtMTYwMTI3Mjc3NF19
-->