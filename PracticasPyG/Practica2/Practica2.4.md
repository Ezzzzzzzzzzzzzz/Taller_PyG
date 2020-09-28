# Animando otras propiedades

La animación no se trata solo de hacer que las cosas se muevan: *también se trata de hacer que las cosas cambien.* 

Hasta ahora, hemos estado animando formas moviéndolas, pero podemos usar el mismo enfoque de cambiar variables a lo largo del tiempo para afectar otras propiedades, como las dimensiones de nuestras formas. 

### Para ello, cambie el código del   `fragmento03` por el `fragmento 04`.

### Fragmento 04
```python
rectX = windowWith / 2
rectY = windowHeight / 2
rectWidth = 50
rectHeight = 50

while True:
    surface.fill((0, 0, 0))
    pygame.draw.rect(surface, (255, 255, 0), (rectX-rectWidth /2, rectY-rectHeight /2, rectWidth, rectHeight))
    
    rectWidth += 1
    rectHeight += 1
```
### Aquí, `pygame.draw.rect` dibuja un rectángulo de la misma forma que lo hicimos antes, pero, como en otros ejemplos, reemplazamos los parámetros que determinan el ancho y la altura de nuestro rectángulo con variables que cambiamos.

También hacemos un poco de matemáticas en nuestro código. A medida que el cuadrado se agranda, el punto desde el que se dibuja no cambiará, por lo que la forma se agrandará, pero lo hará fuera del centro del resto de la ventana. Al restar la mitad del ancho y la mitad de la altura de las coordenadas en las que dibujamos nuestra forma, nuestro cuadrado permanecerá en el centro de la ventana a medida que se hace más grande. Lo bueno de usar variables en nuestras matemáticas es que no importa cómo cambiemos nuestras variables, la forma creada siempre estará en el centro de la ventana. Cambie el número en la línea rectWidth a cualquier otro número entre 2 y 10. Ahora, cuando nuestro cuadrado se agranda, se convierte en un rectángulo, porque su ancho aumenta más rápido que su altura, pero aún permanece en el centro.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU0NDUzODIyMiwyNzY1NzQ4MTIsMjA4Mz
Q1MTgxMCwtMTE4MzgzMjI5NCwtMTg3NjEyMzczOF19
-->