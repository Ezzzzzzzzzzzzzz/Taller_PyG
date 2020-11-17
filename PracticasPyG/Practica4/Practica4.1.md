# El bucle "principal" del juego
Las líneas
```python 
def drawPlayer():

  pygame.draw.rect(surface, (255,0,0), (player["x"], player["y"], player["width"], player["height"]))

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

def createPlatform():

  global lastPlatform, platformDelay

  platformY = windowHeight
  gapPosition = random.randint(0, windowWidth - 40)

  gamePlatforms.append({"pos" : [0, platformY], "gap" : gapPosition})
  lastPlatform = GAME_TIME.get_ticks()

  if platformDelay > 800:
    platformDelay -= 50

def movePlatforms():
  # print("Platforms")

  for idx, platform in enumerate(gamePlatforms):

    platform["pos"][1] -= platformSpeed

    if platform["pos"][1] < -10:
      gamePlatforms.pop(idx)
      

def drawPlatforms():

  for platform in gamePlatforms:

    pygame.draw.rect(surface, (255,255,255), (platform["pos"][0], platform["pos"][1], windowWidth, 10))
    pygame.draw.rect(surface, (0,0,0), (platform["gap"], platform["pos"][1], 40, 10) )


def gameOver():
  global gameStarted, gameEnded

  platformSpeed = 0
  gameStarted = False
  gameEnded = True

def restartGame():

  global gamePlatforms, player, gameBeganAt, platformsDroppedThrough, platformDelay

  gamePlatforms = []
  player["x"] = windowWidth / 2
  player["y"] = 0
  gameBeganAt = GAME_TIME.get_ticks()
  platformsDroppedThrough = -1
  platformDelay = 2000

def quitGame():
  pygame.quit()
  sys.exit()
```

son donde vive la lógica de nuestro juego, **pero el estado de nuestro juego se controla en nuestro bucle principal entre las líneas**:

```python 
# 'main' loop
while True:

  surface.fill((0,0,0))

  for event in GAME_EVENTS.get():

    if event.type == pygame.KEYDOWN:

      if event.key == pygame.K_LEFT:
        leftDown = True
      if event.key == pygame.K_RIGHT:
        rightDown = True
      if event.key == pygame.K_ESCAPE:
        quitGame()

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT:
        leftDown = False
      if event.key == pygame.K_RIGHT:
        rightDown = False

      if event.key == pygame.K_SPACE:
        if gameStarted == False:
          restartGame()
          gameStarted = True

    if event.type == GAME_GLOBALS.QUIT:
      quitGame()

  if gameStarted is True:
    # Play game
    timer = GAME_TIME.get_ticks() - gameBeganAt

    movePlatforms()
    drawPlatforms()
    movePlayer()
    drawPlayer()

  elif gameEnded is True:
    # Draw game over screen
    surface.blit(game_over_image, (0, 150))

  else :
    # Welcome Screen
    surface.blit(title_image, (0, 150))

  if GAME_TIME.get_ticks() - lastPlatform > platformDelay:
    createPlatform()

  clock.tick(60)
  pygame.display.update()
```
Al igual que nuestros programas anteriores, en las líneas:

```python
  for event in GAME_EVENTS.get():

    if event.type == pygame.KEYDOWN:

      if event.key == pygame.K_LEFT:
        leftDown = True
      if event.key == pygame.K_RIGHT:
        rightDown = True
      if event.key == pygame.K_ESCAPE:
        quitGame()

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT:
        leftDown = False
      if event.key == pygame.K_RIGHT:
        rightDown = False

      if event.key == pygame.K_SPACE:
        if gameStarted == False:
          restartGame()
          gameStarted = True
```
 escuchamos varios eventos en el juego en nuestro bucle principal y cambios en función de los eventos enviados por nuestra computadora (teclado, mouse, eventos de salida, etc.). 

Las líneas:

