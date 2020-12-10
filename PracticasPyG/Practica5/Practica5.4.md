# Clickeando nuestros botones

Ahora que tenemos una caja de resonancia con botones, necesitamos hacer que esos botones hagan algo. 

Los botones son una de esas cosas que pueden ser realmente simples o realmente complicadas: algunos sistemas hacen mucho del trabajo por usted, mientras que otros no hacen tanto. Desafortunadamente, Pygame es uno de los últimos sistemas, pero eso no importa: podemos escribir el código para nuestros botones nosotros mismos.

En las líneas:
```python
  for event in GAME_EVENTS.get():

    if event.type == pygame.KEYDOWN:

      if event.key == pygame.K_ESCAPE:
        quitGame()

    if event.type == GAME_GLOBALS.QUIT:
      quitGame()

    if event.type == pygame.MOUSEBUTTONUP:
      handleClick()

  drawButtons()
  checkVolume()
  drawVolume()

  pygame.display.update()
```
tenemos código que maneja algunos de los eventos que suceden en Pygame. También reconocerá el código en las líneas:
```python 
  for event in GAME_EVENTS.get():

    if event.type == pygame.KEYDOWN:

      if event.key == pygame.K_ESCAPE:
        quitGame()

    if event.type == GAME_GLOBALS.QUIT:
      quitGame()

    if event.type == pygame.MOUSEBUTTONUP:
      handleClick()
```
 es el mismo código que usamos para salir de Pygame en los últimos cuatro programas, pero en las líneas 
```python
    if event.type == pygame.MOUSEBUTTONUP:
      handleClick()
``` 
 notará que estamos buscando un evento `MOUSEBUTTONUP`.  **Si se está preguntando por qué buscamos `MOUSEBUTTONUP` y no algo como `MOUSECLICK`, recuerde que para que un botón del mouse suba, debe haber bajado primero, lo que significa que se debe haber hecho clic en el mouse.** 

Si se ha hecho clic con el mouse, llamamos a la función `handleClick()`, que está en las líneas 38-55. Al igual que cuando dibujamos nuestros botones, vamos a trabajar en la lista de botones para averiguar dónde están en nuestra superficie. **Si nuestro mouse hace clic donde está el botón, reproduciremos ese sonido; de lo contrario, no haremos nada.**
 
Para comprobar si se hizo clic o no en un botón, necesitamos saber tres cosas: 
> 1) La posición de cada botón 
> 2) El tamaño de ese botón 
> 3) Dónde estaba el mouse cuando se hizo clic. 

### Si las coordenadas de nuestro mouse son mayores que las coordenadas `x` y `y` de la imagen del botón, pero menores que las coordenadas `x`y `y` más el ancho y alto de la imagen, entonces podemos estar seguros de que se hizo clic en el botón que estamos revisando y por lo tanto, podemos reproducir el sonido de ese botón; de lo contrario, el mouse estaba fuera del botón.

![](https://github.com/Ezzzzzzzzzzzzzz/Taller_PyG/blob/master/PracticasPyG/Practica5/Pant.JPG)

### Verificar de esta manera es un poco engañoso: nuestros botones son círculos, pero verificamos si se ha producido un clic dentro de un cuadrado que rodea el botón. Hacemos esto porque el resultado es casi exactamente el mismo y el código para verificar un clic en un cuadrado es mucho más rápido que para verificar un círculo o una forma irregular. Este cuadrado a menudo se denomina cuadro delimitador y se utiliza a menudo para comprobar los clics.

## handleClick()
```python
def handleClick():

  global mousePosition, volume

  for button in buttons:

    buttonSize = button['image'].get_rect().size
    buttonPosition = button['position']

    if mousePosition[0] > buttonPosition[0] and mousePosition[0] < buttonPosition[0] + buttonSize[0]:

      if mousePosition[1] > buttonPosition[1] and mousePosition[1] < buttonPosition[1] + buttonSize[1]:
        button['sound'].set_volume(volume)
        button['sound'].play()

    if mousePosition[0] > stopButton['position'][0] and mousePosition[0] < stopButton['position'][0] + stopButton['image'].get_rect().size[0]:
      if mousePosition[1] > stopButton['position'][1] and mousePosition[1] < stopButton['position'][1] + stopButton['image'].get_rect().size[1]:
        pygame.mixer.stop()
```


Las comprobaciones se realizan en las líneas 47 y 49. Si se determina que cualquiera de las declaraciones es Falsa, no pasará nada, pero si ambas son correctas, reproducimos el sonido con la línea 50. Recuerde, este es un objeto de sonido, no un flujo de sonido. , así que cuando tocamos este sonido, se reproduce a través del mezclador, ya que todos los sonidos pasan para poder reproducirse. Sin embargo, tenga en cuenta que el mezclador no tiene control sobre ese sonido específico porque se reproduce en su propio canal separado.

<!--stackedit_data:
eyJoaXN0b3J5IjpbOTc0NDA1NjgyLDUyOTgwMTYwOSw5OTkyMT
EwMl19
-->