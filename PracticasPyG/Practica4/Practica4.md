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

Las primeras 39 líneas de nuestro código contienen las declaraciones de importación `import` y las variables que vamos a necesitar para que nuestro juego despegue. A estas alturas, **gran parte de esto debería parecer bastante familiar. En la parte superior tenemos nuestras declaraciones de importación `import`, que nos permiten incluir módulos para ayudar con el desarrollo de nuestro juego. Toma nota de la importación `GAME_TIME`, ya que se usará bastante más adelante.**

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

Las líneas: 
```python 
title_image = pygame.image.load("assets/title.jpg")
game_over_image = pygame.image.load("assets/game_over.jpg")
```
están cargando imágenes que usaremos para nuestras pantallas de inicio y finalización del juego.

### Podríamos dibujar la interfaz gráfica de usuario (GUI) con código, pero al usar imágenes nos ahorramos tiempo y esfuerzo al costo de unos pocos kilobytes.

Hemos visto estas líneas antes:
```python

windowWidth = 400
windowHeight = 600

surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Drop!')
```
estas son las variables que usaremos para controlar cómo se ve la ventana del juego. 

Las líneas: 
```python
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

player = {
  "x" : windowWidth / 2,
  "y" : 0,
  "height" : 25,
  "width" : 10,
  "vy" : 5
}
```
Son las variables que usaremos para realizar un seguimiento del estado de nuestro juego, como dónde están las cosas, qué tan grandes son y cómo deben moverse. Dos de estas pueden destacar como un poco diferentes de las variables que hemos usado anteriormente: `gamePlatforms` y `player`. **Uno de estos parece vacío y el otro tiene varios valores. `gamePlatforms`es un tipo de variable conocido como lista, mientras que `player` es un tipo conocido como diccionario y no funcionan como lo hacen otras variables. Dediquemos un poco de tiempo a comprender cómo funcionan.**

## Diccionarios y listas

En practicas anteriores, casi siempre hemos usado variables que tienen un valor, pero hay otras variables que pueden contener múltiples valores,**- como tuplas, por ejemplo -**, y estas son muy útiles para nosotros a medida que comenzamos a hacer programas más grandes y poderosos. Cuando escribimos programas pequeños, tener variables con un solo valor es genial, porque podemos ver qué variables están haciendo qué.

Sin embargo, a medida que los programas crecen, puede resultar más difícil nombrar las variables de una manera que se relacione con lo que intentamos hacer. Imaginemos un juego en el que hay más de un jugador, como un [MMO (Multijugador Online Masivo)](https://es.wikipedia.org/wiki/Videojuego_multijugador_masivo_en_l%C3%ADnea); si escribimos código como lo hemos hecho antes, necesitaríamos crear varios conjuntos de variables para cada jugador. **No hace falta ser un genio para darse cuenta de que el código se volverá inmanejable y muy rápido**.

¿Y si quisiéramos manejar a cuatro o 100 o 1,000 jugadores al mismo tiempo? ¿Escribimos a mano variables para cada uno? **No**. **En su lugar, podemos utilizar diccionarios y listas**.

La variable `player` es un diccionario. Un diccionario es una variable con varias claves (keys) que tienen valores.

### Puede pensar en un diccionario como lo haría en su contraparte del mundo real: si quiere saber qué es algo, busque hasta encontrar la definición.

Entonces, digamos que queremos saber cuál es el valor de `x` en el diccionario del `player`; todo lo que tenemos que hacer es solicitar `player["x"]`. **Podemos hacer lo mismo con cualquier otro valor que esté almacenado en él, y también podemos guardar o cambiar valores.**

![](https://github.com/Ezzzzzzzzzzzzzz/Games-with-Pygame/blob/master/Part%204/Images/Diagrams/DictionariesAndLists.png)

Si el valor `player["y"]` es `20` y queremos cambiarlo a `25`, ingresaremos player ["y"] = 25, al igual que establecer cualquier otra variable. Los diccionarios son realmente útiles, porque nos permiten agrupar valores de una manera que es fácil de leer y de acceder con código. Si revisamos nuestro ejercicio mental de juego MMO, nos daremos cuenta rápidamente de que todavía necesitamos 100 variables para manejar a 100 jugadores, a pesar de que hemos hecho las cosas más ordenadas y más útiles. ¿Cuál es la mejor manera de realizar un seguimiento de los diccionarios? Ahí es donde entran las listas.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyNTc2NDc0MDQsNTkyNjg2NjkyLC0xOT
M3NDI5ODExLC0xOTM3NDI5ODExLC00MDEwMzg0MDgsLTEwOTgx
MDIwNzgsLTgxNjI2MTkzNiwxMTc1MjIwODcxXX0=
-->