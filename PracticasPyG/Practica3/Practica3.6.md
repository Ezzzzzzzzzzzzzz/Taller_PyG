# Comprobando el cuadrado

Ahora que sabemos dónde está nuestro mouse y qué botones están presionados, podemos hacer algo con esa información. 

Inmediatamente después de nuestro código que verifica los botones de nuestro mouse, llamamos `checkBounds()`. 
```python
	 # Compruebe si el mouse está presionado
    if pygame.mouse.get_pressed()[0] == True: # [(0)bot_izq,(1)bot_central,(2)bot_derecho]
        mousePressed = True
    else:
        mousePressed = False

    checkBounds()

```
### `checkBounds()` tiene un trabajo: verificar si la posición de nuestro mouse está o no dentro de los límites (bordes) de nuestro cuadrado.

Si estuviéramos haciendo un juego completo, esta función probablemente verificaría la posición de cada objeto del juego con las coordenadas del mouse, pero en este ejemplo solo estamos interesados en nuestro cuadrado rojo.
<!--stackedit_data:
eyJoaXN0b3J5IjpbNTc1NDExNzI2LC03MTg1OTA3MDNdfQ==
-->