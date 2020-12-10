# Stopping todos nuestros sonidos
Hemos hecho un gran trabajo al lograr que nuestro código produzca una variedad de ruidos de corral, pero ¿qué podemos hacer si queremos detener estos ruidos?.

Afortunadamente, tenemos un botón para encargarse de esto por nosotros. En la línea 14 tenemos un diccionario llamado `stopButton`:
```python 
stopButton = { "image" : pygame.image.load("assets/images/stop.png"), "position" : (275, 585)}
```
a diferencia de los botones de nuestra caja de resonancia, no tiene sonido, solo una imagen y un elemento de posición. Eso lo hace especial. 

Debajo de todo el código utilizado para manejar nuestros botones de sonido, tenemos un código que solo se ocupa del botón de parada: en la línea:
```python
 surface.blit(stopButton["image"], stopButton['position'])
```
dibujamos el botón de parada, justo después de haber dibujado todos los de sonido, y en las líneas:
```python
    if mousePosition[0] > stopButton['position'][0] and mousePosition[0] < stopButton['position'][0] + stopButton['image'].get_rect().size[0]:
      if mousePosition[1] > stopButton['position'][1] and mousePosition[1] < stopButton['position'][1] + stopButton['image'].get_rect().size[1]:
        pygame.mixer.stop()
```
 verificamos específicamente si se ha hecho clic en el botón de parada o no. **¿Por qué le damos un trato especial al botón de stop?**

La respuesta es que es único, y para cada botón que no hace lo mismo que todos los demás botones, necesitamos escribir un código personalizado. Por supuesto, podríamos usar diccionarios y listas como lo hemos hecho para nuestros botones de sonido, pero eso es mucho más complicado de lo que se requiere para nuestros propósitos en este momento.

## ¡ES RUIDOSO! Oh ... ahora está tranquilo ...

Entonces, hemos cargado sonidos, los reproducimos y los detuvimos, pero ¿y si solo quisiéramos hacer que los sonidos sean un poco más silenciosos? Esto es bastante simple de lograr. Cada uno de nuestros objetos de sonido tiene una función `set_volume()` a la que se le puede pasar un valor entre `0.0` y `1.0`. `0.0` es mudo, mientras que `1.0` es volumen completo. Si pasa un valor mayor que `1.0`, se convertirá en `1.0`, y si pasa un valor menor que `0.0`, se convertirá en `0.0`. 

Para comenzar, necesitamos hacer un control deslizante de volumen. En las líneas:

## drawVolume()
```python
def drawVolume():
  pygame.draw.rect(surface, (229, 229, 229), (450, 610, 100, 5))
  volumePosition = (100 / 100) * (volume * 100)
  pygame.draw.rect(surface, (204, 204, 204), (450 + volumePosition, 600, 10, 25))
```

dibujamos dos rectángulos. **El primer rectángulo representa el rango de `0.0` a `1.0` y el segundo rectángulo es un indicador del volumen actual**. Cuando iniciamos por primera vez nuestra caja de resonancia, el volumen se establece en `1.0`:
```python
volume = 1.0
```
por lo que nuestro indicador debería estar completamente a la derecha, pero eso no nos sirve de mucho si queremos para las cosas mas suaves.

Justo antes de llamar a `drawVolume()` en la línea 104 llamamos `checkVolume()` en la línea 103. 
```python
 checkVolume()
 drawVolume()
```
**Aquí vemos la posición actual del mouse y si el botón izquierdo del mouse está presionado o no. Si es así, es probable que nuestro usuario intente arrastrar nuestro indicador al nivel en el que desea que esté el sonido. Entonces calculamos dónde está el mouse entre `0.0` y `1.0` en nuestro indicador y configuramos el volumen al nuevo nivel.**

### checkVolume()
```python
def checkVolume():

  global mousePosition, volume

  if pygame.mouse.get_pressed()[0] == True:
    
    if mousePosition[1] > 600 and mousePosition[1] < 625:
      if mousePosition[0] > 450 and mousePosition[0] < 550:
        volume = float((mousePosition[0] - 450)) / 100
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwMDU0NzUxMDhdfQ==
-->