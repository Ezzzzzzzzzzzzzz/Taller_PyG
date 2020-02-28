# Animación de SHAPES (Formas) & PATHS (Trayectorias)

## Moviendo SHAPES en el tiempo y el espacio

Cuando pensamos en la animación, nuestras mentes pueden convertir dibujos en películas animadas: aquí, cambios sutiles en la forma y el color engañan a nuestros cerebros para que vean movimientos donde no los hay. 
**No es diferente con las computadoras:** cada vez que mueves un mouse o minimizas una ventana, nada se ha movido; en cambio, **los píxeles se han dibujado, actualizado, actualizado y luego dibujado nuevamente, con todo en su nuevo lugar.**

![](https://media.giphy.com/media/YTEAn0boXGmY0/giphy.gif)

## Algunas cosas que notar
A partir de ahora, vamos a incluir `pygame.locals`y las `pygame.events` de Pygame. 
Estas son variables especiales que Pygame incluye para ayudarnos a escribir código más legible, así como eliminar parte de la complejidad de interactuar con el sistema en el que ejecutamos nuestro código.

>`pygame.locals` contiene principalmente propiedades que describen el sistema y el estado del juego, por lo que lo llamamos **GAME_GLOBALS** para reflejar esto.
```python
import pygame.locals as GAME_GLOBALS
```
> 
>`pygame.events` incluye una lista de eventos, como eventos de teclado o eventos del sistema que ocurrieron desde la última vez que Pygame actualizó su vista; por eso lo importamos como **GAME_EVENTS**.
```python
import pygame.event as GAME_EVENTS
```

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
Lo v**Vamos a usar en el código `Bottom` para verificar si nuestro jugador intentó o no abandonar el juego mientras se estaba ejecutando (en este caso, tratando de cerrar la ventana), y luego cerrar nuestro programa correctamente.**

### Código BOTTOM (Pie de código)
```python
for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
```
Si ejecuta el código `Fragmento 01` (coloque el código `TOP` y el `Fragmento 01``  juntos en un archivo)  sin descomentar nada, verá un montón de cuadrados rojos que aparecen y desaparecen por toda la pantalla.

### Fragmento 01
```python
while True:
    surface.fill((0,0,0))
    pygame.draw.rect(surface, (255,0,0), (random.randint(0, windowWidth), random.randint(0, windowHeight), 10, 10))
```

![https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica2/Py2.JPG](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica2/Py2.JPG)

¡No te preocupes, nada está roto! Esto es solo para demostrar que Pygame dibuja, destruye y vuelve a dibujar cosas en una ventana. 

Agregue un `#` al comienzo de la línea que comienza con `surface.fill()`. Usamos este código para borrar los datos de píxeles del marco (frame) anterior. Sin él, lo que vemos son todos los diferentes marcos (frames) construidos uno encima del otro a medida que pasa el tiempo. `surface.fill()` es como la pintura que usamos para cubrir el fondo de pantalla antiguo antes de agregar el nuevo: crea una pizarra en blanco con la que podemos trabajar.

![https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica2/Py2.2.JPG](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica2/Py2.2.JPG)

Pero eso no es muy útil, ¿verdad? Reemplacemos el código del `fragmento 01` con el `fragmento 02` y verá un cuadrado verde moviéndose lentamente a la derecha de la pantalla.

![https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica2/p2.3.JPG](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica2/p2.3.JPG)

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
Entonces, ¿qué está haciendo que nuestro cuadrado se mueva? Cuando vimos la primera practica, dibujábamos formas como esta usando números que pasaríamos a Pygame, como `pygame.draw.rect(surface, (255,0,0), (20, 50, 40, 30))`, y eso está muy bien, siempre y cuando nunca quieras cambiar nada de esa forma.

**¿Qué pasaría si quisiéramos cambiar la altura, el ancho o el color de esta forma? ¿Cómo podríamos decirle a Pygame que cambie los números que ya ingresamos? ** 

Aquí es donde entran las variables. En lugar de pasar números a `pygame.draw.rect()`, pasamos las variables en su lugar. Después de dibujar las formas, podemos cambiar la variable para que la próxima vez que se dibuje se vea ligeramente diferente.

Con el `fragmento 02`, cada vez que dibujamos nuestro cuadrado verde, agregamos `0.01` a la variable que usamos para definir su coordenada X (qué tan lejos está de la izquierda de la pantalla), `greenSquareX`. Hacemos esto con `+=`, que básicamente dice **"tome el valor actual de la variable y luego agregue el número que viene después"**.

**Si cambiamos esa línea para leer `greenSquareX += 0.05`, cada vez que dibujemos nuestro cuadrado, será 0.05 píxeles a la derecha de donde estaba la última vez que se dibujó. Esto da la ilusión de que la forma se mueve más rápido que antes. Si cambiamos el número que ajustamos a `greenSquareX` a `0`, nuestra forma nunca se movería; y si lo cambiamos a `-0.05`, se movería hacia atrás.**

## Moviéndose en todas direcciones

¿Seguramente también podemos subir y bajar? 

**Comente la línea `greenSquareX` del `fragmento 02` y elimine el comentario de la línea de abajo quitando el `#`**. Nuestro cuadrado comenzará a viajar hacia la parte inferior de la pantalla. Al igual que antes, estamos cambiando la variable que le dice a nuestra forma a dónde ir, `greenSquareY`(tenga en cuenta que ahora estamos cambiando `Y`, no `X`), solo un poco cada vez para que se mueva. Y, tal como vimos al cambiar la variable `X`, **podemos hacer que el cuadrado verde suba agregando un número negativo**.

Así que ahora podemos animar cosas que se mueven en cuatro direcciones; eso es suficiente libertad para hacer tantos juegos clásicos: [Pokémon](https://www.youtube.com/watch?v=s_4zaj8EbFI), [Legend Of Zelda](https://www.zelda.com/), [Space Invaders](https://elgoog.im/space-invaders/) y más. **Estos juegos solo moverían cosas horizontal y verticalmente, pero nunca al mismo tiempo**. 

![](https://media.giphy.com/media/xyKxclKcUXfaM/giphy.gif)

**El próximo desafío sería cómo hacer que las cosas se muevan en diagonal.** Afortunadamente, este es un proceso bastante simple también.

 Si **descomentamos** `greenSquareX` y `greenSquareY` en nuestro código, nuestra forma se moverá hacia la derecha y hacia abajo cada vez que Pygame actualice la pantalla. 

>Si **sumamos a nuestros valores** `X` e `Y`, **nuestras formas se moverán hacia la derecha y hacia abajo**. 
>
>Si **sumamos** a nuestro valor `X` y **restamos** de nuestro valor `Y`, **nuestras formas se moverán hacia la derecha y hacia arriba**. 
>
>Si **restamos** de nuestro valor `X` y **sumamos** a nuestro valor `Y`, **nuestras formas se moverán hacia la izquierda y hacia abajo**. 
>
>Finalmente, si **restamos nuestros valores** `X` e `Y`, **nuestra forma se moverá hacia la izquierda y hacia arriba**. 

Eso significa que tenemos ocho direcciones en las que nuestros objetos pueden moverse, es decir, que usamos números que son enteros e iguales entre sí. Si utilizamos valores diferentes para nuestros valores `X` e `Y`, y utilizamos **flotantes** *(que son números con un decimal, como 2.3 o 3.141)* en lugar de **enteros** *(números enteros)*, podríamos lograr un movimiento completo de 360 grados.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ1OTgxMDc2MywxMDQ3ODIzMjA1LC03MT
A0NzY0MjQsNzIwMDk3NjA1LDIwNTkyMDM0MjcsLTc0NTY2Njks
MTkyNTUxNjg4MSwtMTk2MDAxMTYyNywtMTkzODIwNzUxOSwxNT
Y2NTkzNDcsMTAyNTc0NjE1OSwtNzU0NzIwNzQxLC0xMTU5NDM5
OTU2LC0yMjczMzgxNCwtMjk0NTYyNDYwLC0yNzQ0NDI2NTcsMT
gyODI2NzU4NiwxOTM2MzMzNTI5XX0=
-->