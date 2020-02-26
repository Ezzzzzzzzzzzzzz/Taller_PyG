# Animación de SHAPES (Formas) & PATHS (Trayectorias)

## Moviendo SHAPES en el tiempo y el espacio

Cuando pensamos en la animación, nuestras mentes pueden convertir dibujos en películas animadas: aquí, cambios sutiles en la forma y el color engañan a nuestros cerebros para que vean movimientos donde no los hay. 
No es diferente con las computadoras: cada vez que mueves un mouse o minimizas una ventana, nada se ha movido; en cambio, los píxeles se han dibujado, actualizado, actualizado y luego dibujado nuevamente, con todo en su nuevo lugar.

## Algunas cosas que notar
A partir de ahora, vamos a incluir `pygame.locals`y las `pygame.events` de Pygame. 
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
Lo vamos a usar en el código `Bottom` para verificar si nuestro jugador intentó o no abandonar el juego mientras se estaba ejecutando (en este caso, tratando de cerrar la ventana), y luego cerrar nuestro programa correctamente.

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
¡No te preocupes, nada está roto! Esto es solo para demostrar que Pygame dibuja, destruye y vuelve a dibujar cosas en una ventana. Agregue un `#` al comienzo de la línea que comienza con `surface.fill()`. Usamos este código para borrar los datos de píxeles del marco (frame) anterior. Sin él, lo que vemos son todos los diferentes marcos (frames) construidos uno encima del otro a medida que pasa el tiempo. `surface.fill()` es como la pintura que usamos para cubrir el fondo de pantalla antiguo antes de agregar el nuevo: crea una pizarra en blanco con la que podemos trabajar.

Pero eso no es muy útil, ¿verdad? Reemplacemos el código del `fragmento 01` con el `fragmento 02` y verá un cuadrado verde moviéndose lentamente a la derecha de la pantalla.

### Fragmento 02
```python
while True:
    surface.fill((0, 0, 0))
    pygame.draw.rect(surface, (0, 255, 0), (greenSquareX, greenSquareY, 10, 10))
    greenSquareX += 0.01
    #greenSquareY += 0.01
```
Entonces, ¿qué está haciendo que nuestro cuadrado se mueva? Cuando vimos la primera practica, dibujábamos formas como esta usando números que pasaríamos a Pygame, como `pygame.draw.rect(surface, (255,0,0), (20, 50, 40, 30))`, y eso está muy bien, siempre y cuando nunca quieras cambiar nada de esa forma.

¿Qué pasaría si quisiéramos cambiar la altura, el ancho o el color de esta forma? ¿Cómo podríamos decirle a Pygame que cambie los números que ya ingresamos? Aquí es donde entran las variables. En lugar de pasar números a `pygame.draw.rect()`, pasamos las variables en su lugar. Después de dibujar las formas, podemos cambiar la variable para que la próxima vez que se dibuje se vea ligeramente diferente.

Con el `fragmento 02`, cada vez que dibujamos nuestro cuadrado verde, agregamos `0.01` a la variable que usamos para definir su coordenada X (qué tan lejos está de la izquierda de la pantalla), `greenSquareX`. Hacemos esto con `+=`, que básicamente dice **"tome el valor actual de la variable y luego agregue el número que viene después"**.

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU2NTQ4MjI0MywxMDI1NzQ2MTU5LC03NT
Q3MjA3NDEsLTExNTk0Mzk5NTYsLTIyNzMzODE0LC0yOTQ1NjI0
NjAsLTI3NDQ0MjY1NywxODI4MjY3NTg2LDE5MzYzMzM1MjldfQ
==
-->