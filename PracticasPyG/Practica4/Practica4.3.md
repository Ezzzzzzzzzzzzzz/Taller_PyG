# Moviendo tu avatar

Nuestro avatar no es una construcción complicada: en su forma más simple, es un rectángulo rojo. Una vez dibujadas nuestras plataformas, queremos averiguar dónde puede ir nuestro avatar. 

Como verá, la función `movePlayer()` en las líneas es el hogar de la mayor parte de la lógica de nuestro juego. Antes de mirar el código, hablemos de lo que está sucediendo: 

 - Queremos que nuestro jugador caiga cuando haya una brecha en la plataforma o no haya ninguna plataforma.
 - También queremos que el avatar suba con la plataforma si no hay un hueco presente. Para codificar esta lógica, podríamos 		verificar la posición de todas las plataformas en cada fotograma y escribir un código que averigüe si nuestro avatar está o no en la parte superior de una plataforma o no, pero eso realmente hará que nuestra computadora trabaje duro y no sería eficiente. En cambio, estamos haciendo algo más simple: nuestras plataformas son siempre blancas y nuestro fondo siempre es negro, por lo que si podemos saber el color del píxel justo debajo de nuestro avatar, podemos determinar si necesitamos o no soltar.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM0OTIwNDY4NV19
-->