# Las plataformas de juego

Una vez que se ha presionado la barra espaciadora, comenzará un nuevo juego. Toda la lógica del juego está entre las líneas 40 y 146, pero llamamos a los métodos para generar el juego en las líneas:

```python
    movePlatforms()
    drawPlatforms()
    movePlayer()
    drawPlayer()
```

en un orden particular. 

### movePlatforms()

Primero, llamamos `movePlatforms()`, que funciona en todas las plataformas del juego y lo mueve hacia arriba en la pantalla a la velocidad establecida con la variable `platformSpeed`. 

`movePlatforms` también comprueba si la plataforma ha alcanzado o no la parte superior de nuestra ventana de juego; si lo ha hecho, eliminará esa plataforma de nuestra lista de plataformas de juegos.

Puede notar que el bucle `for` en la línea 110 es un poco diferente de los que usamos en el pasado. A diferencia de la mayoría de los bucles `for` en Python, este pasa el índice al bucle con el valor `idx`. Necesitamos este índice para poder eliminar la plataforma correcta de la lista de plataformas de juego; de lo contrario, tendríamos que trabajar en la lista e intentar averiguar cuál necesita ir cada vez, y eso no sería bueno para la velocidad de fotogramas. .
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3OTMxNTg0NzRdfQ==
-->