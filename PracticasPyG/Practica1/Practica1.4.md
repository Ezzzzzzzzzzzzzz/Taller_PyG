# PATH´s (Trayectorias) 
**Hemos cubierto rectángulos, cuadrados y círculos, pero ¿qué pasa si queremos dibujar un triángulo, un pentágono, un hexágono o un octágono.**

Desafortunadamente, no hay funciones para cada tipo de forma, pero podemos usar **Path's**. **Los Path´s nos permiten dibujar formas irregulares definiendo puntos en el espacio, uniéndolos con líneas y rellenando el espacio que hemos creado**.

Esto es un poco más complejo, por lo que es hora de pasar de nuestro programa original `hello.py`. **Cree un nuevo archivo, llámelo `paths.py` y guárdelo con el siguiente texto dentro:**

```python
import pygame 

pygame.init()

window = pygame.display.set_mode((500, 400))

while True:    
    
    pygame.display.update()
```
Esta es simplemente nuestra aplicación Pygame básica de nuevo. Si desea hacer una copia de esto para experimentar sin romper nada, ahora sería un buen momento para hacerlo. 

Cada **Path** está hecho de líneas conectadas, pero, antes de comenzar a unir las cosas, dibujemos un par de líneas independientes para familiarizarnos con ellas. 

Podemos hacer esto con `pygame.draw.line()`. Edite `paths.py` para que su bucle `while` se lea de la siguiente manera:

```python
while True:    
    
    pygame.draw.line(window, (255, 255, 255), (0, 0), (500, 400), 1)
        
    pygame.display.update()
```
Si ejecuta este código ahora, **verá una línea blanca de un píxel de ancho que va desde la parte superior izquierda a la parte inferior derecha de nuestra ventana de Pygame**. Los parámetros que pasamos a `pygame.draw.line` comienzan de la misma manera que los rectángulos y elipses. 
> **Primero le decimos a Pygame dónde queremos dibujar la forma y luego elegimos un color**. Ahora, las cosas cambian un poco. 
> El **siguiente argumento** es una **tupla con las coordenadas X e Y** para donde queremos que comience nuestra línea, 
> El **tercer argumento** es una **tupla con las coordenadas X e Y** para donde queremos que nuestra línea termine. **Estos son los dos puntos entre los cuales se dibujará nuestra línea. **
> **El argumento final es que el ancho de la línea se dibuja en píxeles**.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU4MzQxNDE4OF19
-->