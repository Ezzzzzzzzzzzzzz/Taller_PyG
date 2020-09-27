#### TOP

import pygame, sys, random
#incluye propiedades del sistema y estado de juego
import pygame.locals as GAME_GLOBALS
#incluye lista de eventos: teclado, sistema, etc. 
import pygame.event as GAME_EVENTS

pygame.init()
windowWith = 640
windowHeight = 480
surface = pygame.display.set_mode((windowWith, windowHeight))
pygame.display.set_caption("Pygame Shapes!")


#### FRAGMENTO 03

#Creamos cuatro variables
blueSquareX = 0.0
blueSquareY = 0.0
blueSquareVX = 1
blueSquareVY = 1

while True:
    #Borramos la informacion del frame anterior
    surface.fill((0, 0, 0))
    
    #Dibujamos una forma
    pygame.draw.rect(surface, (0, 0, 255), (blueSquareX, blueSquareY, 10, 10))
    
    #Toma el valor actual y sumale el valor que viene después
    blueSquareX += blueSquareVX
    blueSquareY += blueSquareVY
    blueSquareVX += 0.1
    blueSquareVY += 0.1
  
#### BOTTOM

    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
