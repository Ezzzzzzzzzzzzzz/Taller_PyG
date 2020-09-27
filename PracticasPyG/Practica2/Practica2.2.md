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
    greenSquareX += 1
    #greenSquareY += 1
```

### **Comente la línea `greenSquareX` del `fragmento 02` y elimine el comentario de la línea de abajo quitando el `#`. Nuestro cuadrado comenzará a viajar hacia la parte inferior de la pantalla**. 

Al igual que antes, estamos cambiando la variable que le dice a nuestra forma a dónde ir, `greenSquareY`(tenga en cuenta que ahora estamos cambiando `Y`, no `X`), solo un poco cada vez para que se mueva. Y, tal como vimos al cambiar la variable `X`, **podemos hacer que el cuadrado verde suba agregando un número negativo**.

![https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica2/py2.3.JPG](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica2/py2.3.JPG)

Así que ahora podemos animar cosas que se mueven en cuatro direcciones; eso es suficiente libertad para hacer tantos juegos clásicos: [Pokémon](https://www.youtube.com/watch?v=s_4zaj8EbFI), [Legend Of Zelda](https://www.zelda.com/), [Space Invaders](https://elgoog.im/space-invaders/) y más. 

**Estos juegos solo moverían cosas horizontal y verticalmente, pero nunca al mismo tiempo**. 

![](https://media.giphy.com/media/xyKxclKcUXfaM/giphy.gif)

### **El próximo desafío sería cómo hacer que las cosas se muevan en diagonal.** Afortunadamente, este es un proceso bastante simple también.

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

**Eso significa que tenemos ocho direcciones en las que nuestros objetos pueden moverse, es decir, que usamos números que son enteros e iguales entre sí. Si utilizamos valores diferentes para nuestros valores `X` e `Y`, y utilizamos **flotantes** *(que son números con un decimal, como 2.3 o 3.141)* en lugar de **enteros** *(números enteros)*, podríamos lograr un movimiento completo de 360 grados.**

![https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica2/py2.4.JPG](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica2/py2.4.JPG)

Juguemos un poco más con números y decimales. Hasta ahora, los valores que hemos usado para animar nuestras formas en la pantalla han sido enteros que permanecen constantes. Con cada cuadro, siempre agregaríamos 1 (o algún otro valor arbitrario) para mover nuestro objeto. 

### Pero, **¿qué sucede si cambiamos los valores que usamos para animar cosas? ¿Qué pasa si, en lugar de agregar `1` a las coordenadas `X` / `Y`, agregamos `1`, luego `1.1`, luego `1.2`, y así sucesivamente?**

Reemplace el código del `fragmento 02` con el código del `fragmento 03` (o cree un nuevo archivo con el código `TOP (superior)` + `fragmento 03` + `BOTTOM`). **Ahora, si corremos eso, ¿qué vemos?**

### Fragmento 03
```python
blueSquareX = 0.0
blueSquareY = 0.0
blueSquareVX = 1
blueSquareVY = 1

while True:
	surface.fill((0, 0, 0))
	pygame.draw.rect(surface, (0, 0, 255), (blueSquareX, blueSquareY, 10, 10)
	blueSquareX += blueSquareVX
	blueSquareY += blueSquareVY
	blueSquareVX += 0.1
	blueSquareVY += 0.1
```
 Estamos agregando a nuestros valores X e Y, por lo que nuestro cuadrado se mueve hacia abajo y hacia la derecha, pero algo es diferente de nuestros bits de código anteriores: **a medida que nuestro programa continúa ejecutándose, nuestro cuadrado se mueve un poco más hacia la derecha de lo que hizo en los cuadros anteriores. Se está acelerando. Esto se debe a que utilizamos variables que almacenan una medida básica de velocidad.** 

Al usar una variable para agregar un valor a nuestras coordenadas X e Y, podemos aumentar la cantidad de distancia que se agrega en cada cuadro, lo que da la ilusión de aceleración. 

**Si cambiamos nuestro código para que aumente nuestras variables de velocidad (blueSquareVX / blueSquareVY en este caso) a través de la multiplicación en lugar de la suma o la resta, nuestras formas se acelerarían exponencialmente; apenas tendríamos tiempo para verlos antes de que salieran corriendo de la pantalla.**
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQyNDc2Mjk2OCwtNTczMzM5NDM2LDEwOT
Q3NjIzODgsLTM5NTgwODkwNywxMDE2OTc3NTYxLDE5NzY4Mjcx
MjUsMzcxNzA3Mzc3LDEzOTQ1ODk0NSwtNDM1NTA0NTk4LC0xOD
Y1NjY4ODE4LDk4MTUyMDA3NV19
-->