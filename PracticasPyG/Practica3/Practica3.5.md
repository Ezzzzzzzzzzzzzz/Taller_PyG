#  Eventos del mouse en Pygame

El mouse es un kit simple, por lo que el código es mucho menos complicado que el código de nuestro teclado. Si copia `mouse.py` y lo ejecuta, verá un cuadrado rojo familiar en la parte inferior de la pantalla. 

Presionar las teclas del teclado no hará nada esta vez, porque este cuadrado es diferente. Si desea moverlo, debe usar el mouse para levantarlo.
![](https://media.giphy.com/media/111ebonMs90YLu/giphy.gif)
Arrastre el mouse sobre el cuadrado, mantenga presionado el botón izquierdo del mouse y arrastre hacia arriba. Nuestro cuadrado se mueve con nuestro mouse. Si suelta el botón del mouse, el cuadrado volverá a la parte inferior de la ventana. Agradable y simple, pero **¿cómo funciona?**

# [mouse.py](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica3/mouse.py)

Esta vez, casi no tenemos ningún código en nuestro bucle principal. 
```python 
while True:

    mousePosition = pygame.mouse.get_pos()
    surface.fill((0,0,0))

    # Compruebe si el mouse está presionado
    if pygame.mouse.get_pressed()[0] == True:
        mousePressed = True
    else:
        mousePressed = False

    checkBounds()
    checkGravity()
    drawSquare()

    clock.tick(60)
    pygame.display.update()

    for event in GAME_EVENTS.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quitGame()

        if event.type == GAME_GLOBALS.QUIT:
            quitGame()
```
**Aquí solo estamos verificando si el primer botón del mouse ha sido presionado o no** y luego llamamos a tres funciones: 
- `checkBounds()` (comprobar limites)
- `checkGravity()` (comprobar gravedad) 
- `drawSquare()` (dibuja el cuadrado). 

### Las dos cosas importantes que debemos saber al usar un mouse son dónde está y qué botones se presionaron, si los hay. 

Una vez que sepamos estas dos cosas, podemos hacer que las cosas sucedan. En primer lugar, vamos a averiguar dónde está el mouse, y lo haremos con:
```python
	mousePosition = pygame.mouse.get_pos()
``` 
A diferencia de nuestro `keynoard.py` no tenemos que trabajar en una lista de eventos y verificar si fueron eventos del mouse. 

En cambio, cuando llamamos a [`pygame.mouse.get_pos()`](https://www.pygame.org/docs/ref/mouse.html?highlight=get_pressed#pygame.mouse.get_pos) obtenemos una **tupla** con dos valores: **el valor actual de X e Y del mouse dentro de la ventana**.

Ahora que sabemos dónde está el mouse, todo lo que tenemos que hacer es determinar si se presionó alguno de los botones:
```python  
	# Compruebe si el mouse está presionado
    if pygame.mouse.get_pressed()[0] == True: # boton izquierdo
        mousePressed = True
    else:
        mousePressed = False
```
### `pygame.mouse.get_pressed()`devuelve una tupla de tres valores: el primero es para el botón izquierdo del mouse, el segundo para el botón central del mouse y el tercero para el botón derecho del mouse.

Si se presiona el botón, el valor es **Verdadero / True**; de lo contrario, es **Falso / False**. 

No estamos haciendo nada con el botón central o derecho del mouse, por lo que simplemente podemos verificar el primer valor (el botón izquierdo del mouse) con [`pygame.mouse.get_pressed()[0]`](https://www.pygame.org/docs/ref/mouse.html?highlight=get_pressed#pygame.mouse.get_pressed).

![](https://media.geeksforgeeks.org/wp-content/uploads/CommonArticleDesign1-min.png)

### Si `pygame.mouse.get_pressed()[0]` es **True**, entonces nuestro jugador ha hecho clic en un botón y podemos continuar. 

En este caso, establecemos `mousePressed` en **True**, tal como lo hicimos con `leftDown` y `rightDown` en `keyboard.py`, para que podamos usarlo en todo nuestro programa.


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2Mjc5MDA4MzQsLTE3MDY5ODU5NDMsMT
AwNjk5Mjk3NiwxMTcyOTkwOCwxNDMzNzcxNTQ2LDczNTI3MzY3
NywtMTE0NTU2NDk5MCwtMTY4OTQ3NjAyOCwtMTk2OTkyNTIxMC
wyMzM3NDU1NTgsODkzNDI2MTI0LDI3NTExNTI1MSwtMjIzOTgx
ODM0XX0=
-->