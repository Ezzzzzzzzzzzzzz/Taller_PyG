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


#### FRAGMENTO 02

#Creamos dos variables
greenSquareX = windowWidth / 2
greenSquareY = windowHeight / 2

while True:
    #Borramos la informacion del frame anterior
    surface.fill((0, 0, 0))
    
    #Dibujamos una forma
    pygame.draw.rect(surface, (0, 255, 0), (greenSquareX, greenSquareY, 10, 10))
    
    #Toma el valor actual y sumale el valor que viene después
    greenSquareX += 1
    #greenSquareY += 1
  
#### BOTTOM

    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
