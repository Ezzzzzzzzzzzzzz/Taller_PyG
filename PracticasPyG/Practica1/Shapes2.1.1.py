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


#### FRAGMENTO 01

while True:
    #surface.fill((0, 0, 0))
    pygame.draw.rect(surface, (255, 0, 0), (random.randint(0, windowWith), random.randint(0, windowHeight), 10, 10))

    

#### BOTTOM

    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
