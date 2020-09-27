#Carga todo el codigo de pygame a nuestro script
import pygame

#Le dice a pygame que estamos listos para usarlo
pygame.init()

#"window" será el parametro de como debe verse Pygame cuando se ejecute el programa
#cada parametro afectara la forma y el tamaño
window = pygame.display.set_mode((500,400))

while True:
    
    #pygame.draw.line(¿Donde dibujare?,(Rojo,Verde,Azul),(XInicio,YInicio,XFin,YFin),AnchoLinea)
    pygame.draw.line(window, (255, 255, 225), (0, 0), (500, 400), 1)
    
    #Hemos terminado de dibujar
    pygame.display.update()