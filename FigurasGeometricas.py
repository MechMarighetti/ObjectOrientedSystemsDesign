from abc import ABC
from abc import abstractmethod

class FiguraGeometrica(ABC):
    
    
    def __init__(self, colorfondo: str, colorborde: str):
        self.colorfondo = colorfondo
        self.colorborde = colorborde
        
    @property
    def colorfondo(self):
        return self.__colorfondo
    
    @colorfondo.setter
    def colorfondo(self, colorfondo):
        self.__colorfondo = colorfondo
        
    @property
    def colorborde(self):
        return self.__colorborde
    
    @colorborde.setter
    def colorborde(self, colorborde):
        self.__colorborde = colorborde
        
    @abstractmethod    
    def area(self)-> float:
        pass
    
    @abstractmethod
    def perimetro(self):
        pass
    
