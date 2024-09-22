import random

class Password:
    # Atributos de clase privados
    __LONGITUD = 8
    __CARACTERES_VALIDOS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"

    def __init__(self, longitud=__LONGITUD):
        # Validación de la longitud mínima y máxima
        if 6 <= longitud <= 15:
            self.__longitud = longitud
        else:
            self.__longitud = Password.__LONGITUD
        
        # Generar contraseña al crear el objeto
        self.__contraseña = self.generarPassword()

    def generarPassword(self):
        self.__contraseña = ''.join(random.choice(self.__CARACTERES_VALIDOS) for i in range(self.__longitud))
        return self.__contraseña

    # Método que verifica si la contraseña es fuerte
    def esFuerte(self):
        mayusculas = sum(1 for c in self.__contraseña if c.isupper())
        minusculas = sum(1 for c in self.__contraseña if c.islower())
        numeros = sum(1 for c in self.__contraseña if c.isdigit())
        especiales = sum(1 for c in self.__contraseña if c in "<=>@#%&+")
        return mayusculas > 1, minusculas > 1, numeros > 1, especiales > 0

    @property
    def longitud(self):
        return self.__longitud

    @longitud.setter
    def longitud(self, longitud):
        if 6 <= longitud <= 15:
            self.__longitud = longitud
            self.generarPassword()

    @property
    def contraseña(self):
        return self.__contraseña

    @contraseña.setter
    def contraseña(self, contraseña):
        # Validación de la longitud mínima y máxima
        if 6 <= len(contraseña) <= 15:
            self.__contraseña = contraseña
            self.longitud = len(contraseña)
        else:
            print("La contraseña debe tener entre 6 y 15 caracteres")

    # Sobrescribir el método __str__ para mostrar la contraseña y si es fuerte
    def __str__(self):
        return f"{self.__contraseña} - {self.esFuerte()}"

# Función para solicitar longitud por teclado
def ingresar_longitud():
    try:
        return int(input("Ingrese la longitud de la contraseña (0 para valor por defecto): "))
    except ValueError:
        return 0

# Crear lista de contraseñas
lista_passwords = []

# Solicitar contraseñas al usuario
for i in range(3):  # Se pueden cambiar el número de contraseñas a generar
    longitud = ingresar_longitud()
    if longitud == 0:
        password = Password()
    else:
        password = Password(longitud)
    lista_passwords.append(password)

# Mostrar las contraseñas generadas y si son fuertes
for i, password in enumerate(lista_passwords, 1):
    print(f"Contraseña {i}: {password}")