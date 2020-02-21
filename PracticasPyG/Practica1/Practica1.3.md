# Dibujando CIRCULOS
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
    
    #No relleno
    pygame.draw.circle(window, (255, 255, 0), (300, 200), 20, 2)
    
    pygame.display.update()
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU3ODIxMzU3NSwtNTE0MzE3NDY1XX0=
-->