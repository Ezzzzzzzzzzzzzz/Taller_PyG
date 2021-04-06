# V es para vector
Entonces, ahora que comprendemos cómo funciona la gravedad, es hora de echar un vistazo a lo que es un vector. Puedes pensar en un vector como una flecha:

### Tiene dos valores, una X y una Y, y juntos apuntan en una dirección. 

>- Por ejemplo, si dibujáramos una línea desde **(0,0) a lo largo de un vector de (8, 4)** en una cuadrícula, **apuntaría hacia abajo y hacia la derecha; por cada unidad recorrida a lo largo del eje X (píxeles, centímetros, pulgadas, brazas, el tipo de unidad no importa), se viajarían 0,5 unidades a lo largo del eje Y.**
>- Si tuviéramos que dibujar otra línea desde **(0,0) a lo largo de un vector de (-1, -2), la línea viajaría hacia la izquierda y hacia arriba;** por cada unidad recorrida a lo largo del eje X, se atravesarían dos a lo largo del eje Y.

![](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/pyg_partII/PracticasPyG/Practica6/vectors.JPG)

Entonces, con los vectores podemos describir la dirección, pero también podemos expresar algo llamado **magnitud**. 

### La magnitud del vector es la longitud de la línea trazada entre (0,0) y el vector en una cuadrícula, pero también podemos pensar en la magnitud como una cantidad o tamaño de algo; por ejemplo, podríamos usarlo como velocidad. 

Cuando usamos vectores para describir la dirección, a menudo ayuda normalizarlos. **Esto significa que tomamos un vector, como (1, 3), y convertimos cada valor en un valor entre -1 y 1 dividiéndolo por la magnitud.** 

![](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/pyg_partII/PracticasPyG/Practica6/Normalization.JPG)

>- Por ejemplo, **el vector (1, 3) se normalizaría a (0.316, 0.948)**
>- mientras que **(-8, 2.4) se normalizaría a (-0.957, 0.287)**

### Normalizar nuestros valores de esta manera hace que sea mucho más fácil afectar las cosas con fuerza y dirección. 

Al tener un valor entre -1 y 1, solo tenemos una indicación de dirección. Cuando tenemos eso, somos libres de ajustarlo por cualquier valor para satisfacer nuestras necesidades; por ejemplo, podríamos multiplicar los valores por un valor de velocidad para dar movimiento a algo.

## Una visión general rápida

Para resumir el material que acabamos de cubrir:
>- La gravedad siempre atrae en la dirección de algo con masa
>- Los vectores describen una dirección y una magnitud que es una cantidad de algo, como la velocidad; y los vectores se pueden reducir a un valor entre -1 y 1 para describir solo una dirección, a través de un proceso llamado **normalización**. 

Ahora que hemos revisado y entendido estos conceptos clave, es hora de empezar a buscar código con Pygame.

**Vamos a omitir la explicación de gran parte del código de este tutorial, es todo el material que hemos visto antes, pero en aras de la claridad, haremos un repaso rápido de las funciones, ¿qué es lo que hacen, y el orden en que se llaman**. 

### Con el conocimiento que hemos adquirido anteriormente, vamos a construir un simulador del sistema solar que mueve los planetas con la gravedad, en función de su masa y velocidad.


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU5ODg3Mjk0MCwtMTU1NTI3OTA3LC0yMD
IzNzUwMjQ3LC0xNzQ4ODk3MTU3LC0yMDI1MzMyODMzLC0zNTE4
NTcwNTgsLTc0NDc0NzEyMywxNjM4OTk1OTcyXX0=
-->