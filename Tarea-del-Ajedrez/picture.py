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
  #Funciona
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
  #Funciona
  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    laImagen = self.img
    selfHorizontal = []
    longitudFicha = len(laImagen)
    """ Recorremos la cantidad de elementos de la lista"""
    for i in laImagen:
      """ Este elemento representa un caracter"""
      elemento = ""
      """Aqui recorreremos desde el 57 hasta el 0 bajando de 1 en 1"""
      """En java seria: for(int i = longitudFicha - 1; i >= 0; i--)"""
      for j in range(longitudFicha - 1, -1 , -1):
        #Recorriendo todos los caracteres de atras hacia adelante
        elemento += i[j]
      selfHorizontal.append(elemento)
    return Picture(selfHorizontal)
  #Funciona
  def negative(self):
    """ Devuelve un negativo de la imagen """
    selfNegative = []
    for x in self.img: # Bucle anidado
      line = '' #Utilizaremos para recorrer linea por linea
      for j in x:
        line = line + self._invColor(j) #Invirtiendo color
      selfNegative.append(line) #Agregando cada linea a la imagen
    return Picture(selfNegative)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    return Picture(None)
  #Funciona
  def up(self, p):
    selfUp = [] # La nueva imagen doble
    for line in p.img: # Añadimos la imagen que ira arriba
      selfUp.append(line)
    for line in self.img: # Recorriendo la segunda imagen (base)
      selfUp.append(line)
    return Picture(selfUp) # Retorno la imagen (Funciona)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    return Picture(None)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    return Picture(None)
  #Funciona
  def verticalRepeat(self, n):
    selfVertical = []
    for i in range(n):
      for j in self.img:
        selfVertical.append(j)
    return Picture(selfVertical)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

