# Simulador.py

![](https://media.giphy.com/media/3o6ZtlX2L2kuaO1rhu/giphy.gif)

En las líneas de la **1 a la 30** de `simulator.py` tenemos todas las variables que necesitamos para ejecutar nuestro programa. Las declaraciones de importación en la parte superior de nuestro script son casi idénticas a nuestros programas anteriores, con una excepción: `import solarsystem` en la línea 5.

```python 
import pygame, sys, random, math
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
import solarsystem

windowWidth = 1024
windowHeight = 768

pygame.init()
clock = pygame.time.Clock()
surface = pygame.display.set_mode((windowWidth, windowHeight), pygame.FULLSCREEN)

pygame.display.set_caption('Solar System Simulator')

previousMousePosition = [0,0]
mousePosition = None
mouseDown = False

background = pygame.image.load("assets/background.jpg")
logo = pygame.image.load("assets/logo.png")
UITab = pygame.image.load("assets/tabs.png")
UICoordinates = [{"name" : "mercury", "coordinates" : (132,687)}, {"name" : "venus", "coordinates" : (229,687)}, {"name" : "earth", "coordinates" : (326,687)}, {"name" : "mars", "coordinates" : (423,687)}, {"name" : "jupiter", "coordinates" : (520,687)}, {"name" : "saturn", "coordinates" : (617,687)}, {"name" : "neptune", "coordinates" : (713,687)}, {"name" : "uranus", "coordinates" : (810,687)}]

celestialBodies = []
currentBody = None
drawAttractions = True
gravity = 10.0
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNDg2MTc5ODk3LC02NTgyODkwOTYsNzc1OD
EyMjZdfQ==
-->