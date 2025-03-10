import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Función para calcular la longitud de arco
def arc_length(fx, fy, fz, t0, t1):
    integrand = lambda t: np.sqrt(fx(t)**2 + fy(t)**2 + fz(t)**2)
    length, _ = quad(integrand, t0, t1)
    return length

# a) (2cos(t), 2sen(t), t) 0<=t <= 2π
t = np.linspace(0, 2*np.pi, 1000)
x_a = 2 * np.cos(t)
y_a = 2 * np.sin(t)
z_a = t
length_a = arc_length(lambda t: -2*np.sin(t), lambda t: 2*np.cos(t), lambda t: 1, 0, 2*np.pi)

plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x_a, y_a, z_a)
plt.title(f'Curva a) Longitud de arco: {length_a:.2f}')
plt.show()

# b) (1, 3t^2, t^3) 0<=t<=1
t = np.linspace(0, 1, 1000)
x_b = np.ones_like(t)
y_b = 3 * t**2
z_b = t**3
length_b = arc_length(lambda t: 0, lambda t: 6*t, lambda t: 3*t**2, 0, 1)

plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x_b, y_b, z_b)
plt.title(f'Curva b) Longitud de arco: {length_b:.2f}')
plt.show()

# c) (sen(3t), cos(3t), 2t^(3/2)) 0<=t<=1
t = np.linspace(0, 1, 1000)
x_c = np.sin(3*t)
y_c = np.cos(3*t)
z_c = 2 * t**(3/2)
length_c = arc_length(lambda t: 3*np.cos(3*t), lambda t: -3*np.sin(3*t), lambda t: 3/2 * t**(1/2), 0, 1)

plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x_c, y_c, z_c)
plt.title(f'Curva c) Longitud de arco: {length_c:.2f}')
plt.show()

# d) (t, t, t^2) 1<=t<=2
t = np.linspace(1, 2, 1000)
x_d = t
y_d = t
z_d = t**2
length_d = arc_length(lambda t: 1, lambda t: 1, lambda t: 2*t, 1, 2)

plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x_d, y_d, z_d)
plt.title(f'Curva d) Longitud de arco: {length_d:.2f}')
plt.show()

# e) (t, t*sin(t), t*cos(t)) 0<=t<=π
t = np.linspace(0, np.pi, 1000)
x_e = t
y_e = t * np.sin(t)
z_e = t * np.cos(t)
length_e = arc_length(lambda t: 1, lambda t: np.sin(t) + t*np.cos(t), lambda t: np.cos(t) - t*np.sin(t), 0, np.pi)

plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x_e, y_e, z_e)
plt.title(f'Curva e) Longitud de arco: {length_e:.2f}')
plt.show()



#Instala el spicy