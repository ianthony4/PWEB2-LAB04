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
    #La solucion anteiror estaba erronea, esa solucion era la 'HorizontalMirror'
    selfReversed = [] #La imagen nueva
    index = len(self.img) - 1
    #Recorremos el arreglo imagen desde atras hacia adelante y lo vamos agregando al 'selfreversed'
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
    #Recorremos la cantidad de elementos de la lista
    for i in laImagen:
      #Este elemento representa un caracter
      elemento = ""
      #Aqui recorreremos desde el 57 hasta el 0 bajando de 1 en 1
      #En java seria: for(int i = longitudFicha - 1; i >= 0; i--)
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

  #Funciona
  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    laImagen = self.img #Esta es la imagen original (izquierda)
    laImagenAdicional = p.img #Esta es la imagen que se añadira (derecha)
    selfJoin = [] # El resultado
    #Ahora se usa ZIP, combinar elementos en secuciencia (TUPLAS)
    for a, b in zip(laImagen, laImagenAdicional): #zip
      selfJoin.append(a + b)
    return Picture(selfJoin)

    return Picture(None)
  
  #Funciona
  def up(self, p):
    selfUp = [] # La nueva imagen doble
    for line in p.img: # Añadimos la imagen que ira arriba
      selfUp.append(line)
    for line in self.img: # Recorriendo la segunda imagen (base)
      selfUp.append(line)
    return Picture(selfUp) # Retorno la imagen (Funciona)

  #Funciona
  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    #Convirtiendo under.java en una funcion pero adapatada a python
    selfUnder = []
    fondo = self.img
    frontal = p.img
    #Lista de caracteres individuales
    charFondo = []
    charFrontal = []
    #Limite
    totalCaracteres = len(fondo) * len(fondo[0])
    # aux = 0 (no necesario, remplazada por APPEND)
    #Este ciclo almacena lo indicado usando 'SLICING [x:y]' para cada linea
    for i in range(len(fondo)):
      for j in range(len(fondo[i])):
        #En vez de SUBSTRING de java se usara SLICING de python
        charFondo.append(fondo[i][j:j+1])
        charFrontal.append(frontal[i][j:j+1])
        # aux += 1 (APPEND lo remplaza)
    
    #Representamos una linea
    line = ""
    #Hacemos una comparacion de los elementos de los caracteres
    #1. Si en la imagen frontal esta vacia (" ") en cierto indice,
    #   colocamos el elemento del fondo en ese mismo indice en la linea
    #   caso contrario, agregamos ese elemento del frontal en la linea
    #2. Se uso MODULOS para controlar las lineas y agragerlas como elemento en el nuevo arreglo
    for i in range(totalCaracteres):
      if charFrontal[i] == " ":
        if(i + 1)% len(fondo) != 0:
          line = line + charFondo[i]
        else:
          line = line + charFondo[i]
          selfUnder.append(line)
          line = "" # Reiniciando Line
      else:
        if(i + 1)% len(fondo) != 0:
          line = line + charFrontal[i]
        else:
          line = line + charFrontal[i]
          selfUnder.append(line)
          line = "" #Reiniciando line
        
      
    
    return Picture(selfUnder)
  
  #Funciona
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    selfHorizonalRepeat = [] #Resultado
    laImagen = self.img
    for i in laImagen:
      elemento = "" # Podriamos decir que cada elemento es una LINEA
      for j in range(n):
        elemento += i # Aumentando y duplicando las lineas
      selfHorizonalRepeat.append(elemento)
    return Picture(selfHorizonalRepeat)
  
  #Funciona
  def verticalRepeat(self, n):
    selfVerticalRepeat = [] #Nueva imagen
    for i in range(n): #La cantidad de veces que se repetira
      for j in self.img: # Añadiendo los caracteres a la nueva imagen
        selfVerticalRepeat.append(j)
    return Picture(selfVerticalRepeat)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    laImagen = self.img
    selfRotate = []
    #Considerando que la figura es igual de larga en cada linea
    #Caso contrario, seria otro for EXTERIOR que modifique en cada iteracion esa longitud
    elementosLinea = len(laImagen[0])
    #Elementos (lineas) en el dibujo
    elementos = len(laImagen)
    #Linea aux
    line = ""
    #Basicamente este ciclo recorre todas las lineas
    #De esa forma extraemos caracter por caracter y lo colocamos en la nueva imagen
    for i in range(elementosLinea):
      for j in range(elementos):
        line += laImagen[j][i:i+1] #Usando slicing
      #Agregamos la linea
      selfRotate.append(line)
      #Reiniciamos la linea
      line = ""

    return Picture(selfRotate)

