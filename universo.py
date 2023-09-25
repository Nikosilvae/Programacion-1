from abc import ABC, abstractclassmethod
class unidimensional(ABC):#aplico Abstraccion

 def __init__(self):
    self.volumen=0
    self.masa=0
    print("Soy Unidimensional")
    
class bidimensional(unidimensional):#Aplico Herencia
   def __init__(self):
      super().__init__()# LLamado de constructor padre
      print("Hola, soy un elemento bidimensional")    




if(__name__ == "__main__"):
   print("Estoy en el programa principal")
   c = unidimensional()
   print(c.volumen)
   