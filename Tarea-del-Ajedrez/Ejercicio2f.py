from interpreter import draw
from chessPictures import *
#Modulo base
#Square negro y blanco
moduloBase = square.negative().join(square)
#Tira de casilleros (1 linea)
tira1Linea = moduloBase.horizontalRepeat(4)