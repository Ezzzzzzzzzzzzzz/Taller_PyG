#Carga todo el codigo de pygame a nuestro script
import pygame 

#Le dice a pygame que estamos listos para usarlo
pygame.init() 

#"window" será el parametro de como debe verse Pygame cuando se ejecute el programa
# cada parametro afectara la forma y el tamaño

window = pygame.display.set_mode((500,400)) #((ancho, alto))

#Para evitar que se cierre el programa utilizamos la instruccion "while" y colocamos
#nuestro código adentro. El ciclo nunca terminara porque True siempre es True
while True:
    #Lo primero que hacemos es dibujar un rectangulo
    #(rojo,verde,azul) ----> 0 = nada | 255 = maximo de color
    #(coordenadaX, coordendaY, anchoRect, altoRect)
    pygame.draw.rect(window,(255,0,0), (0,0,50,50))
    #pygame.draw.rect(window,(0,255,0), (40,0,50,50))
    pygame.draw.rect(window,(0,0,255), (80,0,50,50))
    pygame.draw.rect(window,(0,255,0), (40,0,50,50))
    
    #Hemos terminado de dibujar
    pygame.display.update()
    
    
