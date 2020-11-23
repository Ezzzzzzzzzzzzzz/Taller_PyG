# Las plataformas de juego

Una vez que se ha presionado la barra espaciadora, comenzará un nuevo juego. Toda la lógica del juego está entre las líneas 40 y 146, pero llamamos a los métodos para generar el juego en las líneas:

```python
    movePlatforms()
    drawPlatforms()
    movePlayer()
    drawPlayer()
```
en un orden particular. 

### movePlatforms()

Primero, llamamos `movePlatforms()`, que funciona en todas las plataformas del juego y las mueve hacia arriba en la pantalla a la velocidad establecida con la variable `platformSpeed`. 

```python 
def movePlatforms():
  # print("Platforms")

  for idx, platform in enumerate(gamePlatforms):

    platform["pos"][1] -= platformSpeed  

    if platform["pos"][1] < -10:
      gamePlatforms.pop(idx) 
```

`movePlatforms` también comprueba si la plataforma ha alcanzado o no la parte superior de nuestra ventana de juego; si lo ha hecho, eliminará esa plataforma de nuestra lista de plataformas de juegos.

Puede notar que el bucle [`for`](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica4/bucleForPython.md) en la línea:

```python
for idx, platform in enumerate(gamePlatforms):
```
es un poco diferente de los que usamos en el pasado. A diferencia de la mayoría de los bucles `for` en Python, este pasa el índice del bucle con el valor `idx`.

```python
# Ejemplo
gameplatforms = [1,2,3,4]

for idx, platform in enumerate(gameplatforms):
    print('Clave:', idx, 'Valor:', platform)
```

Necesitamos este índice para poder eliminar la plataforma correcta de la lista de `gamePlatforms` de lo contrario, tendríamos que trabajar en la lista e intentar averiguar cuál se necesita ir cada vez, y eso no sería bueno para la velocidad de fotogramas. 

La función [`pop`](https://www.geeksforgeeks.org/python-list-pop/#:~:text=pop()%20is%20an%20inbuilt,or%20the%20given%20index%20value.&text=Parameter%20%3A,is%20popped%20out%20and%20removed.) elimina un elemento de una lista en un punto dado; si quisiéramos eliminar la segunda plataforma de la lista, por ejemplo, pasaríamos `gamePlatforms.pop(1)`; recuerde, las listas comienzan en 0, por lo que 1 es el segundo elemento de nuestra lista.

Una vez que hayamos determinado dónde deben ir las plataformas y cuáles deben desaparecer, podemos dibujarlas. 

### drawPlatforms()

Hacemos esto con `drawPlatforms`.

```python
def drawPlatforms():

  for platform in gamePlatforms:

    pygame.draw.rect(surface, (255,255,255), (platform["pos"][0], platform["pos"][1], windowWidth, 10))
    pygame.draw.rect(surface, (0,0,0), (platform["gap"], platform["pos"][1], 40, 10) )
```

Nada de lujos aquí; **simplemente estamos dibujando un rectángulo blanco que es el ancho de la pantalla, y luego un rectángulo negro para el espacio por el que el personaje puede pasar a la siguiente plataforma.**

Pero, ¿de dónde vienen estas plataformas? En la línea

```python 
  if GAME_TIME.get_ticks() - lastPlatform > platformDelay:
    createPlatform()
```
encontramos la respuesta. Pygame realiza un seguimiento de cuánto tiempo ha estado funcionando el juego con su función `get_ticks()`.

Queremos lanzar una plataforma cada 2 segundos entonces, en cada bucle, verificamos cuánto tiempo ha pasado desde que creamos una nueva plataforma restando el tiempo en que creamos una plataforma por última vez del tiempo actual del juego, al que accedemos con [`GAME_TIME.get_ticks()`](https://www.pygame.org/docs/ref/time.html#pygame.time.get_ticks). 

```python 
# milisegundos [1000 ms = 1 s]
platformDelay = 2000 
```
El tiempo de juego se registra en milisegundos, por lo que si han pasado 2000 milisegundos (1000 milisegundos = 1 segundo) desde que generamos una plataforma, es hora de crear una nueva; lo hacemos con `createPlatform`. 

### createPlatform()
```python
def createPlatform():

  global lastPlatform, platformDelay

  platformY = windowHeight
  gapPosition = random.randint(0, windowWidth - 40)

  gamePlatforms.append({"pos" : [0, platformY], "gap" : gapPosition})
  lastPlatform = GAME_TIME.get_ticks()

  if platformDelay > 800:
    platformDelay -= 50
```
Usamos global para decirle a nuestro código que queremos usar variables que existen en el alcance global, no crear nuevas con el mismo nombre en el alcance de la función. 

En las líneas:

```python
  global lastPlatform, platformDelay

  platformY = windowHeight
  gapPosition = random.randint(0, windowWidth - 40)
```
estamos creando variables que definirán la posición de la plataforma `platformY` (plataforma Y) y la ubicación del hueco a través del cual caer junto con ella `gapPosition` (Posición del hueco). 

### Queremos que nuestra plataforma se eleve siempre desde la parte inferior de la ventana, pero el espacio puede estar en cualquier punto a lo largo de la plataforma.

Así como rastrear jugadores se vuelve difícil, cuando tenemos muchos con que lidiar, lo mismo ocurre con nuestras plataformas. Generamos una plataforma cada 2 segundos y ese retraso es cada vez menor. Si has estado jugando durante más de un minuto, ¡habrás saltado a unas 100 plataformas! 

No podemos preprogramar todas las plataformas e incluso si pudiéramos, nuestro juego se volvería muy fácil después de un par de jugadas. 

La línea:
```python

```

es donde creamos nuestras nuevas plataformas. **Como cualquier lista, podemos agregarle nuevos elementos;** en Python, podemos hacer esto con [`.append()`](https://www.geeksforgeeks.org/append-extend-python/). En este caso, estamos creando un diccionario con todo lo que necesitamos para crear una plataforma, la posición de la plataforma (almacenada con la tecla pos) y la ubicación del hueco (almacenada con la tecla gap).


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTcxMzkwODUyLC01MDc2NjY5OTcsLTQyOD
EwNTE1OCwtMTM1MjQ4OTkzNywtNzgxODgxNzgxLC0zOTc3MTMz
MTYsMjAyNDU2MjAyOSwtMTU1ODIxMjIyNiwyNDk4NzE4MDYsLT
IwMzYwMjI0MTAsMzcxNTUzMDM0LC0xNzY5MzQ1MzU3LC0xNzkz
MTU4NDc0XX0=
-->