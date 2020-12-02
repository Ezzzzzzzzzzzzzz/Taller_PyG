# Pygame Soundbar

En sesiones anteriores, armamos un videojuego simple en el que intentamos evitar el terrible destino de ser aplastados por un techo cayendo a través de plataformas hacia el espacio de abajo. No tenía los gráficos más elegantes, pero, de nuevo, los gráficos elegantes no lo son todo. 

**Una cosa simple que podemos hacer para mejorar la experiencia de nuestros jugadores es agregar sonidos**, y eso es lo que haremos aquí. Vamos a aprender cómo funcionan los sonidos con Pygame armando una caja de resonancia con algunos controles simples. 

![](https://media.giphy.com/media/SXTTVIwYA36XpgfqJW/giphy.gif)

### Aprenderemos a cargar sonidos, reproducirlos, ajustar los controles de sonido y usar el mezclador para detener todo. También crearemos un código para crear los botones de la caja de resonancia; esto se basará en nuestro conocimiento de listas, diccionarios y eventos de mouse que hemos adquirido en sesiones anteriores.

Si bien MP3 es un formato muy popular para reproducir música y sonidos (seguramente ustedes tienen miles de archivos en un disco duro en algún lugar), la desventaja es que es una tecnología patentada. **Como tal, Pygame y otras bibliotecas populares no admiten MP3 de fábrica, quizás porque no pueden pagar una licencia.** Por lo tanto, usaremos [**OGG**](https://es.wikipedia.org/wiki/Ogg), un formato de sonido abierto que tu computadora y Pygame reproducirán sin ningún problema. Todos los sonidos para este proyecto están disponibles en GitHub, en formato OGG y MP3, para que juegues. 

## Lo primero es lo primero

Al igual que con cualquier proyecto de Pygame, hay un par de cosas que debemos resolver antes de poder ensuciarnos las manos escribiendo código real. 

### sounds.py
```python



```
Las líneas 1-14 deberían parecerle realmente familiares a estas alturas: primero tenemos nuestras declaraciones de importación en las líneas 1-5, luego establecemos las propiedades de nuestras ventanas en las líneas 6-11, y finalmente creamos un par de variables para usar en nuestro programa Pygame un poco más adelante en las líneas 13-17. Si observa la línea 13, verá la variable de botones; cuando estemos listos para comenzar a crear nuestros botones, agregaremos algunos diccionarios a esta lista para que podamos realizar un seguimiento de todos los botones de la caja de resonancia que creamos.




<!--stackedit_data:
eyJoaXN0b3J5IjpbLTc2MjI3Mjc4Nyw1OTg2Njg3MzAsNzQ0MT
kxNzA5XX0=
-->