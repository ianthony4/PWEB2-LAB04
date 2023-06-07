from interpreter import draw
from chessPictures import *

"""Antes de llegar a la solucion de abajo, se estuvo intentanto
    metodos como crear una linea de figuras y casilleros, usando 'join' """
# filaFiguras = rock.join(knight).join(bishop).........................join(rock)
# filaCasilleros = square.join(square.negative()).horizontalRepeat(4)
"""Y luego hacer uso de la funcion UNDER, como si fueran 2 figuras"""
# firstLine = filaCasilleros.under(filaFiguras)
# draw(firstLine)
"""Lo anterior no funciono, debido a esto que decidimos trabajar FIGURA POR FIGURA para under"""

"""CREACIÓN DE LA FILA DE FIGURAS (CON SU SQUARE)"""

#Modulo de Figuras
figuras = [rock,knight,bishop,queen,king,bishop,knight,rock]
# Creacion de la primera linea
primeraLinea = []
# Ciclo que creara la linea de figuras y cuadrados por debajo

for i in range(len(figuras)):
    if i%2 == 0:
        primeraLinea.append(square.under(figuras[i].negative()))
    else:
        primeraLinea.append(square.negative().under(figuras[i].negative()))

#Metodo que recolecta en una sola variable la linea
def imprimir(arr):
    for i in range(len(arr)):
        if i > 0:
            output = output.join(arr[i])
        else:
            output = arr[i]
    return output
#Recolectamos en una variable picture
firstLine = imprimir(primeraLinea)


"""CREACIÓN DE LA FILA DE PEONES"""
#Creando los 2 primeros peones con su casillero
firstPawn = square.under(pawn)
secondPawn = square.negative().under(pawn)
#Pequeño modulo de los 2 peones
modPawn = firstPawn.join(secondPawn)
#Ahora la fila de peones (blancos)
linePawn = modPawn.horizontalRepeat(4)

"""CREACION DE LOS CASILLEROS DE 3 X 8 (EJERCICIO 2-F)"""
#Modulo basico
twoSquare = square.negative().join(square)
#fila entera
lineSquare = twoSquare.horizontalRepeat(4)
#fila doble
doubleLineSquare = lineSquare.up(lineSquare.negative())
#Resultado final (tambien se puede usar VERTICAL REPEAT)
quadLineSquare = doubleLineSquare.up(doubleLineSquare)


# Imprimimos
draw(quadLineSquare)