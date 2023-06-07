from interpreter import draw
from chessPictures import *
#Modulo base
#Square negro y blanco
moduloBase = square.negative().join(square)
#Tira de casilleros (1 linea)
tira1Linea = moduloBase.horizontalRepeat(4)
#Tira de casilleros (2 lineas, linea de arriba invertida)
tira2Linea = tira1Linea.up(tira1Linea.negative())
#Salida
output = tira2Linea.verticalRepeat(2)
#Dibujar la salida
draw(output)