from datetime import date

from BancoPaquete import CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    def __init__(self, nro_cuenta, cbu, alias, saldo, monto_maximo_descubierto):
        super().__init__(nro_cuenta, cbu, alias, saldo)
        self.monto_maximo_descubierto = monto_maximo_descubierto

        @property
        def monto_maximo_descubierto(self):
            return self.__monto_maximo_descubierto

        @monto_maximo_descubierto.setter
        def monto_maximo_descubierto(self, value):
            if value >= 0:
                self.__monto_maximo_descubierto = value
            else:
                raise ValueError("El monto máximo descubierto debe ser mayor o igual a 0")

    @property
    def saldo(self):
        return self._CuentaBancaria__saldo

    @saldo.setter
    def saldo(self, value):
        if value >= 0:
            self._CuentaBancaria__saldo = value
        else:
            raise ValueError("El saldo debe ser mayor o igual a 0")

    @property
    def movimientos(self):
        return self._CuentaBancaria__movimientos

    @movimientos.setter
    def movimientos(self, value):
        self._CuentaBancaria__movimientos = value

    @property
    def monto_maximo_descubierto(self):
        return self.__monto_maximo_descubierto

    @monto_maximo_descubierto.setter
    def monto_maximo_descubierto(self, value):
        if value >= 0:
            self.__monto_maximo_descubierto = value
        else:
            raise ValueError("El monto máximo descubierto debe ser mayor o igual a 0")

    def transferir(self, monto_a_transferir, cuenta_destino):
        if monto_a_transferir > 0 and monto_a_transferir <= self.saldo + self.monto_maximo_descubierto:
            self.saldo -= monto_a_transferir
            cuenta_destino.saldo += monto_a_transferir
            self.movimientos.append((date.today(), "transferencia", monto_a_transferir, self.saldo))
            return True
        return False