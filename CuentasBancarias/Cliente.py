from .CajaDeAhorro import CajaDeAhorro
from .CuentaCorriente import CuentaCorriente

class Cliente:
    def __init__(self, razon_social, cuit, tipo_persona, domicilio):
        self.__razon_social = razon_social
        self.__cuit = cuit
        self.__tipo_persona = tipo_persona
        self.__domicilio = domicilio
        self.__cuentas_bancarias = []

    @property
    def razon_social(self):
        return self.__razon_social

    @property
    def cuit(self):
        return self.__cuit

    @property
    def tipo_persona(self):
        return self.__tipo_persona

    @property
    def domicilio(self):
        return self.__domicilio

    @property
    def cuentas_bancarias(self):
        return self.__cuentas_bancarias

    def crear_nueva_cuenta_bancaria(self, tipo_cuenta, *args):
        if tipo_cuenta == "CajaDeAhorro":
            cuenta = CajaDeAhorro(*args)
        elif tipo_cuenta == "CuentaCorriente":
            cuenta = CuentaCorriente(*args)
        else:
            return False
        self.__cuentas_bancarias.append(cuenta)
        return True