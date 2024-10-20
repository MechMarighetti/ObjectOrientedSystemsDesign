from abc import ABC, abstractmethod
from datetime import date


class CuentaBancaria(ABC):

    def __init__(self, nombre, nro_cuenta, cbu, alias, saldo):
        self.nombre = nombre
        self.saldo = saldo
        self.nro_cuenta = nro_cuenta
        self.cbu = cbu
        self.alias = alias
        self.__movimientos = []
    

    def depositar(self, monto_a_depositar):
        if monto_a_depositar > 0:
            self.saldo += monto_a_depositar
            self.movimientos.append((date.today(), "depósito", monto_a_depositar, self.__saldo))
            return True
        return False

    def retirar(self, cantidad):
        self.saldo -= cantidad
        
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
        
    @property
    def cbu(self):
        return self.__cbu
    
    @saldo.setter
    def cbu(self, cbu):
        self.__cbu = cbu
        
    @property
    def nro_cuenta(self):
        return self.__nro_cuenta
    
    @nro_cuenta.setter
    def nro_cuenta(self, nro_cuenta):
        self.__nro_cuenta = nro_cuenta
    
    @property
    def alias(self):
        return self.__alias
    
    @alias.setter
    def alias(self, alias):
        self.__alias = alias
    
    @property
    def movimientos(self):
        return self.__movimientos
        
    def consultar_saldo(self):
        return self.saldo
    
    
    @abstractmethod
    def extraer(self, monto_a_extraer):
        pass

    @abstractmethod
    def transferir(self, monto_a_transferir, cuenta_destino):
        pass

    def __str__(self):
        return f"{self.nombre} tiene un saldo de {self.saldo} pesos"
