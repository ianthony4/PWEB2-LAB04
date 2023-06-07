from interpreter import draw
from chessPictures import *

#El modulo
#Caballo negro y caballo blanco juntos
kniBkniW = knight.negative().join(knight)
#La salida
output = (kniBkniW.horizontalMirror().join(knight.horizontalMirror())).up(kniBkniW.negative())
#Dibujar la salida
draw(output)