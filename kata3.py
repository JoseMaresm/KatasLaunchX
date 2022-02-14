"""
    Kata 3
"""

# Ejercicio No. 1
velocidadAsteroide = 49
if velocidadAsteroide > 25:
    print("¡ Alerta ! Se dirige un Asteroide a la tierra !!!")
else:
    print("¡ Que tengas un buen dia !")


# Ejercicio No. 2

velocidadAsteroide2 = 19
if velocidadAsteroide2 >= 20:
    print("¡Hay uno que se dirige a la tierra ahora!")
else:
    print("No se puede ver el haz de luz del Asteroide")


# Ejercicio No 3.

tamañoAsteroide = 30
velocidadasteriode = 40
if tamañoAsteroide >= 25 and tamañoAsteroide < 100 and velocidadasteriode > 25 :
    print("El asteroide causara mucho daño")
elif velocidadasteriode >= 20:
    print("Se puede ver el asteroide")
elif tamañoAsteroide < 25:
    print("El asteroide se quemara al entrar a la admosfera")
else:
    print("No hay asteroide que ver")

    