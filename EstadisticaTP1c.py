import matplotlib.pyplot as plt
import numpy as np

# Datos de las variables X y Y
X = [5, 8, 20, 30, 50]
Y = [30, 20, 20, 40, 25]

# a. Diagrama de dispersión
plt.scatter(X, Y)
plt.title("Diagrama de Dispersión")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()

# c. Calcular la covarianza muestral
covarianza_muestral = np.cov(X, Y, ddof=1)[0][1]

# d. Calcular el coeficiente de correlación de Pearson
coef_correlacion = np.corrcoef(X, Y)[0][1]

covarianza_muestral, coef_correlacion

# Nuevos datos de las variables X y Y
X_new = [20, 17, 17, 14, 16, 12, 14, 18]
Y_new = [32, 26, 24, 26, 26, 24, 20, 26]

# a. Diagrama de dispersión para las nuevas observaciones
plt.scatter(X_new, Y_new)
plt.title("Diagrama de Dispersión")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()

# c. Calcular la covarianza muestral
covarianza_muestral_new = np.cov(X_new, Y_new, ddof=1)[0][1]

# d. Calcular el coeficiente de correlación de Pearson
coef_correlacion_new = np.corrcoef(X_new, Y_new)[0][1]

covarianza_muestral_new, coef_correlacion_new