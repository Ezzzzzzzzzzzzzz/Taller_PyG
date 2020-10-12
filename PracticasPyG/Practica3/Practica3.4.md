# Move()

### Justo después de nuestro código de detección de teclas simplemente tenemos `move()`.  Esta es una llamada a una función.

 Hasta ahora, casi todo el código que escribimos estaba dentro de nuestro bucle principal. 

El problema es que después de un tiempo, tener cada línea de código en un bucle grande puede volverse un poco complicado y difícil de seguir. 

### Para hacernos la vida más fácil, hemos puesto el código que es responsable de hacer que nuestro personaje se mueva a su propia función, la función de movimiento.

Cuando llamamos a `move()`, se ejecuta una gran cantidad de código. 

En la línea 31 tenemos una declaración global. Debido a que nuestro código está dentro de la función move (), ya no tiene el mismo alcance que nuestro bucle for. Aunque podemos mirar los valores de las variables fuera de nuestra función, no podemos establecerlos, a menos que los incluyamos en la declaración global. Esto le dice a Python que cuando llamamos playerX, por ejemplo, definitivamente nos referimos al playerX en la parte superior del archivo, no a un nuevo playerX que podríamos crear dentro de la función.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAxOTA5MDE4LDE5Mjg5NDE4NDksNTE3Mj
g1MzY3XX0=
-->