"""
    Kata 9
"""

# Ejercicio 1


def promedio(tan1,tan2,tan3):
    return (tan1 + tan2 + tan3) / 3

def combustible(tanque1, tanque2, tanque3):
    return promedio(tanque1,tanque2,tanque3)

    
print("El promedio es: ", round(combustible(9,15,4),2))


# Ejercicio 2

def informeCohete(horaPrelanzamiento,
                  tiempoVuelo, 
                  destino,
                  tanqueExterno, 
                  tanqueInterno):
    return f'''
    Hora Prelanzamiento: {horaPrelanzamiento}
    Tiempo de vuelo estimado: {tiempoVuelo + horaPrelanzamiento}
    Destino: {destino}
    Tanque: {tanqueExterno + tanqueInterno}
'''
print(informeCohete(12,5,"Mars",200,300))

def infoCohete(destino, *minutos, **combustible):
    return f'''
    Destino: {destino}
    Tiempo de vuelo estimado: {sum(minutos)}
    Tanque: {sum(combustible.values())}
'''
print(infoCohete("Moon",15,24,3,externo=200,interno=100))

# estudiar mas el uso de *arg y **arg
def infoCohete(destino, *minutos, **combustible):
    reporte = f'''
    Destino: {destino}
    Tiempo de vuelo estimado: {sum(minutos)}
    Tanque: {sum(combustible.values())}
'''
    # estudiar mas los argumentos y comprender mas su funcion
    for tanque,val in combustible.items():
        reporte += f'''     tanque {tanque}  => {val} galones\n'''
    return reporte

print(infoCohete("Moon",15,24,3,externo=200,interno=100))