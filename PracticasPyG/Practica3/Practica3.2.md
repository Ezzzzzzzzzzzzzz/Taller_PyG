# ¿Cómo sabemos qué teclas se presionan y cuándo? 

En las practicas anterior, importamos `pygame.events` como `GAME_EVENTS`; ahora podemos usarlo. 

**Cada programa de Pygame que escribimos es un gran bucle que se ejecuta para siempre o hasta que salimos del programa**. Cada vez que se ejecuta nuestro ciclo, Pygame crea una lista de eventos que han ocurrido desde la última vez que se ejecutó el ciclo.

Esto incluye eventos del sistema, como una señal `QUIT`; *eventos del mouse [como un clic con el botón izquierdo]*; y *eventos de teclado [como cuando se presiona o suelta un botón]*. 

Una vez que tenemos la lista de eventos que recibió Pygame, podemos decidir cómo nuestro programa debe responder a esos eventos. 

### Si el usuario intenta salir, podríamos guardar el progreso del juego y cerrar la ventana en lugar de simplemente salir del programa, o podríamos mover un personaje cada vez que se presione una tecla. 

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

- En las **líneas 89**, **91**, **93** y **97**, usamos `pygame.K_LEFT`, `pygame.K_RIGHT`, `pygame.K_UP` y `pygame.K_ESCAPE` para verificar si alguna de las teclas presionadas son teclas que estamos buscando. 

**Una vez que sabemos que se presionó una tecla y qué tecla fue, podemos escribir código para afectar nuestro programa de maneras específicas.**

**Por ejemplo**, si se ha presionado la *tecla de flecha izquierda*, podemos mover nuestro reproductor a la izquierda con ``playerX -= 5``, pero no lo hemos hecho aquí. 
**¿Por qué no?** Pygame no emite eventos duplicados para presionar teclas, por lo que si mantenemos presionada una tecla para mantener nuestro cuadrado moviéndose hacia la izquierda, no pasaría nada. Nuestro cuadrado se movería la primera vez que Pygame detectara la pulsación de una tecla, pero luego se detendría hasta que volviéramos a pulsar el botón. Esto está destinado a ayudar a prevenir situaciones en las que presionar varias teclas podría fallar en nuestros juegos o dar a un jugador una ventaja injusta, pero no nos ayuda mucho cuando se trata de crear juegos con movimientos suaves. Entonces, ¿cómo solucionamos esto? Cada vez que detectamos una pulsación de tecla, en lugar de realizar una acción, como mover nuestro cuadrado, establecemos una variable.




<!--stackedit_data:
eyJoaXN0b3J5IjpbNjQ4Mjg5MTE0LDk3MDE0MzM3OSwtODA5OT
czOTEyLDM2MDg0NzYwNCwxNjY1MzMxNTEzLDQ1ODc3ODYwNSw5
MTE0ODEwNzIsMjAzNTYzMTgzNywtMTYwMTI3Mjc3NF19
-->