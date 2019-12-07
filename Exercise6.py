
#parameter listaPuntos = array with paris of space's points [X,Y]
#returns listaRectas = array with the horizontal and vertical lines formed by two points
def getRectas(listaPuntos):
    verticales = []
    horizontales = []

    for i in range (len(listaPuntos)):
        x = listaPuntos[i][0]
        y = listaPuntos[i][1]

        for j in range (i, len(listaPuntos)):
            if x != listaPuntos[j][0] and y == listaPuntos[j][1] and j < i + 2:
                listaIntermedia = []
                listaIntermedia.append(listaPuntos[i])
                listaIntermedia.append(listaPuntos[j])
                horizontales.append(listaIntermedia)
            elif x == listaPuntos[j][0] and y != listaPuntos[j][1] and j < i + 2:
                listaIntermedia = []
                listaIntermedia.append(listaPuntos[i])
                listaIntermedia.append(listaPuntos[j])
                verticales.append(listaIntermedia)

    listaRectas = [verticales, horizontales]
    return listaRectas

#parameters = rectas1 and rectas2 are arrays that contain lines from the wires of the problem
#returns = listaIntersecciones array that contains the intersections points of the wires
def getIntersecciones(rectas1, rectas2):
    verticales1 = rectas1[0]
    verticales2 = rectas2[0]
    horizontales1 = rectas1[1]
    horizontales2 = rectas2[1]
    listaIntersecciones = []

    for i in verticales1:
        x = i[0][0]
        y1 = i[0][1]
        y2 = i[1][1]
        for j in horizontales2:
            y = j[0][1]
            x1 = j[0][0]
            x2 = j[1][0]
            if ((x1 < x and x2 > x) or (x1 > x and x > x)) and ((y1 < y and y < y2 ) or (y1 > y and y2 < y )):
                listaIntersecciones.append([x, y])

    for i in verticales2:
        x = i[0][0]
        y1 = i[0][1]
        y2 = i[1][1]
        for j in horizontales1:
            y = j[0][1]
            x1 = j[0][0]
            x2 = j[1][0]
            if ((x1 < x and x2 > x) or (x1 > x and x > x)) and ((y1 < y and y < y2 ) or (y1 > y and y2 < y )):
                listaIntersecciones.append([x, y])

    return listaIntersecciones

def leerFichero(ruta):
    file = open(ruta, 'r')
    datos = file.readlines()
    file.close()
    vector = []
    vectorFinal = []
    for caracter in datos:
        vector.append(caracter)
    intermedio = []
    for i in vector[0].split(','):
        if (i != '\n' ):
            intermedio.append(i)
    vectorFinal.append(intermedio)
    intermedio = []

    for i in vector[1].split(','):
        if (i != '\n' ):
            intermedio.append(i)
    vectorFinal.append(intermedio)
    return vectorFinal

# parameter movimientos = array with the instructions given
# returns listaPuntos = array with the points on the space given
def obtenerPuntos(movimientos):
    listaPuntos = [[0,0]]
    for i in range(len(movimientos)):
        indicacion = movimientos[i][0]
        if(indicacion == 'R'):
            numero = movimientos[i].strip(indicacion)
            numero = int(numero)
            puntoAnterior = listaPuntos[len(listaPuntos) - 1]
            listaPuntos.append([puntoAnterior[0] + numero, puntoAnterior[1]])
        elif(indicacion == 'L'):
            numero = movimientos[i].strip(indicacion)
            numero = int(numero)
            puntoAnterior = listaPuntos[len(listaPuntos) - 1]
            listaPuntos.append([puntoAnterior[0] - numero, puntoAnterior[1]])
        elif(indicacion == 'D'):
            numero = movimientos[i].strip(indicacion)
            numero = int(numero)
            puntoAnterior = listaPuntos[len(listaPuntos) - 1]
            listaPuntos.append([puntoAnterior[0], puntoAnterior[1] - numero])
        else:#el caso en que sea Up
            numero = movimientos[i].strip(indicacion)
            numero = int(numero)
            puntoAnterior = listaPuntos[len(listaPuntos) - 1]
            listaPuntos.append([puntoAnterior[0], puntoAnterior[1] + numero])
    return listaPuntos

def getTraza(punto, rectas1, rectas2):
    verticales1 = rectas1[0]
    verticales2 = rectas2[0]
    horizontales1 = rectas1[1]
    horizontales2 = rectas2[1]
    lista1 = []
    listaFinal = []

    for i in verticales1:
        x = i[0][0]
        y1 = i[0][1]
        y2 = i[1][1]
        lista1.append(i[0])
        lista2 = []
        for j in horizontales2:
            y = j[0][1]
            x1 = j[0][0]
            x2 = j[1][0]
            lista2.append(j[0])
            if x == punto[0] and y == punto[1]:
                listaFinal.append(lista1)
                listaFinal.append(lista2)
                return listaFinal

    lista1 = []
    for i in verticales2:
        x = i[0][0]
        y1 = i[0][1]
        y2 = i[1][1]
        lista1.append(i[0])
        lista2 = []
        for j in horizontales1:
            y = j[0][1]
            x1 = j[0][0]
            x2 = j[1][0]
            lista2.append(j[0])
            if x == punto[0] and y == punto[1]:
                listaFinal.append(lista1)
                listaFinal.append(lista2)

                return listaFinal

def calculaPeso(traza, punto, indicador):
    sumaX = 0
    sumaY = 0
    anteriorx = 0
    anteriory = 0
    X = 0
    Y = 0
    for i in traza[indicador]:
        x = anteriorx - i[0]
        sumaX += abs(x)
        # y =
        y = anteriory - i[1]
        sumaY += abs(y)
        X = i[0]
        Y = i[1]
        anteriorx = i[0]
        anteriory = i[1]

    sumaX += abs(X - punto[0])
    sumaY += abs(Y - punto[1])

    return sumaX + sumaY



ruta = 'text3.txt'
movimientos = leerFichero(ruta)
listaPuntosCable1 = obtenerPuntos(movimientos[0])
listaPuntosCable2 = obtenerPuntos(movimientos[1])
rectasCable1 = getRectas(listaPuntosCable1)
rectasCable2 = getRectas(listaPuntosCable2)
puntosInterseccion = getIntersecciones(rectasCable1, rectasCable2)
trazaSolucion = 10000000000000
for i in puntosInterseccion:
    traza = getTraza(i, rectasCable1, rectasCable2)
    peso0 = calculaPeso(traza, i, 0)
    peso1 = calculaPeso(traza, i, 1)

    if (peso1 + peso0) < trazaSolucion: trazaSolucion = peso1 + peso0

print(f'La distancia recorrida desde (0,0) es: {trazaSolucion}' )
