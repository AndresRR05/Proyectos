import numpy as np
from sympy import symbols, integrate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Declaramos las variables simbólicas
x, y, z = symbols('x y z')

# Definimos la función f(x, y, z)
f = 5 - 3*y

# Límites del tetraedro
def limites_x():
    return (0, 1)

def limites_y(x):
    return (0, 1 - x)

def limites_z(x, y):
    return (0, 1 - x - y)

# Calculamos el volumen de la función dentro del tetraedro
volumen = integrate(
    integrate(
        integrate(f, (z, *limites_z(x, y))),
        (y, *limites_y(x))),
    (x, *limites_x())
)

print(f"El volumen del tetraedro bajo la función es: {volumen.evalf()} unidades cúbicas")

# --- Gráfica del tetraedro ---
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Definimos los vértices del tetraedro
vertices = np.array([
    [0, 0, 0],  # Vértice en el origen
    [1, 0, 0],  # Vértice sobre el eje X
    [0, 1, 0],  # Vértice sobre el eje Y
    [0, 0, 1],  # Vértice sobre el eje Z
])

# Definimos las caras del tetraedro
caras = [
    [vertices[0], vertices[1], vertices[2]],
    [vertices[0], vertices[1], vertices[3]],
    [vertices[0], vertices[2], vertices[3]],
    [vertices[1], vertices[2], vertices[3]],
]

# Agregamos las caras al gráfico
poly3d = Poly3DCollection(caras, alpha=.5, linewidths=1, edgecolors='k')
poly3d.set_facecolor([0.5, 0.5, 1, 0.7])  # Color de las caras
ax.add_collection3d(poly3d)

# Configuramos los ejes
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.title("Tetraedro delimitado por los planos y la función")

plt.show()