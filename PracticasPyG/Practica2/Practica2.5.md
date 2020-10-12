# Cambiando el color sobre el tiempo
![](https://media.giphy.com/media/1X7gN6XKLLKcfQR79i/giphy.gif)

Vamos a terminar cambiando los colores de nuestras formas a lo largo del tiempo, pasando a nuestra última sección de código, `fragmento 05`.

## Fragmento 05
```python
squaresRed = random.randint(0, 255)
squaresBlue = random.randint(0, 255)
squaresGreen = random.randint(0, 255)

while True:
    surface.fill((0, 0, 0))
    pygame.draw.rect(surface, (squaresRed, squaresGreen, squaresBlue), (50, 50, windowWidth /2, windowHeight /2))
    
    if squaresRed >= 255:
        squaresRed = random.randint(0, 255)
    else:
        squaresRed += 1
    
    if squaresGreen >= 255:
        squaresGreen = random.randint(0, 255)
    else:
        squaresGreen += 1
    
    if squaresBlue >= 255:
        squaresBlue = random.randint(0, 255)
    else:
        squaresBlue += 1
```
Al igual que nuestros fragmentos de código anteriores, estamos usando variables en lugar de valores para definir cómo se verán nuestras formas con `pygame.draw.rect` 

Aquí, no solo estamos sumando y restando valores cada vez que dibujamos nuestras formas; **en cambio, estamos verificando los valores que tenemos antes de cambiarlos, usando una declaración `if`, `else`.**

**Este es un concepto clave del desarrollo de juegos:** *la forma en que un juego responde a las acciones de un jugador es el resultado de cientos y miles de estas pequeñas comprobaciones que se realizan cada pocos milisegundos. Sin ellos, no habría ningún tipo de orden en ningún juego: sería como nuestro primer fragmento de código, con el cuadrado simplemente apareciendo y desapareciendo en posiciones aleatorias, ¡y no hay mucha diversión en eso!*

Con estas comprobaciones de `if`, `else`, **nos aseguramos de que los valores de rojo, verde y azul nunca superen los 255** (el valor máximo en el que pueden mostrarse estos colores; de lo contrario, Pygame devolverá un error).

Si nuestros valores están a punto de superar los 255, les asignamos un valor aleatorio entre 0 y 255. 

El color de nuestro cuadrado cambiará y luego continuará avanzando lentamente a través de la paleta de colores RGB agregando 1 a nuestras variables **R**, **G** , y  **B** (`squaresRed`, `squaresGreen` y `squaresBlue`) mientras se ejecuta nuestro programa Pygame. 

![](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica2/Cap2.2.6.JPG)

>Al igual que antes, si agregamos un número mayor a cada una de nuestras variables, pasaríamos por los colores disponibles más rápidamente. 
>
>De manera similar, si agregamos menos a cada valor RGB cada vez que Pygame se actualiza, pasaríamos por todos los colores disponibles más lentamente. 

Además de ser un gran dispositivo de aprendizaje, también se ve bastante impresionante.
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjQ0OTEwODM1LDE1NzE3ODI4MzUsMTg0Mz
kyODI5NiwyMDY4ODM2OTQ5LC04OTgwNjc3NjksOTQ2MTMwNDQy
XX0=
-->