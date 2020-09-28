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
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjA4MzQ1MTgxMCwtMTE4MzgzMjI5NCwtMT
g3NjEyMzczOF19
-->