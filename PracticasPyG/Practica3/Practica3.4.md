# Move()

### Justo después de nuestro código de detección de teclas simplemente tenemos `move()`.  Esta es una llamada a una función.

 Hasta ahora, casi todo el código que escribimos estaba dentro de nuestro bucle principal. 

El problema es que después de un tiempo, tener cada línea de código en un bucle grande puede volverse un poco complicado y difícil de seguir. 

### Para hacernos la vida más fácil, hemos puesto el código que es responsable de hacer que nuestro personaje se mueva a su propia función, la función de movimiento.

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
    else :
        playerVY = 0.0
        haveJumped = False

    # ¿Está nuestro cuadrado en el aire?
    # ¡Mejor agrega algo de gravedad para bajarlo!
    if playerY < windowHeight - playerSize:
        playerY += gravity
        gravity = gravity * 1.1
    else :
        playerY = windowHeight - playerSize
        gravity = 1.0

    playerY -= playerVY

    if playerVX > 0.0 and playerVX < maxSpeed or playerVX < 0.0 and playerVX > -maxSpeed:
        if haveJumped == False:
            playerVX = playerVX * 1.1
```
Lo primero que tenemos es una declaración global. Debido a que nuestro código está dentro de la función `move()`, ya no tiene el mismo alcance que nuestro bucle `for`. Aunque podemos mirar los valores de las variables fuera de nuestra función, no podemos establecerlos, a menos que los incluyamos en la declaración global. 

Esto le dice a Python que cuando llamamos playerX, por ejemplo, definitivamente nos referimos al playerX en la parte superior del archivo, no a un nuevo playerX que podríamos crear dentro de la función.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTcwNDEyMDczMiwtMTQ2NTExODkxOSwxOT
I4OTQxODQ5LDUxNzI4NTM2N119
-->