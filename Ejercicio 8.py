class Persona:
    def __init__(self, nombre, edad, dni):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad      # Atributo privado
        self.__dni = dni        # Atributo privado

    # Método para retornar la edad
    def mostrar_edad(self):
        return self.__edad

    # Método para verificar si es mayor de edad
    def es_mayor_edad(self):
        return self.__edad >= 18

# Ejemplo de uso:
persona1 = Persona("Mech", 33, "35678131")
persona2 = Persona("Naomi", 17, "45233230")

if __name__ == '__main__':
    print(persona1.mostrar_edad())  # Imprime la edad
    print(persona1.es_mayor_edad())  
    print(persona2.es_mayor_edad())  
    print(persona1.__dict__)
    print(vars(persona2))
