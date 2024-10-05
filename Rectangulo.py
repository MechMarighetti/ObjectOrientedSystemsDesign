import FigurasGeometricas as fg

class Rectangulo(fg.FiguraGeometrica):
    
    
    def __init__(self, colorfondo, colorborde, base, altura):
        super().__init__(colorfondo, colorborde) ## Cuando se llama a super no se pasa el self (si se llama al modulo.clase si)
        self.base = base
        self.altura = altura
        
    @property
    def base(self):
        return self.__base
         
    @base.setter
    def base(self, base):
        self.__base = base
        
    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, altura):
        self.__altura = altura
    
    def area(self):
        return self.base * self.altura
     #Si no se implementa alguno de los metodos abstractos, la clase no se puede instanciar
    
    def perimetro(self):
        return (self.base+self.altura)*2
    
if __name__ == '__main__':

    rectangulo = Rectangulo("rojo", "negro", 5, 55)

    print(f"Color del rectángulo: {rectangulo.colorfondo}")
    print(f"Color del borde del rectángulo: {rectangulo.colorborde}")
    print(f"Área del rectángulo: {rectangulo.area()}")
    print(f"Perímetro del rectángulo: {rectangulo.perimetro()}")

    #figura = fg.FiguraGeometrica('azul', 'verde')
    #No se pueden crear objetos de clases abstractas.