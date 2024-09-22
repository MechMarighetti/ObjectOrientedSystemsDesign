import numpy as np

# Datos: Intervalos de salarios y número de trabajadores
intervalos = [(2400, 2599), (2600, 2799), (2800, 2999), (3000, 3199), (3200, 3399), (3400, 3599)]
trabajadores = [7, 20, 15, 32, 12, 14]

# Calcular puntos medios de cada intervalo
puntos_medios = [(i[0] + i[1]) / 2 for i in intervalos]

# Total de trabajadores (población)
N = sum(trabajadores)

# Calcular la media poblacional (μ)
media_poblacional = sum(f * x for f, x in zip(trabajadores, puntos_medios)) / N

# Calcular la varianza poblacional (σ^2)
varianza_poblacional = sum(f * (x - media_poblacional) ** 2 for f, x in zip(trabajadores, puntos_medios)) / N

# Calcular la varianza muestral (s^2)
varianza_muestral = sum(f * (x - media_poblacional) ** 2 for f, x in zip(trabajadores, puntos_medios)) / (N - 1)

# Desvío estándar poblacional (σ)
desvio_poblacional = np.sqrt(varianza_poblacional)

# Desvío estándar muestral (s)
desvio_muestral = np.sqrt(varianza_muestral)

# Coeficiente de variación (CV)
coef_variacion = (desvio_poblacional / media_poblacional) * 100

media_poblacional, varianza_poblacional, varianza_muestral, desvio_poblacional, desvio_muestral, coef_variacion