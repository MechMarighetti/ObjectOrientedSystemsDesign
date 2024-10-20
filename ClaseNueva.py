class Persona:
    def __init__(self, nombre, apellido, dni, altura):
        self.name = nombre
        self.apell = apellido
        self.__dni = dni
        self.__altura = altura
        
    def vacacionar(self):
        print(f"Persona de vacaciones")
    
    @property
    def name(self):
        return self.__nombre
    
    @name.setter
    def name(self, nombre):
        self.__nombre = nombre
    
    @property
    def apell(self):
        return self.__apellido
    
    @apell.setter
    def apell(self, apellido):
        self.__apellido = apellido
    @property
    def altura(self):
        return self.__altura

    def altura(self, altura):
        self.__altura = altura
    
pancho = Persona("Francisco", "Lopez", 12435098, 176) 
caro = Persona("Carolina", "Acevedo", 23953892, 165)

print("Los nombres de las personas son ", caro.name, " ", pancho.name)

#Asignación de nuevo valor usando properties:
caro.name = "Maria Carolina"
pancho.name = "Franco Javier"

print("Los nombres de las personas son ", caro.name, " ", pancho.name)