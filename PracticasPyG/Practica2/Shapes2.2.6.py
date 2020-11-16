#### TOP

import pygame, sys, random
#incluye propiedades del sistema y estado de juego
import pygame.locals as GAME_GLOBALS
#incluye lista de eventos: teclado, sistema, etc. 
import pygame.event as GAME_EVENTS

pygame.init()
windowWidth = 640 # Ancho Ventana
windowHeight = 480 # Alto de ventana
surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Pygame Shapes PILARES!")


#### FRAGMENTO 05
cuadroRojo = random.randint(0, 255) # Genera numeros aleatorios entre 0 y 255
cuadroAzul = random.randint(0, 255) # Genera numeros aleatorios entre 0 y 255
cuadroVerde = random.randint(0, 255) # Genera numeros aleatorios entre 0 y 255

while True: # True = Verdadero | loop = ciclo infinito de repeticion
    surface.fill((0, 0, 0)) # referscar la ventana
    pygame.draw.rect(surface, (cuadroRojo, cuadroVerde, cuadroAzul), (50, 50, windowWidth /2, windowHeight /2))
    
    if cuadroRojo >= 255:
        cuadroRojo = random.randint(0, 255)
    else:
        cuadroRojo += 1
    
    if cuadroVerde >= 255:
        cuadroVerde = random.randint(0, 255)
    else:
        cuadroVerde += 1
        
    if cuadroAzul >= 255:
        cuadroAzul = random.randint(0, 255)
    else:
        cuadroAzul += 1
    
    

#### BOTTOM

    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
