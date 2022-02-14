"""
    Kata 7
"""

# Ejercicio 1

newPlanet = input("Ingresar un nuevo planeta: ")
planets = []

# Revisar que no sea la palabra 'done'
while newPlanet.lower() != "done":
    # revisar que la entrada no sea numerico
    if newPlanet.isdigit():
        print("Entrada Incorrecta")
        newPlanet = input("Ingresa un nuevo planeta: ")
    else:
        planets.append(newPlanet)
        newPlanet = input("Ingresa otro planeta o ingresa 'done' para finalizar: ")
    
if newPlanet == "done":
    print("Mostrando la lista")
    print("Planetas ingresados: ",planets)
    
    # Ejercicio 2

    print("Mostrar los planetas con ciclo FOR")
    for planet in planets:
        print(planet)
else:
    print("No ingresaste planetas")
    

