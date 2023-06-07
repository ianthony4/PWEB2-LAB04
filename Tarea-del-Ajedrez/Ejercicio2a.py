from interpreter import draw
from chessPictures import *

# Tan sencillo como combinar una serie de metodos
# que nosotros mismos hemos creado ;)  

#Caballo Negro y caballo blanco juntos
kniBkniW = knight.negative().join(knight)
#La salida
output = (kniBkniW.up((kniBkniW).negative()))
#Dibujar salida
draw(output)

