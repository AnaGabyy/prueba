#crear clase automovil ruedas inicializado en 4
#constructor color, marca, aceleración y velocidad

class Automovil:
  ruedas=4
  def __init__(self, color, marca, aceleracion):
    self.color=color
    self.marca=marca
    self.aceleracion=aceleracion
    self.velocidad=0
    
  def acelerar(self):
    self.velocidad = self.velocidad + self.aceleracion
    velocidadAceleracion= f"La velocidad del coche es de {self.velocidad}"
    return velocidadAceleracion
  
coche1=Automovil("Rojo", "Toyota", 20)

print(coche1.ruedas, coche1.color, coche1.marca, coche1.aceleracion)
print(f"El coche tiene una aceleracion de {coche1.aceleracion}")
coche1.aceleracion=30


coche1.acelerar()


#print(f"La velocidad del coche es de {coche1.velocidad}")  