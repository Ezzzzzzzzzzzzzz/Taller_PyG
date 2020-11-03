# Move()

### Justo después de nuestro código de detección de teclas simplemente tenemos `move()`.  Esta es una llamada a una función.

 Hasta ahora, casi todo el código que escribimos estaba dentro de nuestro bucle principal. 

El problema es que después de un tiempo, tener cada línea de código en un bucle grande puede volverse un poco complicado y difícil de seguir. 

### Para hacernos la vida más fácil, hemos puesto el código que es responsable de hacer que nuestro personaje se mueva a su propia función, la función de movimiento.

![](https://media.giphy.com/media/jxiDBvPYEtTAk/giphy.gif)

Cuando llamamos a `move()`, se ejecuta una gran cantidad de código. 
```python
def move():

    global playerX, playerY, playerVX, playerVY, haveJumped, gravity

    # Muevete a la izquierda
    if leftDown:
        #Si ya nos estamos moviendo hacia la derecha, restablezca la velocidad de movimiento e invierta la dirección
        if playerVX > 0.0:
            playerVX = moveSpeed
            playerVX = -playerVX    
        # Asegúrate de que nuestro cuadrado no deje nuestra ventana a la izquierda.
        if playerX > 0:
            playerX += playerVX 

    # Muevete a la derecha
    if rightDown:
        # Si ya nos estamos moviendo hacia la izquierda, restablezca la velocidad de movimiento nuevamente.
        if playerVX < 0.0:
            playerVX = moveSpeed
        # Asegúrate de que nuestro cuadrado no deje nuestra ventana a la derecha.
        if playerX + playerSize < windowWidth:
            playerX += playerVX

    if playerVY > 1.0:
        playerVY = playerVY * 0.9
    else:
        playerVY = 0.0
        haveJumped = False

    # ¿Está nuestro cuadrado en el aire?
    # ¡Mejor agrega algo de gravedad para bajarlo!
    if playerY < windowHeight - playerSize:
        playerY += gravity
        gravity = gravity * 1.1
    else:
        playerY = windowHeight - playerSize
        gravity = 1.0

    playerY -= playerVY

    if playerVX > 0.0 and playerVX < maxSpeed or playerVX < 0.0 and playerVX > -maxSpeed:
        if haveJumped == False:
            playerVX = playerVX * 1.1
```
Lo primero que tenemos es una declaración `global`. 
```python
global playerX, playerY, playerVX, playerVY, haveJumped, gravity
```
Debido a que nuestro código está dentro de la función `move()`, ya no tiene el mismo alcance que nuestro bucle `for`. Aunque podemos mirar los valores de las variables fuera de nuestra función, no podemos establecerlos, a menos que los incluyamos en la declaración `global`. 

### Esto le dice a Python que cuando llamamos `playerX`, por ejemplo, definitivamente nos referimos al `playerX` en la parte superior del archivo, y no a un nuevo `playerX` que podríamos crear dentro de la función.

![](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica3/GlobalVariable.JPG)

[Alcance de las variables](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica3/GlobalScope.py)

### Después es donde hacemos que nuestro cuadrado se mueva hacia la izquierda o hacia la derecha, dependiendo de los botones que se hayan pulsado. 

Si el botón de flecha izquierda está apretada, queremos mover el **cuadrado/personaje/objeto** hacia la izquierda. 

**Para hacer esto de manera convincente, primero debemos verificar si nuestro cuadrado ya se está moviendo o no y la dirección en la que va. Si nuestro cuadrado ya está viajando hacia la derecha, debemos detenerlo y luego cambiar de dirección.**

En esta línea se comprueba si la velocidad X de nuestro cuadrado es superior a 0.0 (yendo hacia la derecha). 

```python 
    # Muevete a la izquierda
    if leftDown:
        #Si ya nos estamos moviendo hacia la derecha, detente e invierte la dirección
        if playerVX > 0.0:
            playerVX = moveSpeed
            playerVX = -playerVX    
```
Si no es así, entonces no necesitamos movernos en absoluto, o ya nos estamos moviendo hacia la izquierda, así que podemos seguir moviéndonos. 

Pero si nos movemos hacia la derecha, configurar `playerVX` para `moveSpeed` y luego invertirlo detendrá nuestro cuadrado y lo enviará en la dirección correcta.

Tampoco queremos que nuestro cuadrado se salga de la pantalla;
```python 
        # Asegúrate de que nuestro cuadrado no deje nuestra ventana a la izquierda.
        if playerX > 0:
            playerX += playerVX 
```
Estas líneas detienen el movimiento de nuestro cuadrado si está en el borde izquierdo de nuestra pantalla. 

Las líneas 
```python
        # Asegúrate de que nuestro cuadrado no deje nuestra ventana a la derecha.
        if playerX + playerSize < windowWidth:
            playerX += playerVX
```
hacen exactamente lo mismo pero al revés.

### Es aquí donde agregamos gravedad al movimiento de nuestro cuadrado. 

```python
    if playerVY > 1.0:
        playerVY = playerVY * 0.9
    else:
        playerVY = 0.0
        haveJumped = False

    # ¿Está nuestro cuadrado en el aire?
    # ¡Mejor agrega algo de gravedad para bajarlo!
    if playerY < windowHeight - playerSize:
        playerY += gravity
        gravity = gravity * 1.1
    else:
        playerY = windowHeight - playerSize
        gravity = 1.0
```
Cuando presionamos la flecha hacia arriba en nuestro teclado, nuestro cuadro salta, pero lo que sube debe de bajar. **Al igual que cuando cambiamos de dirección cuando corremos, debemos reducir la velocidad después de saltar antes de comenzar a caer nuevamente.** 
```python
    if playerVY > 1.0:
        playerVY = playerVY * 0.9
    else:
        playerVY = 0.0
        haveJumped = False
```

Primero, verificamos si nuestro cuadrado viaja hacia arriba a una velocidad superior a 1 píxel por cuadro. Si es así, **multiplicamos ese valor por 0,9 para que eventualmente llegue a un punto en el que viaje a menos de 1 píxel por segundo; cuando eso sucede, establecemos el valor en 0 para que podamos comenzar a retroceder hasta la parte inferior de la pantalla.** 

En las líneas, 
```python
    # ¿Está nuestro cuadrado en el aire?
    # ¡Mejor agrega algo de gravedad para bajarlo!
    if playerY < windowHeight - playerSize:
        playerY += gravity
        gravity = gravity * 1.1
```
verificamos que el cuadrado esté en el aire y luego comenzamos a agregar el valor de gravedad al valor `playerVY`; esto hará que nuestro cuadrado vuelva a bajar a la parte inferior de la pantalla. Cada vez que agregamos el valor de gravedad al valor `playerVY`, multiplicamos el primero por 1.1; esto hace que el cuadrado se acelere a medida que cae hacia la parte inferior de la pantalla, tal como lo haría si lanzara una pelota al aire.

Al final las líneas
```python
    else:
        playerY = windowHeight - playerSize
        gravity = 1.0
```
restablecen los valores de `gravity` y `playerVY` cuando la parte inferior del cuadrado toca la parte inferior de la pantalla. 

![](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica3/Explicaci%C3%B3nDinamica.jpg)

Las siguientes líneas son divertidas, ya que impiden que el cuadrado se mueva más rápido hacia la izquierda o hacia la derecha una vez que nuestro cuadrado ha saltado en el aire. 
```python
    if playerVX > 0.0 and playerVX < maxSpeed or playerVX < 0.0 and playerVX > -maxSpeed:
        if haveJumped == False:
            playerVX = playerVX * 1.1
```
![](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica3/Captura.JPG)

No puedes cambiar de dirección después de saltar; solo puedes cambiar de dirección cuando vuelves a tocar el suelo.

Primero, en la línea 52, verificamos si nuestro cuadrado viaja hacia arriba a una velocidad superior a 1 píxel por cuadro. Si es así, entonces multiplicamos ese valor por 0.9 para que eventualmente llegue a un punto en el que viaje a menos de 1 píxel por segundo; cuando eso sucede, establecemos el valor en 0 para que podamos comenzar a retroceder hasta la parte inferior de la pantalla.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU3NjU2NjEzMCw3NTE3MTQ3NDgsLTg0MD
cyMzk2MiwtMTk2NzE5NjU2LC0xMzY2MDU4MTIzLDk2NjM2NjU0
MSwtMTIzMDg4NTQ0LC0yNzEyMjYzNDcsODIwMDMxODQ3LC0yMz
cyMjI2NDEsMjA5MzU5NDk5LC01MzgyMzkzNzcsMTQ0MzU0NjIw
Nyw4MDU2NjM1MTksMTAzMzM0NTM3LC0xMDk1MjIxNTA1LC0xNz
c1NDExNTA5LC04NjgxMTA2MzMsMTE2NDAzMzk4OSwtMjE0MTc4
NDEyM119
-->