```python
  if gameStarted is True:
    # Play game
    timer = GAME_TIME.get_ticks() - gameBeganAt

    movePlatforms()
    drawPlatforms()
    movePlayer()
    drawPlayer()

  elif gameEnded is True:
    # Draw game over screen
    surface.blit(game_over_image, (0, 150))

  else :
    # Welcome Screen
    surface.blit(title_image, (0, 150))
```

Son donde se determina el estado de nuestro juego y las funciones se llaman en consecuencia. Cada función está codificada para manejar un solo aspecto del juego independientemente de las otras funciones, pero deben llamarse en un orden determinado para asegurarnos de que nuestro juego se ejecuta como se espera. 

Para comprender cada función y aspecto de nuestro juego, vamos a trabajar con ellos en el orden en que los llama nuestro bucle principal.

**Cuando nuestro juego se ejecuta por primera vez, queremos mostrar nuestra pantalla de bienvenida que le dice a la gente que presione la barra espaciadora para comenzar.**

![](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica4/intro.JPG)

**Cuando el usuario presiona la barra espaciadora, queremos iniciar el juego y cuando el usuario es empujado fuera de la pantalla, queremos mostrar el juego sobre la pantalla y dejar que se reinicie.** 

![](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica4/gameover.JPG)

Todo esto se maneja en el bucle principal. Vamos a analizarlo.

## La pantalla para comenzar un juego

Cuando comienza nuestro juego, se nos presenta la pantalla de inicio del juego. Esta pantalla es una imagen simple que cargamos en la línea 
```python
title_image = pygame.image.load("assets/title.jpg")
```
de nuestra lista de códigos. En el otro extremo de nuestra lista, en la línea
```python
    # Welcome Screen
    surface.blit(title_image, (0, 150))
```
dibujamos esa imagen en nuestra superficie con [`blit()`](https://www.pygame.org/docs/ref/surface.html?highlight=blit#pygame.Surface.blit). Está en la declaración final `if-elif` de nuestro bucle principal. 

En la línea: 

```python 
if gameStarted is True:
    # Play game
    timer = GAME_TIME.get_ticks() - gameBeganAt

    movePlatforms()
    drawPlatforms()
    movePlayer()
    drawPlayer()

  elif gameEnded is True:
    # Draw game over screen
    surface.blit(game_over_image, (0, 150))

  else :
    # Welcome Screen
    surface.blit(title_image, (0, 150))
```
	
nuestro script comprueba si un juego ya está en marcha; si es así, comprobará el juego y renderizará la pantalla según sea necesario. Si no hay un juego en curso, el bucle verifica si un juego ha terminado o no en la línea:

```python
elif gameEnded is True:
    # Draw game over screen
    surface.blit(game_over_image, (0, 150))
```
en cuyo caso si queremos mostrar la puntuación del jugador en la pantalla de finalización del juego y ofrecerles la opción de volver a jugar. 

Si un juego no se ha iniciado ni terminado, podemos inferir que acabamos de iniciar el juego y, por lo tanto, podemos renderizar la pantalla de inicio. Para iniciar el juego, buscamos una barra espaciadora que presione el teclado en la línea:

```python
      if event.key == pygame.K_SPACE:
        if gameStarted == False:
          restartGame()
          gameStarted = True
```

Si un juego no se ha iniciado (o acaba de terminar), se llama a la función `restartGame` . Todo lo que hace esta función es restablecer todas las variables para un nuevo juego. 

```python
def restartGame():

  global gamePlatforms, player, gameBeganAt, platformsDroppedThrough, platformDelay

  gamePlatforms = []
  player["x"] = windowWidth / 2
  player["y"] = 0
  gameBeganAt = GAME_TIME.get_ticks()
  platformsDroppedThrough = -1
  platformDelay = 2000
```
Para que en el siguiente ciclo de nuestro bucle principal, la configuración estará en su lugar para un nuevo juego y se iniciará.


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTUzOTg1ODc3LC0xNzU0OTI2OTgyLC0xOD
A0OTQ1ODEyLDE1MTcxNzYxOCwxMzUzMjg2MzUxLDIwMTcxMDIx
MDUsMTkwMDQ4NDczNCw5MDI0MTc2NDFdfQ==
-->