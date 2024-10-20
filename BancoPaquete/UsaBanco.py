
# Importar las clases del paquete CuentasBancarias
from BancoPaquete import CajaDeAhorro, CuentaBancaria, CuentaCorriente


class UsaBanco:
    def main(self):
        # Crear instancias de las clases del paquete CuentasBancarias
        cuenta = CuentaBancaria("123456", "Juan Perez", 1000.0)
        cuenta_ahorros = CajaDeAhorro("654321", "Maria Lopez", 2000.0, 0.05)
        cuenta_corriente = CuentaCorriente("789012", "Carlos Gomez", 1500.0, 500.0)

        # Probar métodos de la clase Cuenta
        print("Cuenta:")
        print(cuenta)
        cuenta.depositar(500.0)
        print(f"Saldo después del depósito: {cuenta.saldo}")
        cuenta.retirar(300.0)
        print(f"Saldo después del retiro: {cuenta.saldo}")

        # Probar métodos de la clase CajaDeAhorro
        print("\nCuenta de Ahorros:")
        print(cuenta_ahorros)
        cuenta_ahorros.depositar(1000.0)
        print(f"Saldo después del depósito: {cuenta_ahorros.saldo}")
        cuenta_ahorros.retirar(500.0)
        print(f"Saldo después del retiro: {cuenta_ahorros.saldo}")
        cuenta_ahorros.aplicar_interes()
        print(f"Saldo después de aplicar interés: {cuenta_ahorros.saldo}")

        # Probar métodos de la clase CuentaCorriente
        print("\nCuenta Corriente:")
        print(cuenta_corriente)
        cuenta_corriente.depositar(700.0)
        print(f"Saldo después del depósito: {cuenta_corriente.saldo}")
        cuenta_corriente.retirar(2000.0)
        print(f"Saldo después del retiro: {cuenta_corriente.saldo}")

if __name__ == "__main__":
    UsaBanco().main()