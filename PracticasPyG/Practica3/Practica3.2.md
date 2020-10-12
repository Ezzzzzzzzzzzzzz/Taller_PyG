# ¿Cómo sabemos qué teclas se presionan y cuándo? 
![](https://media.giphy.com/media/3oEduLvxnhDsh83j3O/giphy.gif) 

### En las practicas anterior, importamos `pygame.events` como `GAME_EVENTS`; ahora podemos usarlo. 

**Cada programa de Pygame que escribimos es un gran bucle que se ejecuta para siempre o hasta que salimos del programa**. Cada vez que se ejecuta nuestro ciclo, Pygame crea una lista de eventos que han ocurrido desde la última vez que se ejecutó el ciclo. Esto incluye eventos del sistema, como una señal `QUIT`; *eventos del mouse [como un clic con el botón izquierdo]*; y *eventos de teclado [como cuando se presiona o suelta un botón]*. 

Una vez que tenemos la lista de eventos que recibió Pygame, podemos decidir cómo nuestro programa debe responder a esos eventos. 

### Si el usuario intenta salir, podríamos guardar el progreso del juego y cerrar la ventana en lugar de simplemente salir del programa, o podríamos mover un personaje cada vez que se presione una tecla. 

- En la **línea 85**, creamos un bucle **for** que funcionará con cada evento en la lista que Pygame creó para nosotros. 
```python
for event in GAME_EVENTS.get():
```
Los eventos están organizados en la lista en el orden en que los recibió Pygame. 

### En `keyboard.py`, buscamos principalmente eventos de teclado; podemos comprobar si un evento es o no un evento de teclado comprobando su propiedad `type` con `event.type`. 


### Si nuestro `event.type` es un evento `pygame.KEYDOWN`, sabemos que se presionó una tecla; 

```python
if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                leftDown = True
            if event.key == pygame.K_RIGHT:
                rightDown = True
            if event.key == pygame.K_UP:
                if not haveJumped:
                    haveJumped = True
                    playerVY += jumpHeight
            if event.key == pygame.K_ESCAPE:
                quitGame()
```

### Si nuestro `event.type` es un evento `pygame.KEYUP`, sabemos que una tecla se ha liberado. 
```python
if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                leftDown = False
                playerVX = moveSpeed
            if event.key == pygame.K_RIGHT:
                rightDown = False
                playerVX = moveSpeed
```

Primero buscamos eventos `KEYDOWN` porque la lógica lo dicta: **¡tienes que presionar una tecla hacia abajo antes de que vuelva a levantarse!**


```python
# Obtenga una lista de todos los eventos que sucedieron desde el último rediseño
    for event in GAME_EVENTS.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                leftDown = True
            if event.key == pygame.K_RIGHT:
                rightDown = True
            if event.key == pygame.K_UP:
                if not haveJumped:
                    haveJumped = True
                    playerVY += jumpHeight
            if event.key == pygame.K_ESCAPE:
                quitGame()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                leftDown = False
                playerVX = moveSpeed
            if event.key == pygame.K_RIGHT:
                rightDown = False
                playerVX = moveSpeed

        if event.type == GAME_GLOBALS.QUIT:
            quitGame()
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwMzk3MDgyNjMsLTE1NTYyODAwMSwxOD
cwODMwOTUwLC0yMzEwNDE1MTYsOTcwMTQzMzc5LC04MDk5NzM5
MTIsMzYwODQ3NjA0LDE2NjUzMzE1MTMsNDU4Nzc4NjA1LDkxMT
Q4MTA3MiwyMDM1NjMxODM3LC0xNjAxMjcyNzc0XX0=
-->