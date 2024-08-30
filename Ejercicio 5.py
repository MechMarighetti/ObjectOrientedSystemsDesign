## Escribir una función que permita calcular la duración en segundos de un intervalo dado en horas, minutos y segundos.

def cuantosSegundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos

print(cuantosSegundos(2,4,3))

