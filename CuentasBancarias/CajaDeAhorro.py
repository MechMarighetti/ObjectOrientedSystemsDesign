from datetime import date
from .CuentaBancaria import CuentaBancaria

class CajaDeAhorro(CuentaBancaria):
    def __init__(self, nro_cuenta, cbu, alias, saldo, monto_limite_extracciones, monto_limite_transferencias, cant_extracciones_disponibles, cant_transferencias_disponibles):
        super().__init__(nro_cuenta, cbu, alias, saldo)
        self.__monto_limite_extracciones = monto_limite_extracciones
        self.__monto_limite_transferencias = monto_limite_transferencias
        self.__cant_extracciones_disponibles = cant_extracciones_disponibles
        self.__cant_transferencias_disponibles = cant_transferencias_disponibles

    def extraer(self, monto_a_extraer):
        if monto_a_extraer > 0 and monto_a_extraer <= self.saldo and monto_a_extraer <= self.__monto_limite_extracciones and self.__cant_extracciones_disponibles > 0:
            self._CuentaBancaria__saldo -= monto_a_extraer
            self.__cant_extracciones_disponibles -= 1
            self._CuentaBancaria__movimientos.append((date.today(), "extracción", monto_a_extraer, self.saldo))
            return True
        return False

    def transferir(self, monto_a_transferir, cuenta_destino):
        if monto_a_transferir > 0 and monto_a_transferir <= self.saldo and monto_a_transferir <= self.__monto_limite_transferencias and self.__cant_transferencias_disponibles > 0:
            self._CuentaBancaria__saldo -= monto_a_transferir
            cuenta_destino._CuentaBancaria__saldo += monto_a_transferir
            self.__cant_transferencias_disponibles -= 1
            self._CuentaBancaria__movimientos.append((date.today(), "transferencia", monto_a_transferir, self.saldo))
            return True
        return False