import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir las funciones
def g(x, y):
    return np.sqrt(9 - x*2 - y*2)

def h(x, y):
    return np.sqrt(16 - x*2 - y*2)

def f(x, y):
    return 16 - (x - 3)*2 - (y - 2)*2

# Crear una malla de puntos en el dominio de las funciones
x = np.linspace(-4, 4, 400)
y = np.linspace(-4, 4, 400)
x, y = np.meshgrid(x, y)

# Calcular los valores de z usando las funciones g(x, y), h(x, y) y f(x, y)
z_g = g(x, y)
z_h = h(x, y)
z_f = f(x, y)

# Crear la figura y los ejes 3D
fig = plt.figure(figsize=(18, 6))

# Gráfica de g(x, y)
ax1 = fig.add_subplot(131, projection='3d')
ax1.plot_surface(x, y, z_g, cmap='viridis')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('Gráfica de g(x, y) = (9 - x^2 - y^2)')

# Gráfica de h(x, y)
ax2 = fig.add_subplot(132, projection='3d')
ax2.plot_surface(x, y, z_h, cmap='plasma')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_title('Gráfica de h(x, y) = (16 - x^2 - y^2)')

# Gráfica de f(x, y)
ax3 = fig.add_subplot(133, projection='3d')
ax3.plot_surface(x, y, z_f, cmap='coolwarm')
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')
ax3.set_title('Gráfica de f(x, y) = 16 - (x - 3)^2 - (y - 2)^2')

# Mostrar las gráficas
plt.show()