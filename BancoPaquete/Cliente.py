from BancoPaquete import CajaDeAhorro
from BancoPaquete import CuentaCorriente

class Cliente:
    def __init__(self, razon_social, cuit, tipo_persona, domicilio):
        self.razon_social = razon_social
        self.cuit = cuit
        self.tipo_persona = tipo_persona
        self.domicilio = domicilio
        self.cuentas_bancarias = []

    @property
    def razon_social(self):
        return self.__razon_social
    @razon_social.setter
    def razon_social(self, razon_social): 
        self.__razon_social = razon_social

    @property
    def cuit(self):
        return self.__cuit
    @cuit.setter
    def cuit(self, cuit): 
        self.__cuit = cuit

    @property
    def tipo_persona(self):
        return self.__tipo_persona
    @tipo_persona.setter
    def tipo_persona(self, tipo_persona): 
        self.__tipo_persona = tipo_persona

    @property
    def domicilio(self):
        return self.__domicilio
    @domicilio.setter
    def domicilio(self, domicilio): 
        self.__domicilio = domicilio

    @property
    def cuentas_bancarias(self):
        return self.__cuentas_bancarias
    @cuentas_bancarias.setter
    def cuentas_bancarias(self, cuentas_bancarias): 
        self.__cuentas_bancarias = cuentas_bancarias

    def crear_nueva_cuenta_bancaria(self, tipo_cuenta, *args):
        if tipo_cuenta == "CajaDeAhorro":
            cuenta = CajaDeAhorro(*args)
        elif tipo_cuenta == "CuentaCorriente":
            cuenta = CuentaCorriente(*args)
        else:
            return False
        self.cuentas_bancarias.append(cuenta)
        return True