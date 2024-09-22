#Escribir una función que reciba una muestra de números en una lista y retorne su media.

def calcular_media(lista_numeros):

    if len(lista_numeros) == 0:
        return "No se puede dividir por cero"  # Evitar división por cero si la lista está vacía

    suma = sum(lista_numeros)
    media = suma / len(lista_numeros)
    return media

# Ejemplo de uso
muestra = [150, 48, 22, 78, 12]
media = calcular_media(muestra)
print("La media de la muestra es: ", media)