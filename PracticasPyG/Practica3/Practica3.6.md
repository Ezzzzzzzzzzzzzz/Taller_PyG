# Comprobando el cuadrado

Ahora que sabemos dónde está nuestro mouse y qué botones están presionados, podemos hacer algo con esa información. 

Inmediatamente después de nuestro código que verifica los botones de nuestro mouse, llamamos `checkBounds()`. 
```python
def checkBounds():

    global squareColor, squareX, squareY, draggingSquare

    if mousePressed == True:
        # ¿Esta nuestro cursor sobre el cuadrado?
        if mousePosition[0] > squareX and mousePosition[0] < squareX + squareSize:

            if mousePosition[1] > squareY and mousePosition[1] < squareY + squareSize:

                draggingSquare = True
                pygame.mouse.set_visible(0)

    else:
        squareColor = (255,0,0)
        pygame.mouse.set_visible(1)
        draggingSquare = False
```
### `checkBounds()` tiene un trabajo: verificar si la posición de nuestro mouse está o no dentro de los límites (bordes) de nuestro cuadrado.

Si estuviéramos haciendo un juego completo, esta función probablemente verificaría la posición de cada objeto del juego con las coordenadas del mouse, pero en este ejemplo solo estamos interesados en nuestro cuadrado rojo.

La línea:
```python 
    if mousePressed == True:
```
verifica si se ha presionado el botón del mouse o no; después de todo, no tiene sentido verificar dónde está nuestro mouse si no está haciendo nada. 

Si se ha presionado el botón de nuestro mouse:
```python 
        # ¿Esta nuestro cursor sobre el cuadrado?
        if mousePosition[0] > squareX and mousePosition[0] < squareX + squareSize:
```
 miramos dónde está la coordenada X del mouse y la comparamos con la coordenada X de nuestro cuadrado.
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjcyMTA4NDkxLC03MTg1OTA3MDNdfQ==
-->