import numpy as np
import matplotlib.pyplot as plt

# Definir las funciones
def a(t):
    return np.sqrt(2*t + 4), 2*t + 1

def b(t):
    return 4*np.cos(t), 3*np.sin(t)

def c(t):
    return t, 2*t**2 - 3

def d(t):
    return 3*t - 2, 18*t**2 - 24*t + 6

def e(t):
    return 3*np.cos(t) + np.cos(3*t), 3*np.sin(t) - np.sin(3*t)

# Crear los valores de t
t_a = np.linspace(-2, 6, 400)
t_b = np.linspace(0, 2*np.pi, 400)
t_c = np.linspace(0, 10, 400)
t_d = np.linspace(0, 10, 400)
t_e = np.linspace(0, 2*np.pi, 400)

# Graficar las funciones
fig, axs = plt.subplots(3, 2, figsize=(12, 18))

# Gráfica a
x_a, y_a = a(t_a)
axs[0, 0].plot(x_a, y_a)
axs[0, 0].set_title('a) x(t) = √(2t + 4), y(t) = 2t + 1')
axs[0, 0].grid(True)

# Gráfica b
x_b, y_b = b(t_b)
axs[0, 1].plot(x_b, y_b)
axs[0, 1].set_title('b) x(t) = 4cos(t), y(t) = 3sin(t)')
axs[0, 1].grid(True)

# Gráfica c
x_c, y_c = c(t_c)
axs[1, 0].plot(x_c, y_c)
axs[1, 0].set_title('c) x(t) = t, y(t) = 2t² − 3')
axs[1, 0].grid(True)

# Gráfica d
x_d, y_d = d(t_d)
axs[1, 1].plot(x_d, y_d)
axs[1, 1].set_title('d) x(t) = 3t – 2, y(t) = 18t² − 24t + 6')
axs[1, 1].grid(True)

# Gráfica e
x_e, y_e = e(t_e)
axs[2, 0].plot(x_e, y_e)
axs[2, 0].set_title('e) x(t) = 3cos(t) + cos(3t), y(t) = 3sin(t) – sin(3t)')
axs[2, 0].grid(True)

# Eliminar el sexto subplot vacío
fig.delaxes(axs[2, 1])

# Ajustar el diseño
plt.tight_layout()
plt.show()