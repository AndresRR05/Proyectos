import numpy as np
from scipy.integrate import quad

# Definir las funciones x(t) y y(t)
def x(t):
    return 4 * np.cos(t)

def y(t):
    return 8 * np.sin(8 * t)

# Derivadas dx/dt y dy/dt
def dx_dt(t):
    return -4 * np.sin(t)

def dy_dt(t):
    return 8 * 8 * np.cos(8 * t)

# Expresión dentro de la integral para la superficie de revolución
def integrand(t):
    return 2 * np.pi * y(t) * np.sqrt(dx_dt(t)**2 + dy_dt(t)**2)

# Calcular la integral
a, b = 0, 2 * np.pi
superficie, error = quad(integrand, a, b)

print(f"Superficie de revolución: {superficie:.2f} unidades cuadradas")
