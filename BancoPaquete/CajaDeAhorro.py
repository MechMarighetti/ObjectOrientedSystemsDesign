from datetime import date
from BancoPaquete import CuentaBancaria

class CajaDeAhorro(CuentaBancaria):
    def __init__(self, nro_cuenta, cbu, alias, saldo, monto_limite_extracciones, monto_limite_transferencias, cant_extracciones_disponibles, cant_transferencias_disponibles):
        super().__init__(nro_cuenta, cbu, alias, saldo)
        self.monto_limite_extracciones = monto_limite_extracciones
        self.monto_limite_transferencias = monto_limite_transferencias
        self.cant_extracciones_disponibles = cant_extracciones_disponibles
        self.cant_transferencias_disponibles = cant_transferencias_disponibles

        @property
        def monto_limite_extracciones(self):
            return self.__monto_limite_extracciones

        @monto_limite_extracciones.setter
        def monto_limite_extracciones(self, value):
            self.__monto_limite_extracciones = value

        @property
        def monto_limite_transferencias(self):
            return self.__monto_limite_transferencias

        @monto_limite_transferencias.setter
        def monto_limite_transferencias(self, value):
            self.__monto_limite_transferencias = value

        @property
        def cant_extracciones_disponibles(self):
            return self.__cant_extracciones_disponibles

        @cant_extracciones_disponibles.setter
        def cant_extracciones_disponibles(self, value):
            self.__cant_extracciones_disponibles = value

        @property
        def cant_transferencias_disponibles(self):
            return self.__cant_transferencias_disponibles

        @cant_transferencias_disponibles.setter
        def cant_transferencias_disponibles(self, value):
            self.__cant_transferencias_disponibles = value

    def extraer(self, monto_a_extraer):
        if monto_a_extraer > 0 and monto_a_extraer <= self.saldo and monto_a_extraer <= self.monto_limite_extracciones and self.cant_extracciones_disponibles > 0:
            self._CuentaBancaria__saldo -= monto_a_extraer
            self.cant_extracciones_disponibles -= 1
            self._CuentaBancaria__movimientos.append((date.today(), "extracción", monto_a_extraer, self.saldo))
            return True
        return False

    def transferir(self, monto_a_transferir, cuenta_destino):
        if monto_a_transferir > 0 and monto_a_transferir <= self.saldo and monto_a_transferir <= self.monto_limite_transferencias and self.cant_transferencias_disponibles > 0:
            self._CuentaBancaria__saldo -= monto_a_transferir
            cuenta_destino._CuentaBancaria__saldo += monto_a_transferir
            self.cant_transferencias_disponibles -= 1
            self._CuentaBancaria__movimientos.append((date.today(), "transferencia", monto_a_transferir, self.saldo))
            return True
        return False
    