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


#### FRAGMENTO 04

#Creamos cuatro variables
rectX = windowWith / 2
rectY = windowHeight / 2
rectWidth = 500
rectHeight = 500

while True:
    #Borramos la informacion del frame anterior
    surface.fill((0, 0, 0))
    
    #Dibujamos una forma
    pygame.draw.rect(surface, (255, 255, 0), (rectX-rectWidth /2, rectY-rectHeight /2, rectWidth, rectHeight))
    
    #Toma el valor actual y sumale el valor que viene después
    rectWidth -= 1
    rectHeight -= 1
  
#### BOTTOM

    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
