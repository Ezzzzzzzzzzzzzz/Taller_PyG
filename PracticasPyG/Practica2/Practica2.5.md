# Cambiando el color sobre el tiempo

Vamos a terminar cambiando los colores de nuestras formas a lo largo del tiempo, pasando a nuestra última sección de código, `fragmento 05`.

### Fragmento 05
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
Al igual que nuestros fragmentos de código anteriores, estamos usando variables en lugar de valores para definir cómo se verán nuestras formas con `pygame.draw.rect.` 

Aquí, no solo estamos sumando y restando valores cada vez que dibujamos nuestras formas; **en cambio, estamos verificando los valores que tenemos antes de cambiarlos, usando una declaración `if`, `else`.**

**Este es un concepto clave del desarrollo de juegos:** *la forma en que un juego responde a las acciones de un jugador es el resultado de cientos y miles de estas pequeñas comprobaciones que se realizan cada pocos milisegundos. Sin ellos, no habría ningún tipo de orden en ningún juego: sería como nuestro primer fragmento de código, con el cuadrado simplemente apareciendo y desapareciendo en posiciones aleatorias, ¡y no hay mucha diversión en eso!*

Con estas comprobaciones de `if`, `else`, **nos aseguramos de que los valores de rojo, verde y azul nunca superen los 255** (el valor máximo en el que pueden mostrarse estos colores; de lo contrario, Pygame devolverá un error).

<!--stackedit_data:
eyJoaXN0b3J5IjpbOTQ2MTMwNDQyXX0=
-->