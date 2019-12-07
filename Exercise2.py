import math

def funcion2(numero):
    suma=0
    if numero < 7:
        return numero
    else :
        division = math.trunc(numero/3)
        resta = division - 2
        intermedio = funcion2(resta)
        suma = intermedio + numero
        print(intermedio, suma)

    return suma
#previamente devolvio un numero ahora devolvera una lista con la catidad de carburante de cada uno
def funcion1(lista):
    listaIntermedia = []

    for i in lista:
        division = math.trunc(i/3)
        resta = division-2
        listaIntermedia.append(resta)

    return listaIntermedia

ruta = 'text1.txt'
#f devuelve cada una de las letras como array de 1's y 0's
archivo = open(ruta, "r")
lista=[]
for linea in archivo.readlines():
    linea = linea[0:(len(linea)-1)]
    lista.append(int(linea))
resultado1 = funcion1(lista)

resultado2 = 0

for i in resultado1:
    numero=funcion2(i)
    resultado2 += ( numero  )

print(resultado2)
