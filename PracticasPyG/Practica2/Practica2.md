# Añadiendo más shapes (formas)
### Hemos dibujado con éxito una forma, así que dibujemos algunas más. 

Dibujaremos algunos cuadrados alrededor de la pantalla y analizaremos un poco sus propiedades. **No es necesario crear un nuevo archivo, por lo que nos quedaremos con `hello.py` por ahora.**

**Edite el bucle while para que sea lo mismo que lo siguiente:**
```python
while True:

    pygame.draw.rect(window, (255, 0, 0), (100, 100, 50, 50))
    pygame.draw.rect(window, (0, 255, 0), (150, 100, 50, 50))
    pygame.draw.rect(window, (0, 0, 255), (200, 100, 50, 50))
    
    pygame.display.update()
```
**Ahora deberíamos tener tres cuadrados: rojo, azul y verde**. Hasta ahora, esto es agradable y simple, pero esos cuadrados se colocan uno al lado del otro. 

**¿Qué pasaría si se superpusieran? Vamos a averiguar. 
Cambie su código una vez más a lo siguiente:**
```python
while True:
    
    pygame.draw.rect(window, (255, 0, 0), (0, 0, 50, 50))
    pygame.draw.rect(window, (0, 255, 0), (40, 0, 50, 50))
    pygame.draw.rect(window, (0, 0, 255), (80, 0, 50, 50))
    
    pygame.display.update()
```
**Esta vez tenemos dos rectángulos y un cuadrado**, pero eso no es lo que pedimos. **¿Entonces qué ha ido mal?** Cuando ejecutamos nuestro código, funciona a través de lo que tiene que dibujar y dónde tiene que ponerlo, línea por línea. **Si se dibuja un elemento y luego se dibuja otro sobre él o encima de parte de él, entonces ya no podemos ver qué hay debajo de esa segunda forma.** Los píxeles de la forma dibujada primero se pierden cuando la superponemos con otra forma. Si cambiamos el orden de nuestro código, podemos ver este efecto en acción. 

Corta y pega el código para el segundo cuadrado para que se convierta en el tercer cuadrado dibujado, así:
```python
while True:
    
    pygame.draw.rect(window, (255, 0, 0), (0, 0, 50, 50))
    pygame.draw.rect(window, (0, 255, 0), (40, 0, 50, 50))
    pygame.draw.rect(window, (0, 0, 255), (80, 0, 50, 50))
    
    pygame.display.update()
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTc5Nzg2NjY1LC0xNTkwNTI3MjY3XX0=
-->