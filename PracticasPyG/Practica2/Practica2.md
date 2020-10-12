# Animación de SHAPES (Formas) & PATHS (Trayectorias)

## Moviendo SHAPES en el tiempo y el espacio

Cuando pensamos en la animación, nuestras mentes pueden convertir dibujos en películas animadas: aquí, cambios sutiles en la forma y el color engañan a nuestros cerebros para que vean movimientos donde no los hay. 

**No es diferente con las computadoras:** cada vez que mueves un mouse o minimizas una ventana, nada se ha movido; en cambio, **los píxeles se han dibujado, actualizado, actualizado y luego dibujado nuevamente, con todo en su nuevo lugar.**

![](https://media.giphy.com/media/YTEAn0boXGmY0/giphy.gif)

## Algunas cosas que notar
### A partir de ahora, vamos a incluir `pygame.locals`y las `pygame.events` de Pygame. 
Estas son variables especiales que Pygame incluye para ayudarnos a escribir código más legible, así como eliminar parte de la complejidad de interactuar con el sistema en el que ejecutamos nuestro código.

>`pygame.locals` contiene principalmente propiedades que describen el sistema y el estado del juego, por lo que lo llamamos **GAME_GLOBALS** para reflejar esto.
```python
import pygame.locals as GAME_GLOBALS
```
> 
>`pygame.events` incluye una lista de eventos, como eventos de teclado o eventos del sistema que ocurrieron desde la última vez que Pygame actualizó su vista; por eso lo importamos como **GAME_EVENTS**.
```python
import pygame.event as GAME_EVENTS
```

### Código TOP (Cabecera)
```python
import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()
windowWidth = 640
windowHeight = 480
surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Pygame Shapes!")
```
**Vamos a usar en el código `Bottom` para verificar si nuestro jugador intentó o no abandonar el juego mientras se estaba ejecutando (en este caso, tratando de cerrar la ventana), y luego cerrar nuestro programa correctamente.**

### Código BOTTOM (Pie de código)
```python
	for event in GAME_EVENTS.get():
	    if event.type == GAME_GLOBALS.QUIT:
	        pygame.quit()
	        sys.exit()
	pygame.display.update()
```
Si ejecuta el código `Fragmento 01` (coloque el código `TOP` y el `Fragmento 01``  juntos en un archivo)  sin descomentar nada, verá un montón de cuadrados rojos que aparecen y desaparecen por toda la pantalla.

### Fragmento 01
```python
while True:
    surface.fill((0,0,0))
    pygame.draw.rect(surface, (255,0,0), (random.randint(0, windowWidth), random.randint(0, windowHeight), 10, 10))
```

![https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica2/Py2.JPG](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica2/Py2.JPG)

**¡No te preocupes, nada está roto!** Esto es solo para demostrar que Pygame dibuja, destruye y vuelve a dibujar cosas en una ventana. 

### **Agregue un `#`** al comienzo de la línea que comienza con `surface.fill()`. Usamos este código para borrar los datos de píxeles del marco (frame) anterior. Sin él, lo que vemos son todos los diferentes marcos (frames) construidos uno encima del otro a medida que pasa el tiempo. `surface.fill()` es como la pintura que usamos para cubrir el fondo de pantalla antiguo antes de agregar el nuevo: crea una pizarra en blanco con la que podemos trabajar.

**Pero eso no es muy útil, ¿verdad? Reemplacemos el código del `fragmento 01` con el `fragmento 02` y verá un cuadrado verde moviéndose lentamente a la derecha de la pantalla.**

![https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica2/p2.3.JPG](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica2/p2.3.JPG)

### Fragmento 02
```python
greenSquareX = windowWidth / 2
greenSquareY = windowHeight / 2

while True:
    surface.fill((0, 0, 0))
    pygame.draw.rect(surface, (0, 255, 0), (greenSquareX, greenSquareY, 10, 10))
    greenSquareX += 1
    #greenSquareY += 1
```
Entonces, ¿qué está haciendo que nuestro cuadrado se mueva? Cuando vimos la primera practica, dibujábamos formas como esta usando números que pasaríamos a Pygame, como `pygame.draw.rect(surface, (255,0,0), (20, 50, 40, 30))`, y eso está muy bien, siempre y cuando nunca quieras cambiar nada de esa forma.

**¿Qué pasaría si quisiéramos cambiar la altura, el ancho o el color de esta forma? ¿Cómo podríamos decirle a Pygame que cambie los números que ya ingresamos?** 

Aquí es donde entran las variables. En lugar de pasar números a `pygame.draw.rect()`, pasamos las variables en su lugar. Después de dibujar las formas, podemos cambiar la variable para que la próxima vez que se dibuje se vea ligeramente diferente.

### Con el `fragmento 02`, cada vez que dibujamos nuestro cuadrado verde, agregamos `1` a la variable que usamos para definir su coordenada X (qué tan lejos está de la izquierda de la pantalla), `greenSquareX`. Hacemos esto con `+=`, que básicamente dice **"tome el valor actual de la variable y luego agregue el número que viene después"**.

>**Si cambiamos esa línea para leer `greenSquareX += 5`, cada vez que dibujemos nuestro cuadrado, será 5 píxeles a la derecha de donde estaba la última vez que se dibujó. Esto da la ilusión de que la forma se mueve más rápido que antes.** 
>
>**Si cambiamos el número que ajustamos a `greenSquareX` a `0`, nuestra forma nunca se movería** 
>
>**Si lo cambiamos a `-5`, se movería hacia atrás.**



<!--stackedit_data:
eyJoaXN0b3J5IjpbMjExNjczOTg4OSw3NDA4NTYzOTgsMTE0Mz
k3NDIyLDE3MDQ3NDAwNTgsLTE2ODUzMDgxMjAsLTE1NTg0OTMy
MzIsMzg4OTM1MTMsLTEwMzIxMDE0MywxNDU5ODEwNzYzLDEwND
c4MjMyMDUsLTcxMDQ3NjQyNCw3MjAwOTc2MDUsMjA1OTIwMzQy
NywtNzQ1NjY2OSwxOTI1NTE2ODgxLC0xOTYwMDExNjI3LC0xOT
M4MjA3NTE5LDE1NjY1OTM0NywxMDI1NzQ2MTU5LC03NTQ3MjA3
NDFdfQ==
-->