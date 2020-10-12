# PATH´s (Trayectorias) 
## **Hemos cubierto rectángulos, cuadrados y círculos, pero ¿qué pasa si queremos dibujar un triángulo, un pentágono, un hexágono o un octágono.**

Desafortunadamente, no hay funciones para cada tipo de forma, pero podemos usar **Path's**. 

### **Los Path´s nos permiten dibujar formas irregulares definiendo puntos en el espacio, uniéndolos con líneas y rellenando el espacio que hemos creado**.

Esto es un poco más complejo, por lo que es hora de pasar de nuestro programa original `hello.py`. 

### **Cree un nuevo archivo, llámelo `paths.py` y guárdelo con el siguiente texto dentro:**

```python
import pygame 

pygame.init()

window = pygame.display.set_mode((500, 400))

while True:    
    
    pygame.display.update()
```
Esta es simplemente nuestra aplicación Pygame básica de nuevo. Si desea hacer una copia de esto para experimentar sin romper nada, ahora sería un buen momento para hacerlo. 

### Cada **Path** está hecho de líneas conectadas, pero, antes de comenzar a unir las cosas, dibujemos un par de líneas independientes para familiarizarnos con ellas. 

Podemos hacer esto con `pygame.draw.line()`. Edite `paths.py` para que su bucle `while` se lea de la siguiente manera:

```python
while True:    
    
    pygame.draw.line(window, (255, 255, 255), (0, 0), (500, 400), 1)
        
    pygame.display.update()
```
Si ejecuta este código ahora, **verá una línea blanca de un píxel de ancho que va desde la parte superior izquierda a la parte inferior derecha de nuestra ventana de Pygame**. Los parámetros que pasamos a `pygame.draw.line` comienzan de la misma manera que los rectángulos y elipses. 
> **Primero le decimos a Pygame dónde queremos dibujar la forma y luego elegimos un color**. Ahora, las cosas cambian un poco. 
> 
> El **siguiente argumento** es una **tupla con las coordenadas X e Y** para donde queremos que comience nuestra línea, 
> 
> El **tercer argumento** es una **tupla con las coordenadas X e Y** para donde queremos que nuestra línea termine. **Estos son los dos puntos entre los cuales se dibujará nuestra línea.**
> 
> **El argumento final es que el ancho de la línea se dibuja en píxeles**.

Con esto, ahora podemos crear formas definiendo puntos en nuestra ventana. 

**Dibujemos ese triángulo del que hablamos anteriormente:**
```python
while True:    
    
    pygame.draw.line(window, (255, 255, 255), (50, 50), (75, 75), True)
    
    pygame.draw.line(window, (255, 255, 255), (75, 75), (25, 75), True)
    
    pygame.draw.line(window, (255, 255, 255), (25, 75), (50, 50), True)
        
    
    pygame.display.update()
```
**Deberías tener una imagen de un triángulo blanco con un borde de 1 px**. 

*Sin embargo, este código es bastante largo: muchas cosas, como el color o el ancho de la línea, se escriben varias veces.* Sin embargo, hay una forma más concisa de lograr el resultado que queremos. Todo lo que necesitamos es `pygame.draw.lines()`. Mientras que `pygame.draw.line()` **nos permite dibujar una línea entre dos puntos**, `pygame.draw.lines()` **nos permite dibujar una secuencia de líneas entre numerosos puntos**. Cada punto de coordenadas **XY** se unirá al siguiente punto de coordenadas **XY**, que se unirá al siguiente punto de coordenadas **XY**, **y así sucesivamente**.
```python
while True:    
    
    pygame.draw.lines(window, (255, 255, 255), True, ((50, 50), (75, 75), (25, 75)), 1)
        
    pygame.display.update()
```
![https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica1/PyG_P1.4.JPG](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica1/PyG_P1.4.JPG)

**Es posible que hayas notado que en realidad no cerramos el triángulo: Pygame lo hizo por nosotros.** Justo antes de pasar los puntos de los que se va a dibujar nuestra forma, podemos pasar un valor `True` (Verdadero) o `False`(Falso) que le permitirá a Pygame saber que queremos que cierre nuestras formas por nosotros. **Cámbielo a Falso y obtenemos las dos primeras líneas de nuestra forma, pero no la tercera.** 

**Si queremos hacer una forma más compleja**, simplemente agregamos más puntos así:

```python
while True:    
    
    #pygame.draw.lines(DONDE DIBUJAREMOS, COLOR, ¿CERRAR LA FORMA PARA NOSOSTROS?, LOS PUNTOS PARA DIBUJAR, ANCHO DE LA LINEA)
    pygame.draw.lines(window, (255, 255, 255), True, ((50, 50), (75, 75), (63, 100), (38, 100), (25, 75)), 1)
        
    pygame.display.update()
```
Ahí lo tienes: **tu propio pentágono**. 

![https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica1/PyG_P1.4.2.JPG](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica1/PyG_P1.4.2.JPG)

Si desea hacer un hexágono, un octágono o incluso un [triacontagon](https://en.wikipedia.org/wiki/Triacontagon), simplemente agregue más puntos, así de fácil. 

¿Por qué no intentar experimentar con Pygame para producir algunos pixel art interesantes?
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTczMzY1MzM4NywtMTU0NDUzNTA4OCwtMT
M4NTQ0MjY4OCwtNjY3NzIyNTU2LDYwNTA5NjYwMCwtMTYzMDE1
Nzc2NiwtNDM3NTQzMjc5LC0xMzU4MzcyMTcwLDE1ODM0MTQxOD
hdfQ==
-->