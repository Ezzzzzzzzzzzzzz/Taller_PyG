# Animación de SHAPES (Formas) & PATHS (Trayectorias)

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
## Moviendo SHAPES en el tiempo y el espacio

Cuando pensamos en la animación, nuestras mentes pueden convertir dibujos en películas animadas: aquí, cambios sutiles en la forma y el color engañan a nuestros cerebros para que vean movimientos donde no los hay. 
No es diferente con las computadoras: cada vez que mueves un mouse o minimizas una ventana, nada se ha movido; en cambio, los píxeles se han dibujado, actualizado, actualizado y luego dibujado nuevamente, con todo en su nuevo lugar.

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

### Fragmento 1
```python

```
Si ejecuta el `cófragmento 01 (coloque el código superior, el código 01 y el código inferior juntos en un archivo) sin descomentar nada, verá un montón de cuadrados rojos que aparecen y desaparecen por toda la pantalla.

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTM4ODMzMDMzMCwtMjk0NTYyNDYwLC0yNz
Q0NDI2NTcsMTgyODI2NzU4NiwxOTM2MzMzNTI5XX0=
-->