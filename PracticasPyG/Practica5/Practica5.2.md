# Entonces mezclemos con el mezclador Pygame

Si vas a usar sonidos en Pygame, es más que probable que uses el mezclador incorporado de Pygame. **Puede pensar en el mezclador como su equivalente en el mundo real: todos los sonidos del sistema (o en nuestro caso, del juego) pasan a través de él**. 

![](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica5/Mezclador.JPG)

Cuando hay un sonido en el mezclador, se puede ajustar de varias formas, siendo el volumen el primero. Cuando nuestro mezclador está terminado, pasa el sonido a través de una salida, que, en este caso, son nuestros altavoces. 

**Entonces, antes de comenzar a cargar o reproducir cualquier sonido, necesitamos inicializar el mezclador, al igual que necesitamos inicializar Pygame antes de dibujar cosas; lo hacemos en la línea:**

```python
pygame.mixer.init()
```
## Nuestro primer sonido

![](https://media.giphy.com/media/cP6EXyM397RDgauGqu/giphy.gif)

### Puede reproducir sonidos de un par de formas diferentes en Pygame: puede reproducir una secuencia (streaming) de sonido, que puede considerar como sonido que se reproduce mientras se carga, o puede crear y reproducir un objeto de sonido, que carga el sonido, lo almacena en la memoria de nuestra computadora y luego lo reproduce.

Cada forma de reproducir sonido es buena para diferentes instancias. **La transmisión (streaming) de sonido es mejor, por ejemplo, cuando queremos crear música de fondo que se reproduce mientras hacemos otras cosas, mientras que el objeto de sonido es una mejor opción para cuando queremos reproducir sonidos cortos de forma rápida y frecuente.**

**El objeto de sonido encaja mejor en nuestra caja de resonancia que el flujo de sonido, por lo que los usaremos para nuestros botones un poco más adelante.** 

### Primero vamos a agregar algo de ambiente a nuestra caja de resonancia con un poco de audio de fondo de una granja. El audio de fondo generalmente se repite sin ningún tipo de interacción del usuario, y el audio de transmisión se puede configurar para que se repita sin demasiados problemas, así que eso es lo que vamos a hacer.

Antes de que podamos reproducir música, necesitamos cargarla, en la línea:
```python
pygame.mixer.music.load('assets/sounds/OGG/farm.ogg')
```
de nuestro programa apuntamos Pygame a nuestro audio de fondo farm.ogg. Esto carga el audio en nuestro mezclador, pero no se reproducirá de inmediato. 

En la línea:
```python
pygame.mixer.music.play(-1)
```
llamamos [`pygame.mixer.music.play (-1)`](https://www.pygame.org/docs/ref/music.html?highlight=play#pygame.mixer.music.play), que comienza a reproducir nuestro archivo de sonido. El número que pasamos es el número de veces que queremos que nuestro sonido se repita antes de que deje de reproducirse. 

**Pasamos `-1`, lo que significa que se repetirá para siempre o hasta que lo detengamos**. Si ejecutamos nuestra caja de resonancia en este punto, tendríamos una hermosa ventana en blanco con algunos sonidos de granja calmantes, pero eso es un poco simple. **¡Es hora de hacer algunos botones!**
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwMTkzMjQ5NDEsMTExMTY1MDk1MSw5Nj
gyMzc5NDYsNjUxNzI4OTM3XX0=
-->