from CuentasBancarias import Cliente

class Banco:
    def __init__(self, nombre, domicilio):
        self.nombre = nombre
        self.domicilio = domicilio
        self.clientes = []

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def domicilio(self):
        return self.__domicilio
    
    @domicilio.setter
    def domicilio(self, domicilio):
        self.__domicilio = domicilio

    @property
    def clientes(self):
        return self.__clientes
    @clientes.setter
    def clientes(self, clientes):
        self.__clientes = clientes

    def crear_nuevo_cliente(self, razon_social, cuit, tipo_persona, domicilio):
        cliente = Cliente(razon_social, cuit, tipo_persona, domicilio)
        self.clientes.append(cliente)
        return True