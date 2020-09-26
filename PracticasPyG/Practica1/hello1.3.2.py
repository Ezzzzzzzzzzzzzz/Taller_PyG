#Carga todo el codigo de pygame a nuestro script
import pygame 

#Le dice a pygame que estamos listos para usarlo
pygame.init() 

#"window" será el parametro de como debe verse Pygame cuando se ejecute el programa
#cada parametro afectara la forma y el tamaño

window = pygame.display.set_mode((500,400)) #((ancho, alto))

#Para evitar que se cierre el programa utilizamos la instruccion "while" y colocamos
#nuestro código adentro. El ciclo nunca terminara porque True siempre es True
while True:
   
    #pygame.draw-ellipse(¿Donde dibujo?,(Rojo,Verde,Azul),(coordenadaX,coordenadaY,largoElipse,anchoElipse))
    pygame.draw.ellipse(window,(255,0,0), (100,100,100,50))
    pygame.draw.ellipse(window,(0,255,0), (100,150,80,40))
    pygame.draw.ellipse(window,(0,0,255), (100,190,60,30))
    
    #Hemos terminado de dibujar
    pygame.display.update()
    
    
