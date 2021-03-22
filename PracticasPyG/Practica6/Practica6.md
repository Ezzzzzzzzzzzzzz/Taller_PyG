# Física & Fuerzas

En sesiones anteriores, hemos reunido código que nos permite tomar el control de los elementos de nuestro programa cada vez que interactuamos con ellos, ya sea haciendo clic, arrastrando o escribiendo. La dificultad es que hay mucho que podemos hacer con estas interacciones; pase lo que pase, todo lo que hagamos será determinado por nosotros mismos de alguna manera, y eso puede volverse un poco aburrido después de un tiempo. 

![](https://media.giphy.com/media/LRxbk6xYZzHSVrwHd5/giphy.gif)

Siendo este el caso, **en estas sesiones le daremos a ciertos elementos de nuestro programa la capacidad de interactuar con las cosas que los rodean sin que tengamos que hacer nada: vamos a agregar gravedad (o mejor dicho, movimiento que se asemeja mucho gravedad) a algunos planetas que vamos a hacer como parte de un simulador del sistema solar**.

Debemos reconocer una deuda de gratitud con Daniel Shiffman por la inspiración detrás de estos ejemplos. Su libro [**The Nature of Code**](https://natureofcode.com/) explica los conceptos que se encuentran aquí y más con mucho mayor detalle. Todo su código está escrito en Java (Processing), pero debería poder convertirlo a Python con un poco de trabajo.

## Entendiendo la gravedad

Quizás esté pensando que ya hemos cubierto el tema de la gravedad en el capítulo tres. Este es solo el caso en parte. **Allí, agregamos una fuerza que llamamos gravedad a ciertos objetos para hacerlos caer al fondo de la ventana. Sin embargo, esa fuerza no era particularmente dinámica: sin importar el tamaño o la velocidad del objeto, simplemente se sumaría al valor Y de un objeto hasta que alcanzara la parte inferior de la pantalla, lo cual no es muy interesante.**

### Para este nuevo tipo de gravedad, usaremos algo llamado vectores.
![](https://media.giphy.com/media/3o7aDa022Z5JIgsKkg/giphy.gif)

Un vector es un valor que describe dos cosas: **dirección y magnitud**. Con estos, podemos calcular el efecto de un objeto con masa sobre la velocidad (la velocidad y la dirección) de otro objeto con masa. 

La mayoría de las cosas, como dibujar imágenes o manejar pulsaciones de teclas, las hemos hecho antes, por lo que no las volveremos a revisar; en su lugar, **nos centraremos en describir la gravedad e implementarla en nuestro código**. Esto va a requerir un pensamiento serio, así que si no entiende todo la primera vez, no se preocupe: casi todos los que lean esto probablemente sentirán que deben volver a leerlo.

![](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica6/MathsAhead.JPG)

## Entonces, ¿Qué es este asunto de la "gravedad"?

En el mundo real, la gravedad sigue una regla llamada , **["Ley del cuadrado inverso"](https://es.wikipedia.org/wiki/Ley_de_la_inversa_del_cuadrado)** que es la siguiente: 

### "La atracción gravitacional entre dos masas puntuales es directamente proporcional al producto de sus masas e inversamente proporcional al cuadrado de la distancia de separación. La fuerza siempre es atractiva y actúa a lo largo de la línea que los une ”.

Parece un concepto muy complicado, ¿Qué significa?

En realidad, es muy simple: **significa que la fuerza que actúa sobre algo se reduce a medida que aumenta la distancia.** Por lo tanto, por fuerte que sea el tirón de la gravedad sobre algo, como, por ejemplo, *la Tierra tirando de una pelota de fútbol a 1 [m] en el aire, si moviéramos el mismo objeto de modo que estuviera a 3 [m] de distancia de la fuente de gravedad, la la fuerza será 1/9 de la fuerza, es decir, 1/3 al cuadrado o 1 / distancia^2^.*

**La misma ley se aplica a algo más que a la gravedad, también afecta a la luz y al sonido, pero eso no es relevante aquí.** 

[Lab de Fuerza de Gravedad](https://phet.colorado.edu/sims/html/gravity-force-lab-basics/latest/gravity-force-lab-basics_es.html)

### Lo importante es que ahora debería empezar a tener una idea de cómo debería funcionar la gravedad: más lejos significa menos fuerza, más cerca significa más fuerza. 

Igualmente importante es la oración final de esa declaración:

### "La fuerza es siempre atractiva y actúa a lo largo de la línea que une [las masas puntuales]". 

**La gravedad siempre atrae y nunca repele. Siempre tira en la dirección de los objetos que tira**. 

![](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica6/eart.JPG)

Es por esta verdad que vamos a utilizar vectores para simular la gravedad. Usando vectores, podemos calcular la dirección de cada objeto en relación con otro y ajustarlo a la fuerza de atracción gravitacional en consecuencia. El resultado es que ocurre la gravedad.

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1NjEzMTE3ODcsLTUzNzg1NjIzNSw4Nj
c2OTE3MDFdfQ==
-->