import numpy as np
from scipy.integrate import quad
# Parámetros del huevo de tamaño promedio
a = 3  # semieje mayor
b = 2  # semieje menor
# Definir funciones para el huevo en orientación horizontal
def x_horizontal(t):
    return a * np.cos(t)
def y_horizontal(t):
    return b * np.sin(t)
def dx_dt_horizontal(t):
    return -a * np.sin(t)
def dy_dt_horizontal(t):
    return b * np.cos(t)
def integrand_horizontal(t):
    return 2 * np.pi * np.abs(y_horizontal(t)) * np.sqrt(dx_dt_horizontal(t)**2 + dy_dt_horizontal(t)**2)
# Definir funciones para el huevo en orientación vertical
def x_vertical(t):
    return b * np.cos(t)
def y_vertical(t):
    return a * np.sin(t)
def dx_dt_vertical(t):
    return -b * np.sin(t)

def dy_dt_vertical(t):
    return a * np.cos(t)
# Ajuste para calcular la superficie de revolución alrededor del eje y para la orientación vertical
def integrand_vertical_adjusted(t):
    return 2 * np.pi * np.abs(x_vertical(t)) * np.sqrt(dx_dt_vertical(t)**2 + dy_dt_vertical(t)**2)
# Calcular las superficies de revolución
a, b = 0, 2 * np.pi
superficie_horizontal, _ = quad(integrand_horizontal, a, b)
superficie_vertical_adjusted, _ = quad(integrand_vertical_adjusted, a, b)
print(f"Superficie de revolución en orientación horizontal: {superficie_horizontal:.2f} unidades cuadradas")
print(f"Superficie de revolución en orientación vertical: {superficie_vertical_adjusted:.2f} unidades cuadradas")
