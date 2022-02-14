"""
    Kata 4
"""

# Ejercicio 1

palabrasClaves = ["average","temperature","distance"]
text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

text = text.split(".")


for sent in text:
    for palabraClave in palabrasClaves:
        if palabraClave in sent:
            print(sent.replace("C","Celsius"))
            break


# Ejercicio 2

# Datos con los que vas a trabajar
name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"
titulo = "Gravity"

planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'

# string formateado (personalizado)
titulo = f'datos de gravedad de {nombre}'

print("\n")
print(titulo.title().upper())
print("\n")

multiLine = f"""{'-'*80} 
Nombre del Planeta = {planeta}
gravedad  en {planeta} = {gravedad * 1000} m/m2
"""

# string formateado
# se puede imprimir variables, funciones, multilinea, etc
# practicarlo mas
union = f"""{titulo.title()} 
{multiLine} 
""" 
print(union)


planeta = 'Marte '
gravedad  = 0.03143
nombre = 'Ganímedes'

newTemplate = """
Datos de Gravedad sobre: {nombre}
-------------------------------------------------------------------------------
Nombre del planeta: {planeta}
Gravedad en {nombre}: {gravedad} m/s2
"""

print(newTemplate.format(nombre=nombre,planeta=planeta,gravedad=gravedad*1000))
#print(multiLine)