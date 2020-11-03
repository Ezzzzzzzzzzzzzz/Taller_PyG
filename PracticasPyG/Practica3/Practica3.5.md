# Pygame eventos del  mouse

El mouse es un kit simple, por lo que el código es mucho menos complicado que el código de nuestro teclado. Si copia `mouse.py` y lo ejecuta, verá un cuadrado rojo familiar en la parte inferior de la pantalla. 

Presionar las teclas del teclado no hará nada esta vez, porque este cuadrado es diferente. Si desea moverlo, debe usar el mouse para levantarlo.

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
**Aquí solo estamos verificando si el primer botón del mouse ha sido presionado o no** y luego llamamos a tres funciones: `checkBounds()` (comprobar limites), `checkGravity()` (comprobar gravedad) y `drawSquare()` (dibuja el cuadrado). 

En nuestro código `keyboard.py`, ponemos parte de nuestro código en funciones; esta vez se lo haremos a todos, pero llegaremos a ellos en un momento.

Las dos cosas importantes que debemos saber al usar un mouse son dónde está y qué botones, si los hay, se presionaron. Una vez que sepamos estas dos cosas, podemos hacer que las cosas sucedan. En primer lugar, vamos a averiguar dónde está el mouse, y lo haremos en la línea 76 con pygame.mouse.get_pos ().
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4MjExMDk4MTcsMjc1MTE1MjUxLC0yMj
M5ODE4MzRdfQ==
-->