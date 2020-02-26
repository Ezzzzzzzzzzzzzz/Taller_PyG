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


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTcwMTc0ODY0NSwxODI4MjY3NTg2LDE5Mz
YzMzM1MjldfQ==
-->