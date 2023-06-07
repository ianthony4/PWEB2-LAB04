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
figures = [rock,knight,bishop,queen,king,bishop,knight,rock]
# Creacion de la primera linea
firstLine = []
# Ciclo que creara la linea de figuras y cuadrados por debajo

for i in range(len(figures)):
    if i%2 == 0:
        firstLine.append(square.negative().under(figures[i]))
    else:
        firstLine.append(square.under(figures[i]))

#Metodo que recolecta en una sola variable la linea
def imprimir(arr):
    for i in range(len(arr)):
        if i > 0:
            output = output.join(arr[i])
        else:
            output = arr[i]
    return output
#Recolectamos en una variable picture
lineFiguresWhite= imprimir(firstLine)


"""CREACIÓN DE LA FILA DE PEONES"""
#Creando los 2 primeros peones con su casillero
firstPawn = square.under(pawn)
secondPawn = square.negative().under(pawn)
#Pequeño modulo de los 2 peones
modPawn = firstPawn.join(secondPawn)
#Ahora la fila de peones (blancos)
linePawnWhite = modPawn.horizontalRepeat(4)

"""CREACION DE LOS CASILLEROS DE 3 X 8 (EJERCICIO 2-F)"""
"""Tambien existe la posibilidad de importarlo desde la clase Ejercicio 2F"""
#Modulo basico
twoSquare = square.negative().join(square)
#fila entera
lineSquare = twoSquare.horizontalRepeat(4)
#fila doble
doubleLineSquare = lineSquare.up(lineSquare.negative())
#Resultado final (tambien se puede usar VERTICAL REPEAT)
quadLineSquare = doubleLineSquare.up(doubleLineSquare)

"""CREACION DE MEJORES LINEAS ESPECIFICAS"""
# Aqui identificaremos y definiremos que lineas son negras y que lineas son blancas con las variables ya creadas

#linea de figuras negras
lineFiguresBlack = lineFiguresWhite.negative()
#linea de peones negras
linePawnBlack = linePawnWhite.negative()


# Imprimimos
draw(lineFiguresWhite)