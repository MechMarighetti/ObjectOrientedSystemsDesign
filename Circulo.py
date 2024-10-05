import math
import FigurasGeometricas as fg

class Circulo(fg.FiguraGeometrica):
    def __init__(self, colorborde, colorfondo, radio):
        fg.FiguraGeometrica.__init__(self, colorfondo, colorborde) #cuando se llama al modulo.clase se pasa como parametro el objeto (self)
        self.radio = radio
    
    @property
    def radio(self):
        return self.__radio
    
    @radio.setter
    def radio(self, radio):
        self.__radio = radio

    def area(self):
        return math.pi*math.pow(self.radio, 2)
    
    def perimetro(self):
        return math.pi*(self.radio*2)
    
    

