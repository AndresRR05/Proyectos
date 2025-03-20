import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Definir los límites del recorte
x1, x2 = 2, 6
y1, y2 = 1, 3

# Calcular el área
ancho = x2 - x1
alto = y2 - y1
area = ancho * alto
print(f"El área de la lámina recortada es: {area} unidades cuadradas")

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Añadir el rectángulo original (por ejemplo, de 0 a 8 en x y de 0 a 4 en y)
rect_original = patches.Rectangle((0, 0), 8, 4, linewidth=1, edgecolor='r', facecolor='none', label='Original')
ax.add_patch(rect_original)

# Añadir el rectángulo recortado
rect_recortado = patches.Rectangle((x1, y1), ancho, alto, linewidth=1, edgecolor='b', facecolor='blue', alpha=0.5, label='Recortado')
ax.add_patch(rect_recortado)

# Configurar los límites de los ejes
ax.set_xlim(-2, 10)
ax.set_ylim(-2, 6)

# Añadir leyendas y etiquetas
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Lámina Recortada')

# Mostrar la gráfica
plt.show()