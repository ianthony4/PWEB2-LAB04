from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    """ La solucion anteiror estaba erronea, esa solucion era la 'HorizontalMirror'"""
    selfReversed = [] #La imagen nueva
    index = len(self.img) - 1
    """ Recorremos el arreglo imagen desde atras hacia adelante y lo vamos agregando al 'selfreversed'"""
    while(index >= 0):
          selfReversed.append(self.img[index]) #Vamos agregando
          index = index - 1 #recueindo index
    return Picture(selfReversed)
  
  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    return Picture(None)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    selfNegative = []
    for x in self.img:
      selfNegative.append(self.img._invColor(x))
    return Picture(selfNegative)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    return Picture(None)

  def up(self, p):
    return Picture(None)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    return Picture(None)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    return Picture(None)

  def verticalRepeat(self, n):
    return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

