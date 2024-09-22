# Datos de los salarios
import numpy as np


salarios = [2400, 2400, 2400, 2400, 2400, 2400, 2400, 2400, 2550, 2550, 
            2650, 2650, 2800, 2800, 2900, 3000, 3050, 3250, 3300, 3400]

# a. Calcular el rango
rango = max(salarios) - min(salarios)

# b. Calcular la media muestral
media_muestral = np.mean(salarios)

# c. Calcular la varianza muestral (s^2)
varianza_muestral = np.var(salarios, ddof=1)

# d. Calcular el desvío estándar muestral (s)
desvio_muestral = np.sqrt(varianza_muestral)

# e. Calcular el coeficiente de variación (CV)
coef_variacion = (desvio_muestral / media_muestral) * 100

rango, varianza_muestral, desvio_muestral, coef_variacion

# Datos de la muestra
datos = [12, 25, 15, 21, 10]

# Calcular la media de la muestra
media_muestra = np.mean(datos)

# Calcular el desvío estándar muestral
desvio_muestral = np.std(datos, ddof=1)

# Calcular los puntos z para cada observación
puntos_z = [(x - media_muestra) / desvio_muestral for x in datos]

media_muestra, desvio_muestral, puntos_z