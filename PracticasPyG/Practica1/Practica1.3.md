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
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTMwNzkwNTc5LC01MTQzMTc0NjVdfQ==
-->