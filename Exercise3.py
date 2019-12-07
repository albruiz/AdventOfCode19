

def function(lista):
    contador = 0
    for i in range(len(lista)):
        condicion = contador%4

        if condicion == 0:
            if lista[i] == 1:
                lista[lista[i+3]]=(lista[lista[i+1]] + lista[lista[i+2]])
            elif lista[i] == 2:
                lista[lista[i+3]]=(lista[lista[i+1]] * lista[lista[i+2]])
            elif lista[i] == 99:
                break
        else:
            pass
        contador += 1

    return lista

ruta = 'text2.txt'
#f devuelve cada una de las letras como array de 1's y 0's
archivo = list(open(ruta, "r").read())
listaElementos = []
for i in range(len(archivo)):
    if archivo[i] != ',' and archivo[i] != '\n':
        listaElementos.append(archivo[i])
listaElementos=[1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,6,23,1,23,6,27,1,13,27,31,2,13,31,35,1,5,35,39,2,39,13,43,1,10,43,47,2,13,47,51,1,6,51,55,2,55,13,59,1,59,10,63,1,63,10,67,2,10,67,71,1,6,71,75,1,10,75,79,1,79,9,83,2,83,6,87,2,87,9,91,1,5,91,95,1,6,95,99,1,99,9,103,2,10,103,107,1,107,6,111,2,9,111,115,1,5,115,119,1,10,119,123,1,2,123,127,1,127,6,0,99,2,14,0,0]

'''
listaNumeros = []
for i in listaElementos:
    listaNumeros.append(int(i))

print(listaNumeros)
'''
listaPrueba = [2,4,4,5,99,0]
listaFinal = function(listaElementos)
print(listaFinal)
