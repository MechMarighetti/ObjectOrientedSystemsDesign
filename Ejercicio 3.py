##Ejercicio 3
##Autor: Mercedes Marighetti

""" Escribe un programa en Python que solicite al usuario 5 números
enteros. Luego imprimir el máximo y el mínimo de los valores
ingresados. El programa deberá permitir el ingreso de valores iguales. """
numeros = []
i = 0
for i in range(5) :
    num = int(input("Ingresá un numero: "))
    numeros.append(num)

maximum = max(numeros)
minimum = min(numeros)

print("El máximo valor ingresado es:", maximum)
print("El mínimo valor ingresado es:", minimum)