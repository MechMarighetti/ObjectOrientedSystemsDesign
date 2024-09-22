##Ejercicio 4
##Autor: Mercedes Marighetti

""" Escribe un programa en Python que solicite 5 números enteros al
usuario. El mismo debe indicar si entre dichos valores hay números
duplicados o no, imprimiendo por pantalla “HAY DUPLICADOS” o “SON
TODOS DISTINTOS”. """
numeros = []
i = 0
for i in range(5) :
    num = int(input("Ingresá un numero: "))
    numeros.append(num)
    i += 1
    """ SET coleccion desordenada y mutable de diferentes tipos inmutables """
    conjunto = set(numeros)
    

if len(numeros) == len(conjunto):
    print("SON TODOS DISTINTOS")
else:
    print("HAY DUPLICADOS")