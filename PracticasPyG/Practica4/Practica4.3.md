# Moviendo tu avatar

![](https://media.giphy.com/media/uR6julmSW90mk/giphy.gif)

Nuestro avatar no es una construcción complicada: en su forma más simple, es un rectángulo rojo. Una vez dibujadas nuestras plataformas, queremos averiguar dónde puede ir nuestro avatar. 

### movePlayer()
```python
def movePlayer():
  
  global platformsDroppedThrough, dropping

  leftOfPlayerOnPlatform = True
  rightOfPlayerOnPlatform = True

  if surface.get_at(( int(player["x"]), int(player["y"]) + player["height"])) == (0,0,0,255):
    leftOfPlayerOnPlatform = False

  if surface.get_at(( int(player["x"]) + player["width"], int(player["y"]) + player["height"])) == (0,0,0,255):
    rightOfPlayerOnPlatform = False

  if leftOfPlayerOnPlatform is False and rightOfPlayerOnPlatform is False and (player["y"] + player["height"]) + player["vy"] < windowHeight:
    player["y"] += player["vy"]

    if dropping is False:
      dropping = True
      platformsDroppedThrough += 1

  else :

    foundPlatformTop = False
    yOffset = 0
    dropping = False

    while foundPlatformTop is False:

      if surface.get_at(( int(player["x"]), ( int(player["y"]) + player["height"]) - yOffset )) == (0,0,0,255):
        player["y"] -= yOffset
        foundPlatformTop = True
      elif (player["y"] + player["height"]) - yOffset > 0:
        yOffset += 1
      else :

        gameOver()
        break

  if leftDown is True:
    if player["x"] > 0 and player["x"] - 5 > 0:
      player["x"] -= 5
    elif player["x"] > 0 and player["x"] - 5 < 0:
      player["x"] = 0

  if rightDown is True:
    if player["x"] + player["width"] < windowWidth and (player["x"] + player["width"]) + 5 < windowWidth:
      player["x"] += 5
    elif player["x"] + player["width"] < windowWidth and (player["x"] + player["width"]) + 5 > windowWidth:
      player["x"] = windowWidth - player["width"]
```
Como verá, la función `movePlayer()` en las líneas es el hogar de la mayor parte de la lógica de nuestro juego. Antes de mirar el código, hablemos de lo que está sucediendo: 

- Queremos que nuestro jugador caiga cuando haya una brecha en la plataforma o no haya ninguna plataforma. 
- También queremos que el avatar suba con la plataforma si no hay un hueco presente. 

Para codificar esta lógica, podríamos verificar la posición de todas las plataformas en cada fotograma y escribir un código que averigüe si nuestro avatar está o no en la parte superior de una plataforma o no, pero eso realmente hará que nuestra computadora trabaje duro y no sería eficiente.

**En cambio, estamos haciendo algo más simple: nuestras plataformas son siempre blancas y nuestro fondo siempre es negro, por lo que si podemos saber el color del píxel justo debajo de nuestro avatar, podemos determinar si necesitamos o no soltar. También debemos verificar que nuestro avatar esté completamente fuera del borde de nuestra plataforma antes de dejarlo caer.** 

Para hacer esto, verificamos los valores justo debajo de nuestro avatar, tanto a la izquierda como a la derecha. Podemos obtener el color de un píxel en un punto determinado con [`surface.get_at((X, Y))`](https://www.pygame.org/docs/ref/surface.html?highlight=get_at#pygame.Surface.get_at); esto devolverá una tupla con cuatro valores `(ROJO, VERDE, AZUL, OPACIDAD)`, cada uno entre **0** y **255**, como si hubiéramos establecido los colores nosotros mismos. 

En las líneas:
```python
if surface.get_at(( int(player["x"]), int(player["y"]) + player["height"])) == (0,0,0,255):
    leftOfPlayerOnPlatform = False
```
 verificamos el color debajo de la parte inferior izquierda de nuestro avatar, y en las líneas:
```python
  if surface.get_at(( int(player["x"]) + player["width"], int(player["y"]) + player["height"])) == (0,0,0,255):
    rightOfPlayerOnPlatform = False
```
hacemos lo mismo para la parte inferior derecha. 

Si los valores de color que encontramos en la parte inferior izquierda o inferior derecha del avatar son **(255,255,255,255) (blanco)**, entonces sabemos que al menos un borde de nuestro avatar todavía está en una plataforma. **Si ambos son cualquier cosa menos blancos**, entonces hay un espacio en la plataforma o estamos en un espacio en blanco, por lo que podemos dejar caer nuestro avatar. 

Todo esto sucede en las líneas: 
```python
if leftOfPlayerOnPlatform is False and rightOfPlayerOnPlatform is False and (player["y"] + player["height"]) + player["vy"] < windowHeight:
    player["y"] += player["vy"]

    if dropping is False:
      dropping = True
      platformsDroppedThrough += 1
```
También comprobamos que no dejamos que nuestro avatar se escape por la parte inferior de nuestra ventana.

Entonces, ese es el código que maneja qué hacer si no estamos en la cima de una plataforma, pero ¿qué pasa cuando queremos que nuestro avatar viaje con la plataforma? Si nuestro avatar no puede bajar, debemos averiguar dónde termina la plataforma y dónde comienza su espacio en blanco. 

Hacemos esto en las líneas:

```python
else:
    foundPlatformTop = False
    yOffset = 0
    dropping = False
```
Establecemos dos variables, `foundPlatformTop` y `yOffset`; Usamos estos valores para ayudar a nuestro bucle `while` en las líneas:

```python 
    while foundPlatformTop is False:

      if surface.get_at(( int(player["x"]), ( int(player["y"]) + player["height"]) - yOffset )) == (0,0,0,255):
        player["y"] -= yOffset
        foundPlatformTop = True
      elif (player["y"] + player["height"]) - yOffset > 0:
        yOffset += 1
      else:
        gameOver()
        break
```
**Cuando encontramos un píxel blanco debajo de la parte inferior izquierda o derecha de nuestro avatar, tenemos que trabajar hacia atrás (negativo) para mover nuestro avatar hacia arriba con la plataforma**. Nuestro bucle `while` resta 1 de nuestro valor `player[“y”]` y comprueba el color que encuentra allí. 
```python
        player["y"] -= yOffset
        foundPlatformTop = True
```
Recuerde, aún no hemos dibujado nuestro avatar, por lo que los únicos colores en nuestra superficie son el negro (fondo) o el blanco (plataformas). 

![](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica4/1erVideojuego.png)

Si las coordenadas marcadas son blancas, se agrega 1 al `yOffset` y el bucle `while` continúa buscando un píxel negro. Hará esto hasta que encuentre un píxel negro sobre la coordenada x de nuestro avatar, agregando 1 a la variable `yOffset` cada vez. Una vez que se encuentra un píxel negro, descubrimos dónde termina nuestra plataforma y podemos restar el `yOffset` del `player["y"]` para poner nuestro avatar justo encima de la plataforma; esto se hace en la línea:
```python
      elif (player["y"] + player["height"]) - yOffset > 0:
        yOffset += 1
```
**Si no encontramos un píxel negro antes de llegar a la parte superior de la superficie, se acabó el juego: nuestro avatar está atrapado fuera de la pantalla.**
```python 
 else:
        gameOver()
        break
```
Mover nuestro personaje de izquierda a derecha se hace en las líneas:
```python


```
Si el código te resulta familiar, es porque lo usamos en nuestro último tutorial para mover nuestros cuadrados. Ahora que hemos descubierto dónde puede ir nuestro avatar, podemos dibujarlo llamando a `drawPlayer()` en la línea 203.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTM4OTIzNjc1MywtMTM2ODMxMjE4NywtMT
I2ODE1MTE3LC01NjE5NTgwMDQsMjU4NjE0NjU3LDM1NzIyMzA3
NCwtMTA0ODM3MjE5MywtMTAyMTIyMTM5MSwtOTg3MjE2MTY4LC
05NTYxMjA4NiwxMDk0Njg5NDk0LC0yNTk2MTk0NDksMTM0OTIw
NDY4NV19
-->