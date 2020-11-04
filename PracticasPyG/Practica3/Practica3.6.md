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
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5MDE1MjY3NzQsLTcxODU5MDcwM119
-->