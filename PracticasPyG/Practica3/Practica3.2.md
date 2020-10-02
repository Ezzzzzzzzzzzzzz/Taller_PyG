# ¿Cómo sabemos qué teclas se presionan y cuándo? 

En las practicas anterior, importamos `pygame.events` como `GAME_EVENTS`; ahora podemos usarlo. 

Cada programa de Pygame que escribimos es un gran bucle que se ejecuta para siempre o hasta que salimos del programa. Cada vez que se ejecuta nuestro ciclo, Pygame crea una lista de eventos que han ocurrido desde la última vez que se ejecutó el ciclo.

Esto incluye eventos del sistema, como una señal `QUIT`; *eventos del mouse*, *como un clic con el botón izquierdo*; y *eventos de teclado*, *como cuando se presiona o suelta un botón*. 

Una vez que tenemos la lista de eventos que recibió Pygame, podemos decidir cómo nuestro programa debe responder a esos eventos. 

**Si el usuario intenta salir, podríamos guardar el progreso del juego y cerrar la ventana en lugar de simplemente salir del programa, o podríamos mover un personaje cada vez que se presione una tecla**. 

Y eso es exactamente lo que hace `keyboard.py`.

- En la **línea 85**, creamos un bucle **for** que funcionará con cada evento en la lista que Pygame creó para nosotros. 
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
Los eventos están organizados en la lista en el orden en que los recibió Pygame. 

### En `keyboard.py`, buscamos principalmente eventos de teclado; podemos comprobar si un evento es o no un evento de teclado comprobando su propiedad **type** con `event.type`. 

### Si nuestro `event.type` es un evento `pygame.KEYDOWN`, sabemos que se presionó una tecla; si nuestro `event.type` es un evento `pygame.KEYUP`, sabemos que una tecla se ha liberado. 

Buscamos eventos `KEYDOWN` en la **línea 87** y eventos `KEYUP` en la **línea 93**. Primero buscamos eventos `KEYDOWN` porque la lógica lo dicta: **¡tienes que presionar una tecla hacia abajo antes de que vuelva a levantarse!**

## ¿Cómo sabemos qué tecla presionó nuestro jugador? 

Cada evento de las teclas de Pygame tiene una propiedad **key** que describe qué tecla representa. Si imprimiéramos la propiedad `event.key`, veríamos muchos números, pero estas no son las teclas que presionamos.

Los números que veríamos son códigos clave; son números que están vinculados de forma única a cada tecla de su teclado, y los programadores pueden usarlos para comprobar qué teclas representan. 

Por ejemplo, la tecla **ESC** de su teclado es **27**, la tecla **A** es **97** y la tecla **RETURN** es **13**. 

[Codigo ASCII](https://elcodigoascii.com.ar/codigos-ascii/letra-a-minuscula-codigo-ascii-97.html)







<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExNjkwNDk0NDIsMTY2NTMzMTUxMyw0NT
g3Nzg2MDUsOTExNDgxMDcyLDIwMzU2MzE4MzcsLTE2MDEyNzI3
NzRdfQ==
-->