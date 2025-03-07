import numpy as np
import matplotlib.pyplot as plt

# Circunferencia
# x = r * cos(t)
# y = r * sin(t)
r = 1
t = np.linspace(0, 2 * np.pi, 1000)
x_circ = r * np.cos(t)
y_circ = r * np.sin(t)

plt.figure()
plt.plot(x_circ, y_circ)
plt.title('Circunferencia')
plt.axis('equal')
plt.show()

# Cicloide
# x = r * (t - sin(t))
# y = r * (1 - cos(t))
r = 1
x_cic = r * (t - np.sin(t))
y_cic = r * (1 - np.cos(t))

plt.figure()
plt.plot(x_cic, y_cic)
plt.title('Cicloide')
plt.axis('equal')
plt.show()

# Hipocicloide
# x = (R - r) * cos(t) + r * cos((R - r) / r * t)
# y = (R - r) * sin(t) - r * sin((R - r) / r * t)
R = 5
r = 3
x_hipo = (R - r) * np.cos(t) + r * np.cos((R - r) / r * t)
y_hipo = (R - r) * np.sin(t) - r * np.sin((R - r) / r * t)

plt.figure()
plt.plot(x_hipo, y_hipo)
plt.title('Hipocicloide')
plt.axis('equal')
plt.show()

# Astroide
# x = a * cos^3(t)
# y = a * sin^3(t)
a = 1
x_ast = a * np.cos(t)**3
y_ast = a * np.sin(t)**3

plt.figure()
plt.plot(x_ast, y_ast)
plt.title('Astroide')
plt.axis('equal')
plt.show()

# Lemniscata (símbolo de infinito)
# x = a * cos(t)
# y = a * sin(t) * cos(t)
a = 1
x_lem = a * np.cos(t)
y_lem = a * np.sin(t) * np.cos(t)

plt.figure()
plt.plot(x_lem, y_lem)
plt.title('Lemniscata')
plt.axis('equal')
plt.show()

# Cardioide
# x = a * (1 - cos(t)) * cos(t)
# y = a * (1 - cos(t)) * sin(t)
a = 1
x_car = a * (1 - np.cos(t)) * np.cos(t)
y_car = a * (1 - np.cos(t)) * np.sin(t)

plt.figure()
plt.plot(x_car, y_car)
plt.title('Cardioide')
plt.axis('equal')
plt.show()