# Alcance global 
banana = 5.0

def move():
    # Alcance de la función   
    banana = 10.0
    print("Este es el alcance de la función: ", banana)
    
    banana += 5
    print("Este tambien es el alcance de la funcion: ", banana)
    
print("Este es el alcance global: ", banana)
move()
print("Este tambien es el alcance global: ", banana)
