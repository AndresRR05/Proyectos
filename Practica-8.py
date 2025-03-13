import matplotlib.pyplot as plt
import numpy as np

def cartesian_to_polar(x, y):
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    return r, theta

# Puntos cartesianos
puntos = [(-100, 15), (30, 150), (-70, -80), (45, -10), (0, 80)]

for punto in puntos:
    x, y = punto
    r, theta = cartesian_to_polar(x, y)
    
    # Convertir theta a grados
    theta_deg = np.degrees(theta)
    
    # Crear figura y ejes
    fig, ax = plt.subplots()
    
    # Graficar punto
    ax.scatter(x, y, color='blue', label='Punto cartesiano')
    
    # Graficar línea desde el origen al punto
    ax.plot([0, x], [0, y], color='gray', linestyle='--')
    
    # Configurar límites de los ejes
    ax.set_xlim(-120, 180)
    ax.set_ylim(-100, 180)
    
    # Agregar texto con las coordenadas polares
    ax.text(0.5, 0.9, f'r = {r:.2f}\nθ = {theta_deg:.2f}°', transform=ax.transAxes)
    
    # Agregar leyenda
    ax.legend()
    
    # Mostrar la gráfica
    plt.show()