from interpreter import draw
from chessPictures import *
#El modulo
#Cuadrado blanco y cuadrado negro
modulo = square.join(square.negative())
#Salida
output = (modulo.negative()).horizontalRepeat(4)
#Dibujar la salida
draw(output) 

