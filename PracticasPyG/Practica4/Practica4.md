# Tú primer juego

Ahora que hemos cubierto cómo crear formas, animarlas y configurar mecanismos de control, tenemos todo lo que necesitamos para hacer nuestro primer juego. **Vamos a hacer un juego desplegable de la vieja escuela donde las plataformas se elevan desde el suelo e intentan aplastar a nuestro jugador contra el techo; la única forma de sobrevivir es atravesando los huecos de las plataformas.**

**A diferencia de nuestros ejemplos anteriores, no vamos a escribir un programa que simplemente se ejecute: también crearemos una pantalla de inicio simple y una pantalla de finalización del juego**. 

Todavía tenemos un par de cosas nuevas que vamos a aprender a lo largo del camino, como cargar imágenes y cronometrar eventos. Este es, con mucho, el fragmento de código más grande que habremos escrito, pero no te preocupes: si lo ha seguido hasta ahora, ¡ya reconocerás gran parte de él!

## ¿Cómo funciona nuestro juego?
Antes de escribir cualquier código, es importante tener un conocimiento sólido de cómo va a funcionar nuestro juego. 
>Cuando comience el juego, nuestro avatar (un rectángulo rojo) se desplegará desde la parte superior de la pantalla. 
>Cada dos segundos, una plataforma blanca comenzará a subir desde la parte inferior de la pantalla; 
	>si nuestro personaje aterriza en una de estas plataformas, comenzará a subir junto con ella. 
	>Si salimos de la parte superior de la pantalla del juego, se acabó el juego.
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzA1NDE1MSwxMTc1MjIwODcxXX0=
-->