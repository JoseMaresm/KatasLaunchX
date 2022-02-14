"""
    Kata 6
"""

# Ejercicio 1

planets = ['Mercury',
           'Venus',
           'Earth',
           'Mars',
           'Jupiter',
           'Saturn',
           'Uranus',
           'Neptune']

# cantidad de info en la lista
print(len(planets))

# agregar informacion a la lista
planets.append('Pluton')

print(len(planets))
# Valores negativos devuelven al reves las listas
print("El ultimo planeta es: ", planets[-1])


# Ejercicio 2

planets = ['Mercury', 
           'Venus', 
           'Earth', 
           'Mars', 
           'Jupiter', 
           'Saturn', 
           'Neptune']


nombrePlaneta = input("Ingrese el nombre de un planeta, empezando por una letra mayuscula: ")

# .isdigit() se revisa si la entrada es numerica
while nombrePlaneta.isdigit() is True:
    print("Entrada Incorrecta")
    nombrePlaneta = input("Ingrese el nombre de un planeta, empezando por una letra mayuscula: ")

indicePlaneta = planets.index(str(nombrePlaneta))

print("Los planetas mas cercanos al sol son: ",planets[0:indicePlaneta])
# tambien podemos usar el slice -> planets[indicePlaneta+1:]
print("Los planetas mas lejanos al sol son: ",planets[indicePlaneta+1:len(planets)])