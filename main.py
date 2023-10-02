#crear clase automovil ruedas inicializado en 4
#constructor color, marca, aceleración y velocidad

class Automovil:
  ruedas=4
  def __init__(self, color, marca, aceleracion):
    self.color=color
    self.marca=marca
    self.aceleracion=aceleracion
    self.velocidad=0
    