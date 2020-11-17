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

Puede notar que el bucle `for` en la línea 
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

La función `pop` elimina un elemento de una lista en un punto dado; si quisiéramos eliminar la segunda plataforma de la lista, por ejemplo, pasaríamos `gamePlatforms.pop(1)`; recuerde, las listas comienzan en 0, por lo que 1 es el segundo elemento de nuestra lista.

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

Pero, ¿de dónde vienen estas plataformas? En la línea 196, encontramos la respuesta. Pygame realiza un seguimiento de cuánto tiempo ha estado funcionando el juego con su función `get_ticks()`.

```python 
  if GAME_TIME.get_ticks() - lastPlatform > platformDelay:
    createPlatform()
```

Queremos lanzar una plataforma cada 2 segundos; entonces, en cada bucle, verificamos cuánto tiempo ha pasado desde que creamos una nueva plataforma restando el tiempo en que creamos una plataforma por última vez del tiempo actual del juego, al que accedemos con [`GAME_TIME.get_ticks()`](https://www.pygame.org/docs/ref/time.html#pygame.time.get_ticks).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTc2MzEzMzEyMCwyMDI0NTYyMDI5LC0xNT
U4MjEyMjI2LDI0OTg3MTgwNiwtMjAzNjAyMjQxMCwzNzE1NTMw
MzQsLTE3NjkzNDUzNTcsLTE3OTMxNTg0NzRdfQ==
-->