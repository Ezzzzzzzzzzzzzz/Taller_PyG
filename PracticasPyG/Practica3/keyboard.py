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
playerSize = 20 # Tamaño del personaje
playerX = (windowWidth / 2) - (playerSize / 2) # Nos ayudan a saber la psicion del jugador en el eje X
playerY = windowHeight - playerSize # Nos ayuda a saber la pos. en el eje Y
playerVX = 1.0 # Velocidad del objeto en el eje X
playerVY = 0.0 # Velocidad en el eje Y
jumpHeight = 25.0 # Distancia del brinco
moveSpeed = 1.0
maxSpeed = 10.0 # Velocidad Maxima
gravity = 1.0  # gravedad

# Variables del teclado (keyboard)
leftDown = False # Tecla izquierda
rightDown = False # Tecla derecha
haveJumped = False # Brinco

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
    else:
        playerVY = 0.0
        haveJumped = False

    # ¿Está nuestro cuadrado en el aire?
    # ¡Mejor agrega algo de gravedad para bajarlo!
    if playerY < windowHeight - playerSize:
        playerY += gravity
        gravity = gravity * 1.1
    else:
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

while True: # loop

    surface.fill((0,0,0))

    pygame.draw.rect(surface, (255,0,0), (playerX, playerY, playerSize, playerSize))

    # Obtenga una lista de todos los eventos que sucedieron desde el último rediseño
    for event in GAME_EVENTS.get():

        if event.type == pygame.KEYDOWN: # Oprimir una tecla

            if event.key == pygame.K_LEFT: # ¿Alguien presiono tecla izq?
                leftDown = True # Veradadero
            if event.key == pygame.K_RIGHT:
                rightDown = True
            if event.key == pygame.K_UP:
                if not haveJumped: # Un solo brinco
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

    move() # Llamamos a la funcion move()

    clock.tick(60) #Al llamar Clock.tick(40) una vez por cuadro, el programa nunca se ejecutará a más de 40 cuadros por segundo.
    pygame.display.update()
