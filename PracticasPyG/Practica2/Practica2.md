# Animación de SHAPES (Formas) & PATHS (Trayectorias)

### Algunas cosas que notar
A partir de ahora, vamos a incluir `pygame.locals`y las `pygame.events` de Pygame. 
Estas son variables especiales que Pygame incluye para ayudarnos a escribir código más legible, así como eliminar parte de la complejidad de interactuar con el sistema en el que ejecutamos nuestro código.

>`pygame.locals` contiene principalmente propiedades que describen el sistema y el estado del juego, por lo que lo llamamos **GAME_GLOBALS** para reflejar esto.
```python
import pygame.locals
```
> 
>`pygame.events` incluye una lista de eventos, como eventos de teclado o eventos del sistema que ocurrieron desde la última vez que Pygame actualizó su vista; por eso lo importamos como **GAME_EVENTS**.
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjUxNDYxMDE4LDE4MjgyNjc1ODYsMTkzNj
MzMzUyOV19
-->