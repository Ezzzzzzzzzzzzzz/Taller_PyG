# Game Over
Ya casi hemos terminado; lo último que queremos manejar es lo que sucede cuando nuestro jugador pierde el juego. 

**El juego termina una vez que nuestro avatar desaparece de la parte superior de nuestra pantalla**, y queremos decírselo al usuario. Cuando nuestro avatar desaparece, llamamos a la función `gameOver()`:
```python
def gameOver():
  global gameStarted, gameEnded

  platformSpeed = 0
  gameStarted = False
  gameEnded = True
```
Todo lo que hace la función `gameOver()` es establecer algunas variables que nuestro bucle principal verificará para ver si el juego está en marcha. Una vez que `gameEnded` (juego terminado) sea `True` y `gameStarted` (comenzó el juego) sea `False`, nuestro bucle principal dibujará nuestro juego sobre la pantalla. 

Al igual que nuestra pantalla de bienvenida, dibujamos nuestro juego sobre la imagen en la superficie en la línea: 
```python 
  elif gameEnded is True:
    # Draw game over screen
    surface.blit(game_over_image, (0, 150))
```
y le damos al jugador la opción de reiniciar el juego presionando otra barra espaciadora.

### ¡Y eso es todo! Utilizando todas las habilidades que ya hemos adquirido (y algunas nuevas), creamos nuestro primer juego completo. Como todos los buenos juegos, tenemos un comienzo, un medio y un final.

<!--stackedit_data:
eyJoaXN0b3J5IjpbMjAzMTkwNjM5Ml19
-->