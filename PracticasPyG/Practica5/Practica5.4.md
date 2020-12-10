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
> 3) Dónde estaba el mouse cuando se hizo clic. Si las coordenadas de nuestro mouse son mayores que las coordenadas x y `y
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTY5NzYzNjYyLDk5OTIxMTAyXX0=
-->