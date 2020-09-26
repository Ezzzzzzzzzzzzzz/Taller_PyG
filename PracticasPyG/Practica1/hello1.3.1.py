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
   
    #pygame.draw.circle(¿Donde dibujaremos?,(Rojo,Verde,Azul),(coordenadaX,coordenadaY),radio,altura,ancho)
    
    #Relleno
    pygame.draw.circle(window, (255,255,0), (250,200), 20, 0)
    
    #Sin relleno
    pygame.draw.circle(window, (255,255,0), (300,200), 20, 2)
    
    #Hemos terminado de dibujar
    pygame.display.update()
    
    
