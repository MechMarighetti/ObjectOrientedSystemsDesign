
## Usando la función del ejercicio anterior, escribir un programa que pida al usuario dos intervalos expresados en horas, minutos y segundos, sume sus duraciones, y muestre por pantalla la duración total en horas, minutos y segundos.


def cuantosSegundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos

def sumarHoras(horas1, minutos1, segundos1, horas2, minutos2, segundos2):
    duracion1 = cuantosSegundos(horas1, minutos1, segundos1)
    duracion2 = cuantosSegundos(horas2, minutos2, segundos2)
    duracion_total = duracion1 + duracion2
    return duracion_total

def sumarHoras2(*otros): ##una tupla puede contender listas como elementos
    for i in otros:
        horas2 = i[0]
        minutos2 = i[1]
        segundos2 = i[2]
    duracion2 = cuantosSegundos(horas2, minutos2, segundos2)
    duracion_total = duracion_total + duracion2
    return duracion_total

def segundosAHoras(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    return horas, minutos, segundos_restantes

# Primer horario a sumar
horas1 = int(input("Ingrese las horas: "))
minutos1 = int(input("Ingrese los minutos: "))
segundos1 = int(input("Ingrese los segundos: "))

# Segundo horario a sumar
horas2 = int(input("Ingrese las horas: "))
minutos2 = int(input("Ingrese los minutos: "))
segundos2 = int(input("Ingrese los segundos: "))

horas_total, minutos_total, segundos_total = segundosAHoras(sumarHoras2([horas1, minutos1, segundos1], [horas2, minutos2, segundos2]))

print(f"La duración total es: {horas_total} horas, {minutos_total} minutos, y {segundos_total} segundos.")