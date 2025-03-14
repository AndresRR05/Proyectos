import matplotlib.pyplot as plt
import numpy as np

def polar_to_cartesian(r, theta):
    x = r * np.cos(np.radians(theta))
    y = r * np.sin(np.radians(theta))
    return x, y

# Puntos polares (r, theta en grados)
puntos = [(100, 125), (70, 45), (90, 280), (35, 0), (95, 90)]

for punto in puntos:
    r, theta = punto
    x, y = polar_to_cartesian(r, theta)
    
    # Crear figura y ejes
    fig, ax = plt.subplots()
    
    # Graficar punto
    ax.scatter(x, y, color='red', label='Punto cartesiano')
    
    # Graficar línea desde el origen al punto
    ax.plot([0, x], [0, y], color='gray', linestyle='--')
    
    # Configurar límites de los ejes
    ax.set_xlim(-120, 120)
    ax.set_ylim(-120, 120)
    
    # Agregar texto con las coordenadas cartesianas
    ax.text(0.5, 0.9, f'x = {x:.2f}\ny = {y:.2f}', transform=ax.transAxes)
    
    # Agregar leyenda
    ax.legend()
    
    # Mostrar la gráfica
    plt.show()