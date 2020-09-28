#### TOP

import pygame, sys, random
#incluye propiedades del sistema y estado de juego
import pygame.locals as GAME_GLOBALS
#incluye lista de eventos: teclado, sistema, etc. 
import pygame.event as GAME_EVENTS

pygame.init()
windowWidth = 640
windowHeight = 480
surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Pygame Shapes!")


#### FRAGMENTO 05

#Creamos tres variables
squaresRed = random.randint(0, 255)
squaresBlue = random.randint(0, 255)
squaresGreen = random.randint(0, 255)

while True:
    #Borramos la informacion del frame anterior
    surface.fill((0, 0, 0))
    
    #Dibujamos una forma
    pygame.draw.rect(surface, (squaresRed, squaresGreen, squaresBlue), (50, 50, windowWidth /2, windowHeight /2))
    
    #Condicional if
    if squaresRed >= 255:
        squaresRed = random.randint(0, 255)
    else:
        squaresRed += 1
    
    if squaresGreen >= 255:
        squaresGreen = random.randint(0, 255)
    else:
        squaresGreen += 1
    
    if squaresBlue >= 255:
        squaresBlue = random.randint(0, 255)
    else:
        squaresBlue += 1
  
#### BOTTOM

    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
