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
   
    pygame.draw.rect(window, (255,0,0), (100,100,100,50), 2)
    pygame.draw.ellipse(window, (255,0,0), (100,100,100,50))
    
    pygame.draw.rect(window, (0,255,0), (100,150,80,40), 2)
    pygame.draw.ellipse(window, (0,255,0), (100,150,80,40))
    
    pygame.draw.rect(window, (0,0,255), (100,190,60,30), 2)
    pygame.draw.ellipse(window, (0,0,255), (100,190,60,30))
    
    #Si los parametros de ancho y alto son iguales
    #ellipse dibuja un circulo
    pygame.draw.ellipse(window, (0,0,255), (100,250,40,40))
    
    #Hemos terminado de dibujar
    pygame.display.update()
    
    
