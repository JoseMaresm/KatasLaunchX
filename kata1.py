
"""
    Primer programa
"""
from datetime import date

# funcionan de la misma forma, preguntar sobre la diferencia?
print("*** Fecha ***")
print("Today's date is: ", date.today())
print("Today's date is: ", str(date.today()))
print("\n")




"""
    Convertidor de unidades
"""
print("*** Convertidor ***")
lightYears = 3.26156
parsec = input("Cantidad de Parsec: ")
# remplazo el punto por un digito para que sea numerico todo
_isNumber = parsec.replace('.','',1)

# .isdigit() se revisa si la entrada es numerica
while _isNumber.isdigit() is False or int(_isNumber) <= 0:
        parsec = input("Cantidad de Parsec debe ser numerico positivo: ")
        _isNumber = parsec.replace('.','',1)
# round(valor,2) se utiliza para redondear 2 decimas, puede cambiar
total = round(float(lightYears) * float(parsec),2)
print(str(parsec) + " parsec, is " + str(total) + " lightyears")

