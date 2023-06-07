from interpreter import draw
from chessPictures import *
#El modulo
#Cuadrado blanco y cuadrado negro
modulo = square.join(square.negative())
#salida
output = modulo.horizontalRepeat(4)
#Dibujar salida
draw(output)