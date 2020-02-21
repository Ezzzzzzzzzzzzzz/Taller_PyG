# Dibujando CÍRCULOS y ELIPSES
El proceso de dibujar un círculo es muy parecido a dibujar un cuadrado, excepto que, **en lugar de pasar un ancho y una altura, pasamos un radio y un punto, alrededor del cual dibujamos nuestro círculo**. 

Entonces, por ejemplo, *si quisiéramos dibujar un círculo amarillo en el centro de nuestra ventana con un diámetro de 40 píxeles, usaríamos el siguiente código* para reemplazar el código en el ciclo `while` original en `hello.py`: 
```python
while True:

    #Solo para ayudarnos a recordar
    #pygame.draw.circle(DONDE DIBUJAR, (ROJO, VERDE, AZUL), (COORDENADA X, COORDENADA Y), RADIO, ALTURA, ANCHO)
    
    pygame.draw.circle(window, (255, 255, 0), (250, 200), 20, 0)
    
    pygame.display.update()
```
![https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica1/PyG_P1.3.JPG](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica1/PyG_P1.3.JPG)

**Al igual que dibujar un rectángulo, le decimos a Pygame en qué superficie queremos dibujar nuestro círculo, de qué color queremos que sea y hacia dónde debe ir**. El radio es específico para dibujar esta forma particular. 

**Es posible que haya notado que ponemos un 0 después de nuestro radio; Este es un valor utilizado para determinar el ancho de la línea que dibuja nuestro círculo.** 
>Si pasamos `0`, el **círculo se llena**.
>
> Si pasamos `2`, por ejemplo, **obtenemos una línea de 2 píxeles de ancho con un centro vacío**

```python
while True:
 
    # Relleno
    pygame.draw.circle(window, (255, 255, 0), (200, 200), 20, 0)
    
    # Sin relleno
    pygame.draw.circle(window, (255, 255, 0), (300, 200), 20, 2)
    
    pygame.display.update()
```
### ¿Qué pasa con las elipses? 
Son un cruce ligeramente extraño entre dibujar rectángulos y círculos. Como hicimos cuando dibujamos un rectángulo, pasamos una coordenada X, una coordenada Y, un ancho y una altura, pero terminamos con una forma elíptica. 

Dibujemos una elipse o dos.

```python
while True:

    pygame.draw.ellipse(window, (255, 0, 0), (100, 100, 100, 50))
    
    pygame.draw.ellipse(window, (0, 255, 0), (100, 150, 80, 40))
    
    pygame.draw.ellipse(window, (0, 0, 255), (100, 190, 60, 30))
    
    pygame.display.update()
```

**Ahora debería ver tres elipses: una roja, una verde y una azul. Cada uno debe ser de un tamaño diferente.**

Si desea visualizar cómo se generaron estas formas, podría dibujar rectángulos utilizando las mismas coordenadas que utilizó para dibujar una elipse y encajaría perfectamente dentro de ese cuadro. 

Como habrás adivinado, esto significa que también puedes hacer círculos usando `pygame.draw.ellipse` **si los parámetros ancho y alto son los mismos**.

```python
while True:

    pygame.draw.rect(window, (255, 0, 0), (100, 100, 100, 50), 2)
    
    pygame.draw.ellipse(window, (255, 0, 0), (100, 100, 100, 50))
    
    
    pygame.draw.rect(window, (0, 255, 0), (100, 150, 80, 40), 2)
    
    pygame.draw.ellipse(window, (0, 255, 0), (100, 150, 80, 40))
    
    
    pygame.draw.rect(window, (0, 0, 255), (100, 190, 60, 30), 2)
    
    pygame.draw.ellipse(window, (0, 0, 255), (100, 190, 60, 30))
    
    
    # Circulo   
    pygame.draw.ellipse(window, (0, 0, 255), (100, 250, 40, 40))
    
    
    pygame.display.update()
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNTA4NzY3NjM1LC0xODg2OTE0NTkyLC0yOD
M0MDc2MjQsLTE3MjY5OTA0MTgsLTUxNDMxNzQ2NV19
-->