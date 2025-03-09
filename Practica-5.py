import numpy as np
import matplotlib.pyplot as plt

# Función para calcular la derivada y la línea tangente
def tangent_line(x_func, y_func, t, t_val, num_points=100):
    # Calcular la derivada
    dx_dt = np.gradient(x_func)
    dy_dt = np.gradient(y_func)
    
    # Evaluar en el punto t_val
    dx = np.interp(t_val, t, dx_dt)
    dy = np.interp(t_val, t, dy_dt)
    
    # Coordenadas del punto
    x_point = np.interp(t_val, t, x_func)
    y_point = np.interp(t_val, t, y_func)
    
    # Ecuación de la recta tangente: y - y0 = m(x - x0)
    m = dy / dx if dx != 0 else np.inf
    x_tangent = np.linspace(x_point - 5, x_point + 5, num_points)
    y_tangent = m * (x_tangent - x_point) + y_point
    
    return x_tangent, y_tangent, (x_point, y_point)

# a) X(t) = e^t, Y(t) = cos(t), t = π/4
t_a = np.linspace(0, np.pi / 2, 100)
x_a = np.exp(t_a)
y_a = np.cos(t_a)

# b) X(t) = 3t^2, Y(t) = t^3, t = 2
t_b = np.linspace(0, 3, 100)
x_b = 3 * t_b**2
y_b = t_b**3

# c) X(t) = t * sin(t), Y(t) = 4t, t = π/2
t_c = np.linspace(0, np.pi, 100)
x_c = t_c * np.sin(t_c)
y_c = 4 * t_c

# d) X(t) = t^2, Y(t) = e^(2t), t = 1
t_d = np.linspace(0, 2, 100)
x_d = t_d**2
y_d = np.exp(2 * t_d)

# Graficar
plt.figure(figsize=(12, 10))

# a)
plt.subplot(2, 2, 1)
x_tangent_a, y_tangent_a, point_a = tangent_line(x_a, y_a, t_a, np.pi/4)
plt.plot(x_a, y_a, label='Curva a: $X(t) = e^t$, $Y(t) = \cos(t)$')
plt.plot(x_tangent_a, y_tangent_a, label='Tangente en t=π/4', linestyle='--', color='orange')
plt.scatter(*point_a, color='red')
plt.title('Curva "a" y Tangente')
plt.legend()

# b)
plt.subplot(2, 2, 2)
x_tangent_b, y_tangent_b, point_b = tangent_line(x_b, y_b, t_b, 2)
plt.plot(x_b, y_b, label='Curva b: $X(t) = 3t^2$, $Y(t) = t^3$')
plt.plot(x_tangent_b, y_tangent_b, label='Tangente en t=2', linestyle='--', color='orange')
plt.scatter(*point_b, color='red')
plt.title('Curva "b" y Tangente')
plt.legend()

# c)
plt.subplot(2, 2, 3)
x_tangent_c, y_tangent_c, point_c = tangent_line(x_c, y_c, t_c, np.pi/2)
plt.plot(x_c, y_c, label='Curva c: $X(t) = t \sin(t)$, $Y(t) = 4t$')
plt.plot(x_tangent_c, y_tangent_c, label='Tangente en t=π/2', linestyle='--', color='orange')
plt.scatter(*point_c, color='red')
plt.title('Curva "c" y Tangente')
plt.legend()

# d)
plt.subplot(2, 2, 4)
x_tangent_d, y_tangent_d, point_d = tangent_line(x_d, y_d, t_d, 1)
plt.plot(x_d, y_d, label='Curva d: $X(t) = t^2$, $Y(t) = e^{2t}$')
plt.plot(x_tangent_d, y_tangent_d, label='Tangente en t=1', linestyle='--', color='orange')
plt.scatter(*point_d, color='red')
plt.title('Curva "d" y Tangente')
plt.legend()

plt.tight_layout()
plt.show()