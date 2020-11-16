# Tú primer juego

Ahora que hemos cubierto cómo crear formas, animarlas y configurar mecanismos de control, tenemos todo lo que necesitamos para hacer nuestro primer juego. **Vamos a hacer un juego desplegable de la vieja escuela donde las plataformas se elevan desde el suelo e intentan aplastar a nuestro jugador contra el techo; la única forma de sobrevivir es atravesando los huecos de las plataformas.**

![](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica4/drop.JPG)

**A diferencia de nuestros ejemplos anteriores, no vamos a escribir un programa que simplemente se ejecute: también crearemos una pantalla de inicio simple y una pantalla de finalización del juego**. 

Todavía tenemos un par de cosas nuevas que vamos a aprender a lo largo del camino, como cargar imágenes y cronometrar eventos. Este es, con mucho, el fragmento de código más grande que habremos escrito, pero no te preocupes: si lo ha seguido hasta ahora, ¡ya reconocerás gran parte de él!

## ¿Cómo funciona nuestro juego?
Antes de escribir cualquier código, es importante tener un conocimiento sólido de cómo va a funcionar nuestro juego. 

 - Cuando comience el juego, nuestro avatar (un rectángulo rojo) se
   desplegará desde la parte superior de la pantalla.
 - Cada dos segundos, una plataforma blanca comenzará a subir desde la
   parte inferior de la pantalla; si nuestro personaje aterriza en una
   de estas plataformas, comenzará a subir junto con ella. 
 - Si salimos de la parte superior de la pantalla del juego, se acabó el juego.
 - Podemos mover a nuestro personaje con las teclas de flecha izquierda y derecha para que pueda caer a través de los huecos colocados aleatoriamente en las plataformas. 

El objetivo del juego es sobrevivir el mayor tiempo posible. **Suena fácil, pero las cosas se ponen más difíciles a medida que pasa el tiempo, porque las plataformas comenzarán a aparecer después de un retraso más corto.**

## Variables y requisitos previos

Las primeras 39 líneas de nuestro código contienen las declaraciones de importación y las variables que vamos a necesitar para que nuestro juego despegue. A estas alturas, **gran parte de esto debería parecer bastante familiar. En la parte superior tenemos nuestras declaraciones de importación, que nos permiten incluir módulos para ayudar con el desarrollo de nuestro juego. Toma nota de la importación GAME_TIME, ya que se usará bastante más adelante.**

```python 
import pygame, sys, random

import pygame.locals as GAME_GLOBALS

import pygame.event as GAME_EVENTS

import pygame.time as GAME_TIME

pygame.init()

clock = pygame.time.Clock()

title_image = pygame.image.load("assets/title.jpg")

game_over_image = pygame.image.load("assets/game_over.jpg")

windowWidth = 400

windowHeight = 600

surface = pygame.display.set_mode((windowWidth, windowHeight))

pygame.display.set_caption('Drop!')

leftDown = False

rightDown = False

gameStarted = False

gameEnded = False

gamePlatforms = []

platformSpeed = 3

platformDelay = 2000

lastPlatform = 0

platformsDroppedThrough = -1

dropping = False

gameBeganAt = 0

timer = 0

```

Las líneas 8 y 9 están cargando imágenes que usaremos para nuestras pantallas de inicio y finalización del juego. Podríamos dibujar la interfaz gráfica de usuario (GUI) con código, pero al usar imágenes nos ahorramos tiempo y esfuerzo al costo de unos pocos kilobytes.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyOTEwMTY1NDIsLTQwMTAzODQwOCwtMT
A5ODEwMjA3OCwtODE2MjYxOTM2LDExNzUyMjA4NzFdfQ==
-->