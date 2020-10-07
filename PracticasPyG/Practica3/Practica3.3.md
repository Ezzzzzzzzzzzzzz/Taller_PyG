# ¿Cómo sabemos qué tecla presionó nuestro jugador? 

### Cada evento de las teclas de Pygame tiene una propiedad  `key` que describe qué tecla representa. Si imprimiéramos la propiedad `event.key`, veríamos muchos números, pero estas no son las teclas que presionamos.

![](https://media.giphy.com/media/kD7SCW1rF6FFK/giphy.gif)

Los números que veríamos son códigos clave; son números que están vinculados de forma única a cada tecla de su teclado, y los programadores pueden usarlos para comprobar qué teclas representan. 

Por ejemplo, la tecla **ESC** de su teclado es **27**, la tecla **A** es **97** y la tecla **RETURN** es **13**. 

[Codigo ASCII](https://elcodigoascii.com.ar/codigos-ascii/letra-a-minuscula-codigo-ascii-97.html)

- En las **líneas 89**, **91**, **93** y **97**, usamos `pygame.K_LEFT`, `pygame.K_RIGHT`, `pygame.K_UP` y `pygame.K_ESCAPE` para verificar si alguna de las teclas presionadas son teclas que estamos buscando. 

**Una vez que sabemos que se presionó una tecla y qué tecla fue, podemos escribir código para afectar nuestro programa de maneras específicas.**

**Por ejemplo**, si se ha presionado la *tecla de flecha izquierda*, podemos mover nuestro reproductor a la izquierda con ``playerX -= 5``, **pero no lo hemos hecho aquí**. 

```python 
# Muevete a la izquierda
    if leftDown:
        #Si ya nos estamos moviendo hacia la derecha, restablezca la velocidad de movimiento e invierta la dirección
        if playerVX > 0.0: 
            playerVX = moveSpeed
            playerVX = -playerVX    
        # Asegúrate de que nuestro cuadrado no deje nuestra ventana a la izquierda.
        if playerX > 0:
            playerX += playerVX 
```

**¿Por qué no?** Pygame no admite eventos duplicados para presionar teclas, por lo que si mantenemos presionada una tecla para mantener nuestro cuadrado moviéndose hacia la izquierda, no pasaría nada. 

Nuestro cuadrado se movería la primera vez que Pygame detectara la pulsación de una tecla, pero luego se detendría hasta que volviéramos a pulsar el botón. *Esto está destinado a ayudar a prevenir situaciones en las que presionar varias teclas podría fallar en nuestros juegos o dar a un jugador una ventaja injusta, pero no nos ayuda mucho cuando se trata de crear juegos con movimientos suaves.* 

**¿Cómo solucionamos esto?** Cada vez que detectamos una pulsación de tecla, en lugar de realizar una acción, como mover nuestro cuadrado, establecemos una variable.




<!--stackedit_data:
eyJoaXN0b3J5IjpbLTMwODEwNjIzOCwxMDQ4MTM1NDE0LDE1OD
g4NTAyNjYsLTEwNjAzNTY0NzJdfQ==
-->