# Animando otras propiedades

La animación no se trata solo de hacer que las cosas se muevan: *también se trata de hacer que las cosas cambien.* 

Hasta ahora, hemos estado animando formas moviéndolas, pero podemos usar el mismo enfoque de cambiar variables a lo largo del tiempo para afectar otras propiedades, como las dimensiones de nuestras formas. 

### Para ello, cambie el código del   `fragmento03` por el `fragmento 04`.

### Fragmento 04
```python
rectX = windowWidth / 2
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

También hacemos un poco de matemáticas en nuestro código. 

A medida que el cuadrado se agranda, el punto desde el que se dibuja no cambiará, por lo que la forma se agrandará, pero lo hará fuera del centro del resto de la ventana. Al restar la mitad del ancho y la mitad de la altura de las coordenadas en las que dibujamos nuestra forma, nuestro cuadrado permanecerá en el centro de la ventana a medida que se hace más grande. 

![](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica2/Cap2.2.5.JPG)

Lo bueno de usar variables en nuestras matemáticas es que no importa cómo cambiemos nuestras variables, la forma creada siempre estará en el centro de la ventana. 

### Cambie el número en la línea `rectWidth` a cualquier otro número entre `2` y `10`. Ahora, cuando nuestro cuadrado se agranda, se convierte en un rectángulo, porque su ancho aumenta más rápido que su altura, pero aún permanece en el centro.

```python
#Ejemplo
rectWidth = 10
```

**El mismo efecto funciona en la dirección opuesta.**

### Si comenzamos con un cuadrado que tiene un ancho y una altura de `50`, lo que podemos hacer estableciendo las variables `rectWidth` y `rectHeight` en `50` y cambiamos el `+=` en esas líneas a `-=`, nuestro cuadrado disminuirá de tamaño mientras permanece central a nuestra ventana.

```python
#Toma el valor actual y restale el valor que viene después
    rectWidth -= 1
    rectHeight -= 1
```

### Algo curioso ocurre cuando nuestra forma alcanza un ancho y un alto de 0: comienza a crecer nuevamente. 

¿Por qué? Cuando llegamos a 0, comenzamos a dibujar nuestro rectángulo con números negativos, contra los cuales estamos compensando con nuestras matemáticas. 

Entonces, **cuando dibujamos una forma con un ancho negativo y luego la compensamos con un número negativo, nuestros puntos de partida se vuelven números positivos nuevamente**, aunque reflejados. 

### No podemos ver el efecto porque estamos usando colores sólidos, pero si usáramos el mismo código de expansión/contracción con una imagen, se voltearía al revés y al revés. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ2ODY3NDg2NiwtMTczNTQ5NjkyNiwtNT
UxNTE0MTUyLC0xNzUzODM4MTczLC0xOTM5Mzk4OTc3LC0xMzAw
NTY5NDAyLDE2MTQ5NzIyNjEsODU5Njc1MzY5LC0yMDk5MDY1NT
Y4LC0yMDY0Njk2MjY5LDQ0MDI4NjQ3OSwtNTQ0NTM4MjIyLDI3
NjU3NDgxMiwyMDgzNDUxODEwLC0xMTgzODMyMjk0LC0xODc2MT
IzNzM4XX0=
-->