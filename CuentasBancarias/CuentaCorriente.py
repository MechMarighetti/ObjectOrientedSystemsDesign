from datetime import date
from .CuentaBancaria import CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    def __init__(self, nro_cuenta, cbu, alias, saldo, monto_maximo_descubierto):
        super().__init__(nro_cuenta, cbu, alias, saldo)
        self.__monto_maximo_descubierto = monto_maximo_descubierto

    def extraer(self, monto_a_extraer):
        if monto_a_extraer > 0 and monto_a_extraer <= self.saldo + self.__monto_maximo_descubierto:
            self._CuentaBancaria__saldo -= monto_a_extraer
            self._CuentaBancaria__movimientos.append((date.today(), "extracción", monto_a_extraer, self.saldo))
            return True
        return False

    def transferir(self, monto_a_transferir, cuenta_destino):
        if monto_a_transferir > 0 and monto_a_transferir <= self.saldo + self.__monto_maximo_descubierto:
            self._CuentaBancaria__saldo -= monto_a_transferir
            cuenta_destino._CuentaBancaria__saldo += monto_a_transferir
            self._CuentaBancaria__movimientos.append((date.today(), "transferencia", monto_a_transferir, self.saldo))
            return True
        return False