# Simulador.py

![](https://media.giphy.com/media/3o6ZtlX2L2kuaO1rhu/giphy.gif)

En las siguientes líneas de `simulator.py` tenemos todas las variables que necesitamos para ejecutar nuestro programa. Las declaraciones de importación en la parte superior de nuestro script son casi idénticas a nuestros programas anteriores, con una excepción: `import solarsystem` en la **línea 5**. 

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
**Este no es un módulo como las otras declaraciones de importación, sino un script personalizado escrito para este tutorial, y puede obtenerlo de [Aqui](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/pyg_partII/PracticasPyG/Practica6/solarsystem.py). Simplemente colóquelo en la misma carpeta que el `simulador.py`; simplemente crea nuevos planetas para nuestro simulador y no necesita estar en el código `simulator.py` principal, ya que nuestros juegos comenzarán a complicarse si todo está en un solo script.**

Las líneas 31-54 contienen las funciones `drawUI()` , `drawPlanet ()` y `drawCurrentBody()`. Estos son los responsables de dibujar los elementos de nuestro programa en nuestra ventana. Todos estos se llaman una vez cada vez que se ejecuta el bucle principal, en el orden `drawUI()`, `drawPlanets()` y luego `drawCurrentBody ()`.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExMDc0NTE5ODYsLTE1OTU4NjQwMzMsNT
A5Nzc5NjI1LDQ4NjE3OTg5NywtNjU4Mjg5MDk2LDc3NTgxMjI2
XX0=
-->