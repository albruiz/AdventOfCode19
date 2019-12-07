import math


def funcion1(lista):
    sumaTotal=0

    for i in lista:
        division=math.trunc(i/3)
        resta=division-2
        sumaTotal+=resta

    return sumaTotal

ruta = 'text1.txt'
#f devuelve cada una de las letras como array de 1's y 0's
archivo = open(ruta, "r")
lista=[]
for linea in archivo.readlines():
    linea = linea[0:(len(linea)-1)]
    lista.append(int(linea))
resultado=funcion1(lista)
print(resultado)
