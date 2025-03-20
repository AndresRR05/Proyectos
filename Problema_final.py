import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Límites del rectángulo original
x_min_original = 0
x_max_original = 8
y_min_original = 0
y_max_original = 5

# Límites del rectángulo resultante
x_min_recorte = 2
x_max_recorte = 6
y_min_recorte = 1
y_max_recorte = 3

# Cálculo del área del rectángulo resultante
ancho = x_max_recorte - x_min_recorte
alto = y_max_recorte - y_min_recorte
area_recorte = ancho * alto

print(f"El área del rectángulo resultante es: {area_recorte} unidades cuadradas")

# Crear la figura y los ejes para graficar
fig, ax = plt.subplots()

# Dibujar el rectángulo original
original_rect = patches.Rectangle((x_min_original, y_min_original), 
                                   x_max_original - x_min_original, 
                                   y_max_original - y_min_original, 
                                   linewidth=2, edgecolor='blue', facecolor='none', label="Original")
ax.add_patch(original_rect)

# Dibujar el rectángulo resultante
recorte_rect = patches.Rectangle((x_min_recorte, y_min_recorte), 
                                  ancho, alto, 
                                  linewidth=2, edgecolor='red', facecolor='none', label="Recorte")
ax.add_patch(recorte_rect)

# Configuración de la gráfica
ax.set_xlim(-1, 9)
ax.set_ylim(-1, 6)
ax.set_aspect('equal', adjustable='box')
ax.axhline(0, color='black',linewidth=0.5)
ax.axvline(0, color='black',linewidth=0.5)
ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.title("Rectángulo Original y Recorte")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Mostrar la gráfica
plt.show()