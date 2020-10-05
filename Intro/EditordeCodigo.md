## El editor de código[](https://realpython.com/python-thonny/#the-code-editor "Enlace Permanente")

Ahora que comprende la interfaz de usuario, usemos Thonny para escribir otro pequeño programa. En esta sección, analizará las funciones de Thonny que lo guiarán a través de su flujo de trabajo de desarrollo.

### Escriba algún código[](https://realpython.com/python-thonny/#write-some-code "Enlace Permanente")

En el editor de código (parte superior de la interfaz de usuario), agregue la siguiente función:

```python
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)
print(factorial(3))
``` 

### Guarde su código[](https://realpython.com/python-thonny/#save-your-code "Enlace Permanente")

Antes de continuar, guardemos su programa. La última vez, se le pidió que hiciera esto después de presionar el botón de reproducción. También puede hacer esto haciendo clic en el ícono del disquete azul o yendo a la barra de menú y seleccionando _Archivo_ > _Guardar_ . Llamemos al programa `factorial.py`.

### Ejecute su código[](https://realpython.com/python-thonny/#run-your-code "Enlace Permanente")

Para ejecutar su código, busque y presione el ícono de reproducción. La salida debería verse así:

[![Salida de función factorial](https://files.realpython.com/media/Screenshot_2018-10-11_23.49.22.af82669bc586.png)](https://files.realpython.com/media/Screenshot_2018-10-11_23.49.22.af82669bc586.png)

### Depura tu código[](https://realpython.com/python-thonny/#debug-your-code "Enlace Permanente")

Para comprender realmente lo que está haciendo esta función, pruebe la función de pasos. Realice algunos pasos grandes y pequeños a través de la función para ver qué está sucediendo. Recuerde que puede hacer esto presionando los íconos de flecha:

[![Ventanas paso a paso](https://files.realpython.com/media/Screenshot_2018-10-23_22.47.50.5613862c2c62.png)](https://files.realpython.com/media/Screenshot_2018-10-23_22.47.50.5613862c2c62.png)

Como puede ver, los pasos mostrarán cómo la computadora está evaluando cada parte del código. Cada ventana emergente es como un trozo de papel borrador que la computadora está usando para calcular cada parte del código. Sin esta característica asombrosa, esto podría haber sido difícil de conceptualizar, ¡pero ahora lo tiene!


### Deje de ejecutar su código[](https://realpython.com/python-thonny/#stop-running-your-code "Enlace Permanente")

Hasta ahora, no ha sido necesario presionar el ícono de detener para este programa, particularmente porque se cierra tan pronto como se ejecuta [`print()`](https://realpython.com/python-print/). Intente aumentar el número que se pasa a la función factorial para `100`:

```
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)
print(factorial(100))` 

Luego, recorra la función. Después de un tiempo, notarás que estarás haciendo clic durante mucho tiempo para llegar al final. Este es un buen momento para usar el botón de parada. El botón de parada puede resultar realmente útil para detener un programa que se está ejecutando de forma continua o intencionada o no.

### Encuentre errores de sintaxis en su código[](https://realpython.com/python-thonny/#find-syntax-errors-in-your-code "Enlace Permanente")

Ahora que tiene un programa simple que funciona, ¡vamos a romperlo! Al crear intencionalmente un error en su programa factorial, podrá ver cómo Thonny maneja este tipo de problemas.

Crearemos lo que se llama un **error de sintaxis** . Un [error de sintaxis](https://realpython.com/invalid-syntax-python/) es un error que indica que su código es sintácticamente incorrecto. En otras palabras, su código no sigue la forma correcta de escribir Python. Cuando Python nota el error, mostrará un error de sintaxis para quejarse de su código no válido.

Por encima de la declaración de impresión, agreguemos otra declaración de impresión que diga `print("The factorial of 100 is:")`. Ahora sigamos adelante y creemos errores de sintaxis. En la primera declaración impresa, elimine la segunda comilla y, en la otra, elimine el segundo paréntesis.

Al hacer esto, debería ver que Thonny resaltará su `SyntaxErrors`. Las citas que faltan están resaltadas en verde y los paréntesis que faltan están en gris:

[![errores de sintaxis para la función factorial](https://files.realpython.com/media/Screenshot_2018-10-12_00.11.56.451e383e9c31.png)](https://files.realpython.com/media/Screenshot_2018-10-12_00.11.56.451e383e9c31.png)

Para los principiantes, este es un gran recurso que les permitirá detectar cualquier error tipográfico mientras escribe. Algunos de los errores más comunes y frustrantes al comenzar a programar son las comillas faltantes y los paréntesis que no coinciden.

Si tiene la _Vista del Asistente_ activada, también notará que le dará un mensaje útil para guiarlo en la dirección correcta cuando esté depurando:

[![Muestra al asistente mostrando el texto de ayuda del error de sintaxis](https://files.realpython.com/media/Screenshot_2018-10-20_10.18.50.1f3845020f38.png)](https://files.realpython.com/media/Screenshot_2018-10-20_10.18.50.1f3845020f38.png)

A medida que se sienta más cómodo con Thonny, el Asistente puede ser una herramienta útil para ayudarlo a despegarse.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExNTUzNjM2MjQsNzE3NTEwNTk4XX0=
-->