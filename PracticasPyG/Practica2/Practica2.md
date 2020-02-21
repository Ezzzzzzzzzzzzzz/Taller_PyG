# Añadiendo más shapes (formas)
### Hemos dibujado con éxito una forma, así que dibujemos algunas más. 

Dibujaremos algunos cuadrados alrededor de la pantalla y analizaremos un poco sus propiedades. **No es necesario crear un nuevo archivo, por lo que nos quedaremos con `hello.py` por ahora.**

**Edite el bucle while para que sea lo mismo que lo siguiente:**
```python
while True:

    pygame.draw.rect(window,(255, 0, 0), (100, 100, 50, 50))
    pygame.draw.rect(window,(0, 255, 0), (150, 100, 50, 50))
    pygame.draw.rect(window,(0, 0, 255), (200, 100, 50, 50))
    
    pygame.display.update()
```
**Ahora deberíamos tener tres cuadrados: rojo, azul y verde**. Hasta ahora, esto es agradable y simple, pero esos cuadrados se colocan uno al lado del otro. 
**¿Qué pasaría si se superpusieran?** Vamos a averiguar. Cambie su código una vez más a lo siguiente:
```python

```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjMyMDkxNDUyLC0xNTkwNTI3MjY3XX0=
-->