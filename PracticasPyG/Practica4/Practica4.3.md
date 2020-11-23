# Moviendo tu avatar

![](https://media.giphy.com/media/uR6julmSW90mk/giphy.gif)

Nuestro avatar no es una construcción complicada: en su forma más simple, es un rectángulo rojo. Una vez dibujadas nuestras plataformas, queremos averiguar dónde puede ir nuestro avatar. 

Como verá, la función `movePlayer()` en las líneas es el hogar de la mayor parte de la lógica de nuestro juego. Antes de mirar el código, hablemos de lo que está sucediendo: 

- Queremos que nuestro jugador caiga cuando haya una brecha en la plataforma o no haya ninguna plataforma. 
- También queremos que el avatar suba con la plataforma si no hay un hueco presente. 

Para codificar esta lógica, podríamos verificar la posición de todas las plataformas en cada fotograma y escribir un código que averigüe si nuestro avatar está o no en la parte superior de una plataforma o no, pero eso realmente hará que nuestra computadora trabaje duro y no sería eficiente. En cambio, estamos haciendo algo más simple: nuestras plataformas son siempre blancas y nuestro fondo siempre es negro, por lo que si podemos saber el color del píxel justo debajo de nuestro avatar, podemos determinar si necesitamos o no soltar.
También debemos verificar que nuestro avatar esté completamente fuera del borde de nuestra plataforma antes de dejarlo caer. Para hacer esto, verificamos los valores justo debajo de nuestro avatar, tanto a la izquierda como a la derecha. Podemos obtener el color de un píxel en un punto determinado con [`surface.get_at((X, Y))`](https://www.pygame.org/docs/ref/surface.html?highlight=get_at#pygame.Surface.get_at); esto devolverá una tupla con cuatro valores `(ROJO, VERDE, AZUL, OPACIDAD)`, cada uno entre **0** y **255**, como si hubiéramos establecido los colores nosotros mismos. En las líneas 51-52 verificamos el color debajo de la parte inferior izquierda de nuestro avatar, y en las líneas 54-55 hacemos lo mismo para la parte inferior derecha. Si los valores de color que encontramos en la parte inferior izquierda o inferior derecha del avatar son (255,255,255,255) (blanco), entonces sabemos que al menos un borde de nuestro avatar todavía está en una plataforma. Si ambos son cualquier cosa menos blancos, entonces hay un espacio en la plataforma o estamos en un espacio en blanco, por lo que podemos dejar caer nuestro avatar. Todo esto sucede en las líneas 57-68. También comprobamos que no dejamos que nuestro avatar se escape por la parte inferior de nuestra ventana.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTk4NzIxNjE2OCwtOTU2MTIwODYsMTA5ND
Y4OTQ5NCwtMjU5NjE5NDQ5LDEzNDkyMDQ2ODVdfQ==
-->