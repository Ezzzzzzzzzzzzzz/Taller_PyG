# ¡Un botón aquí, un botón allá, botones EN TODAS PARTES!

![](https://media.giphy.com/media/naxep4vNBAOL6/giphy.gif)

Entonces, **¿Cómo vamos a hacer estos botones?**. Podríamos hacer lo que hemos hecho en sesiones anteriores y dibujar algunas formas y agregarles texto; eso ciertamente haría el trabajo, pero no se verá muy bien. 

### En su lugar, vamos a hacer nuestros botones con algunas imágenes que se han reunido para cada sonido de animal diferente. 

Si desea echar un vistazo a los botones antes de cargarlos, están incluidos junto con el código en la carpeta de [imágenes (images)](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/tree/master/PracticasPyG/Practica5/images) 

Cada botón tiene la silueta de un animal. Emitirá el sonido que hace este animal cuando hagamos clic en él, pero ¿Cómo hacemos que una imagen emita un sonido?. 

**Vamos a utilizar listas y diccionarios de nuevo: ¿recuerdas la variable de botones que vimos al principio de este capítulo? Pudimos ver que actualmente estaba vacío, pero ahora es el momento de agregar algunos diccionarios que describen nuestros botones.**

Si observa las líneas:
```python
# Create Buttons
buttons.append({ "image" : pygame.image.load("assets/images/sheep.png"), "position" : (25, 25), "sound" : pygame.mixer.Sound('assets/sounds/OGG/sheep.ogg')})
buttons.append({ "image" : pygame.image.load("assets/images/rooster.png"), "position" : (225, 25), "sound" : pygame.mixer.Sound('assets/sounds/OGG/rooster.ogg')})
buttons.append({ "image" : pygame.image.load("assets/images/pig.png"), "position" : (425, 25), "sound" : pygame.mixer.Sound('assets/sounds/OGG/pig.ogg')})
buttons.append({ "image" : pygame.image.load("assets/images/mouse.png"), "position" : (25, 225), "sound" : pygame.mixer.Sound('assets/sounds/OGG/mouse.ogg')})
buttons.append({ "image" : pygame.image.load("assets/images/horse.png"), "position" : (225, 225), "sound" : pygame.mixer.Sound('assets/sounds/OGG/horse.ogg')})
buttons.append({ "image" : pygame.image.load("assets/images/dog.png"), "position" : (425, 225), "sound" : pygame.mixer.Sound('assets/sounds/OGG/dog.ogg')})
buttons.append({ "image" : pygame.image.load("assets/images/cow.png"), "position" : (25, 425), "sound" : pygame.mixer.Sound('assets/sounds/OGG/cow.ogg')})
buttons.append({ "image" : pygame.image.load("assets/images/chicken.png"), "position" : (225, 425), "sound" : pygame.mixer.Sound('assets/sounds/OGG/chicken.ogg')})
buttons.append({ "image" : pygame.image.load("assets/images/cat.png"), "position" : (425, 425), "sound" : pygame.mixer.Sound('assets/sounds/OGG/cat.ogg')})
```
verá que cada línea crea un nuevo diccionario para cada animal. Cada diccionario tiene tres claves (o propiedades: los términos son intercambiables). 

> La primera es `image:`(imagen), que nos cargará la imagen de ese botón. En diccionarios anteriores, almacenamos cadenas en diccionarios y luego usamos esas cadenas para cargar imágenes cuando las necesitamos; esta vez, sin embargo, hemos cargado cada imagen en nuestro diccionario con [`pygame.image.load()`](https://www.pygame.org/docs/ref/image.html?highlight=image%20load#pygame.image.load).

Esto ahorra tiempo cuando tenemos que dibujar algo muchas veces, y dado que la imagen nunca cambia, tiene sentido tenerla ahí. 

>Nuestra siguiente clave es la `position:`posición; esta es una tupla simple que contiene las coordenadas xey de donde se dibujarán nuestros botones. La última propiedad, sonido, es como nuestra propiedad de imagen, excepto que, como es de esperar, carga un sonido en lugar de una imagen. Aquí cargamos los sonidos como objetos, lo que significa que son esencialmente autónomos en términos de cómo funcionan.

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTgzMzA5ODg4NywtMTMzMDk4OTg2NiwyMD
Q1MjkyMTE0LC0xMTQ3ODc2OTMyLDg3Mjc3MjQ3OV19
-->