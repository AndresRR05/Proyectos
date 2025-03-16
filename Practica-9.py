import sympy as sp

# Definir las variables
t = sp.symbols('t')

# Ejercicio 1
r1 = sp.Matrix([sp.sqrt(t) - 3, t**2, sp.tan(t)])
lim_r1 = r1.limit(t, 4)
print("Límite de r(t) cuando t tiende a 4:")
print(r1)
print("\nResultado:")
sp.pprint(lim_r1)

# Ejercicio 2
r2 = sp.Matrix([sp.exp(t), sp.sin(t), sp.ln(t)])
lim_r2 = r2.limit(t, sp.pi)
print("\nLímite de r(t) cuando t tiende a π:")
print(r2)
print("\nResultado:")
sp.pprint(lim_r2)

# Ejercicio 3
r3_1 = sp.Matrix([sp.exp(2*t), t**3 + 1, sp.atan(2*t)])
lim_r3_1 = r3_1.limit(t, sp.oo)
print("\nLímite de r(t) cuando e^t tiende a infinito:")
print(r3_1)
print("\nResultado:")
sp.pprint(lim_r3_1)

r3_2 = sp.Matrix([sp.cosh(t), sp.asinh(t), sp.ln(t)])
lim_r3_2 = r3_2.limit(t, sp.oo)
print("\nLímite de r(t) cuando t tiende a infinito:")
print(r3_2)
print("\nResultado:")
sp.pprint(lim_r3_2)
