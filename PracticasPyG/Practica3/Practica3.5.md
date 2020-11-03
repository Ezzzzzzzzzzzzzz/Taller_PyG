# Pygame eventos del  mouse

El mouse es un kit simple, por lo que el código es mucho menos complicado que el código de nuestro teclado. Si copia `mouse.py` y lo ejecuta, verá un cuadrado rojo familiar en la parte inferior de la pantalla. 

Presionar las teclas del teclado no hará nada esta vez, porque este cuadrado es diferente. Si desea moverlo, debe usar el mouse para levantarlo.

Arrastre el mouse sobre el cuadrado, mantenga presionado el botón izquierdo del mouse y arrastre hacia arriba. Nuestro cuadrado se mueve con nuestro mouse. Si suelta el botón del mouse, el cuadrado volverá a la parte inferior de la ventana. Agradable y simple, pero **¿cómo funciona?**

# [mouse.py](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica3/mouse.py)

Esta vez, casi no tenemos ningún código en nuestro bucle `for` principal. Aquí solo estamos verificando si el primer botón del mouse ha sido presionado o no y luego llamamos a tres funciones: checkBounds (), checkGravity () y drawSquare (). En nuestro código keyboard.py, ponemos parte de nuestro código en funciones; esta vez se lo haremos a todos, pero llegaremos a ellos en un momento.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg1MDM5MzIxNiwtMjIzOTgxODM0XX0=
-->