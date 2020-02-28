# Moviéndose en todas direcciones
### Código TOP (Cabecera)
```python
import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()
windowWidth = 640
windowHeight = 480
surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Pygame Shapes!")
```
### Código BOTTOM (Pie de código)
```python
for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
```
### Fragmento 02
```python
greenSquareX = windowWidth / 2
greenSquareY = windowHeight / 2

while True:
    surface.fill((0, 0, 0))
    pygame.draw.rect(surface, (0, 255, 0), (greenSquareX, greenSquareY, 10, 10))
    greenSquareX += 0.01
    #greenSquareY += 0.01
```

**Comente la línea `greenSquareX` del `fragmento 02` y elimine el comentario de la línea de abajo quitando el `#`**. Nuestro cuadrado comenzará a viajar hacia la parte inferior de la pantalla. Al igual que antes, estamos cambiando la variable que le dice a nuestra forma a dónde ir, `greenSquareY`(tenga en cuenta que ahora estamos cambiando `Y`, no `X`), solo un poco cada vez para que se mueva. Y, tal como vimos al cambiar la variable `X`, **podemos hacer que el cuadrado verde suba agregando un número negativo**.

Así que ahora podemos animar cosas que se mueven en cuatro direcciones; eso es suficiente libertad para hacer tantos juegos clásicos: [Pokémon](https://www.youtube.com/watch?v=s_4zaj8EbFI), [Legend Of Zelda](https://www.zelda.com/), [Space Invaders](https://elgoog.im/space-invaders/) y más. **Estos juegos solo moverían cosas horizontal y verticalmente, pero nunca al mismo tiempo**. 

![](https://media.giphy.com/media/xyKxclKcUXfaM/giphy.gif)

**El próximo desafío sería cómo hacer que las cosas se muevan en diagonal.** Afortunadamente, este es un proceso bastante simple también.

> Si **descomentamos** `greenSquareX` y `greenSquareY` en nuestro código, nuestra forma se moverá hacia la derecha y hacia abajo cada vez que Pygame actualice la pantalla. 
>
>Si **sumamos a nuestros valores** `X` e `Y`, **nuestras formas se moverán hacia la derecha y hacia abajo**. 
>
>Si **sumamos** a nuestro valor `X` y **restamos** de nuestro valor `Y`, **nuestras formas se moverán hacia la derecha y hacia arriba**. 
>
>Si **restamos** de nuestro valor `X` y **sumamos** a nuestro valor `Y`, **nuestras formas se moverán hacia la izquierda y hacia abajo**. 
>
>Finalmente, si **restamos nuestros valores** `X` e `Y`, **nuestra forma se moverá hacia la izquierda y hacia arriba**. 

![https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica2/Py2.2.JPG](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica2/Py2.2.JPG)

Eso significa que tenemos ocho direcciones en las que nuestros objetos pueden moverse, es decir, que usamos números que son enteros e iguales entre sí. Si utilizamos valores diferentes para nuestros valores `X` e `Y`, y utilizamos **flotantes** *(que son números con un decimal, como 2.3 o 3.141)* en lugar de **enteros** *(números enteros)*, podríamos lograr un movimiento completo de 360 grados.

 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyNzE4MzM2MTgsOTgxNTIwMDc1XX0=
-->