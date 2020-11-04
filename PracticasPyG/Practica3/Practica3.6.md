# Comprobando el cuadrado

Ahora que sabemos dónde está nuestro mouse y qué botones están presionados, podemos hacer algo con esa información. 

Inmediatamente después de nuestro código que verifica los botones de nuestro mouse, llamamos `checkBounds()`. 

### checkBounds
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
**verifica si se ha presionado el botón del mouse o no**; después de todo, no tiene sentido verificar dónde está nuestro mouse si no está haciendo nada. 

### Si se ha presionado el botón de nuestro mouse miramos dónde está la coordenada X del mouse y la comparamos con la coordenada X de nuestro cuadrado.
```python 
        # ¿Esta nuestro cursor sobre el cuadrado?
        if mousePosition[0] > squareX and mousePosition[0] < squareX + squareSize:
```
### Si nuestro mouse X es mayor que la izquierda de nuestro cuadrado y es más pequeño que el valor X de la derecha de nuestro cuadrado (`squareX + squareSize`), sabemos que nuestro mouse está dentro de los límites X de nuestro cuadrado, pero eso no significa que está dentro de nuestra forma.

Antes de hacer algo con su mouse, debemos verificar que la coordenada Y de su mouse también esté dentro de nuestro cuadrado.

```python
	if mousePosition[1] > squareY and mousePosition[1] < squareY + squareSize:
```

### Si el valor Y de nuestro mouse es mayor que la parte superior de nuestra forma y menor que la parte inferior, entonces podemos estar seguros de que nuestro mouse está en algún lugar dentro de nuestra forma. 

![](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica3/mousecontrol.jpg)

En `mouse.py`, **hemos verificado las coordenadas X e Y en líneas separadas; podríamos haber hecho esto en una sola línea, pero sería una línea bastante intimidante para leer**, y mucho menos para escribir. 

Ahora que sabemos que nuestro mouse está posicionado dentro de nuestro cuadrado y que hemos presionado el botón del mouse, podemos establecer nuestra variable `draggingSquare` (arrastrando el cuadrado) en **True**.

```python 
if mousePressed == True:
        # ¿Esta nuestro cursor sobre el cuadrado?
        if mousePosition[0] > squareX and mousePosition[0] < squareX + squareSize:
            if mousePosition[1] > squareY and mousePosition[1] < squareY + squareSize:
                draggingSquare = True
                pygame.mouse.set_visible(0) # Ajusta la visibilidad del puntero a 0 (desaparece)
```
Una vez que `checkBounds()` ha hecho su trabajo, `checkGravity()` se pone a trabajar. 

### checkGravity()

### Al igual que en `keyboard.py`, `checkGravity()` mira dónde está nuestro cuadrado en la ventana: si no está en la parte inferior de nuestra ventana, acelerará nuestro cuadrado hasta allí. 

Sin embargo, solo hará esto si dejamos ir el botón del mouse, porque no queremos que nuestra forma caiga al suelo cuando la sujetemos.

```python 

```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjY3ODM1MjUyLC0xMzI1ODcwMzc4LC0xNT
c3MTg5MDQ1LC00NjMyMDM4OTksNTUwOTI5MjM0LC03MTg1OTA3
MDNdfQ==
-->