"""
    Kata 5
"""

# Ejercicio 1

distanciaTierra = 149597870 #km
distanciaJupiter = 778547200 #km

distanciaEntrePlanet = (distanciaJupiter - distanciaTierra)
distanciaMillas = distanciaEntrePlanet * 0.621

print(distanciaEntrePlanet)
print(distanciaMillas)


# Ejercicio 2

print("Ingresa la distancia de dos planetas al sol")
distanciaPlanetaUno = input("¿Distancia del primer planeta: ?")

# .isdigit() se revisa si la entrada es numerica
while distanciaPlanetaUno.isdigit() is False:
    print("Entrada Incorrecta")
    distanciaPlanetaUno = input("¿Distancia del primer planeta: ?")

distanciaPlanetaDos = input("¿Distancia del segundo planeta: ?")

# .isdigit() se revisa si la entrada es numerica
while distanciaPlanetaDos.isdigit() is False:
    print("Entrada Incorrecta")
    distanciaPlanetaDos = input("¿Distancia del segundo planeta: ?")



distanciaEntrePlanetas = int(distanciaPlanetaDos) - int(distanciaPlanetaUno)

distanciaEnMillas = distanciaEntrePlanetas * 0.621

print(" Distancia entre planetas: ",abs(distanciaEntrePlanetas))
print("Distancia en millas: ",abs(distanciaEnMillas))