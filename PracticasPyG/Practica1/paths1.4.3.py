#Carga todo el codigo de pygame a nuestro script
import pygame

#Le dice a pygame que estamos listos para usarlo
pygame.init()

#"window" será el parametro de como debe verse Pygame cuando se ejecute el programa
#cada parametro afectara la forma y el tamaño
window = pygame.display.set_mode((500,400))

while True:
    
    #pygame.draw.lines(¿Donde dibujare?, color, ¿cerrar figura x nosotros?, pts para dibujar, anchoLinea)
    pygame.draw.lines(window, (255, 255, 255), True, ((50, 50), (75, 75), (63, 100), (38, 100), (25, 75)), 1)
    
    #Hemos terminado de dibujar
    pygame.display.update()