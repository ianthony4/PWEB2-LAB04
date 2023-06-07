from interpreter import draw
from chessPictures import *
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
# Imprimimos
draw(firstLine)