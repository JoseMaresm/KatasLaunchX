"""
    Kata 8
"""

# Ejercicio 1

from optparse import Values


planet = {
    'name':'Mars',
    'moons':2
}

print(f'El planeta es {planet["name"]} contiene el total de lunas {planet["moons"]}')
print("Se agrega circunferencia")
planet['circunferencia (km)'] = {
    'polar':6752,
    'equatorial': 6792 
}

print(f'''El planeta es {planet["name"]} 
      contiene el total de lunas {planet["moons"]}
      su circunferencia polar es {planet["circunferencia (km)"]["polar"]}km''')

# print(planet)

# Ejercicio 2


planetMoons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

moons = 0
planets = 0
totalMoons = 0

for value in planetMoons.values():
    planets = planets +  1
    totalMoons = totalMoons + value
    
print("el promedio es ", round(totalMoons / planets,2))