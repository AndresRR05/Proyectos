import sympy as sp

# Definimos la variable simbólica
t = sp.symbols('t')
c = sp.symbols('c', real=True, constant=True)
f = sp.Function('f')(t)

# Definimos los componentes de los vectores r y u como funciones dependientes de t
r1, r2, r3 = sp.symbols('r1 r2 r3', cls=sp.Function)
u1, u2, u3 = sp.symbols('u1 u2 u3', cls=sp.Function)

# Asignamos las funciones a las variables de tiempo t para construir los vectores r y u
r = sp.Matrix([r1(t), r2(t), r3(t)])
u = sp.Matrix([u1(t), u2(t), u3(t)])

# Regla 1: Derivada de un escalar por un vector constante
def regla1(c, r):
    return c * sp.diff(r, t)

resultado1 = regla1(c, r)
print("Regla 1: Derivada de un escalar por un vector constante")
sp.pprint(resultado1)
print("\n")

# Regla 2: Derivada de la suma o resta de dos vectores
def regla2(r, u):
    return sp.diff(r, t) + sp.diff(u, t)

resultado2 = regla2(r, u)
print("Regla 2: Derivada de la suma o resta de dos vectores")
sp.pprint(resultado2)
print("\n")

# Regla 3: Derivada del producto de un escalar y un vector
def regla3(f, r):
    return f * sp.diff(r, t) + sp.diff(f, t) * r

resultado3 = regla3(f, r)
print("Regla 3: Derivada del producto de un escalar y un vector")
sp.pprint(resultado3)
print("\n")

# Regla 4: Derivada del producto punto de dos vectores
def regla4(r, u):
    return sp.diff(r, t).dot(u) + r.dot(sp.diff(u, t))

resultado4 = regla4(r, u)
print("Regla 4: Derivada del producto punto de dos vectores")
sp.pprint(resultado4)
print("\n")

# Regla 5: Derivada del producto cruz de dos vectores
def regla5(r, u):
    return sp.diff(r, t).cross(u) + r.cross(sp.diff(u, t))

resultado5 = regla5(r, u)
print("Regla 5: Derivada del producto cruz de dos vectores")
sp.pprint(resultado5)
print("\n")

# Regla 6: Derivada de la composición de una función con un vector
def regla6(f, r):
    return sp.diff(f, t) * sp.diff(r, t)

resultado6 = regla6(f, r)
print("Regla 6: Derivada de la composición de una función con un vector")
sp.pprint(resultado6)
print("\n")

# Regla 7: Verificar si el producto punto de un vector consigo mismo es constante
def regla7(r):
    return sp.Eq(sp.diff(r.dot(r), t), 0)

resultado7 = regla7(r)
print("Regla 7: Verificación de si el producto punto de un vector consigo mismo es constante")
sp.pprint(resultado7)
print("\n")

# Problema 1: Verificar la regla del producto punto para dos vectores específicos
def problema1(r, u):
    return sp.diff(r.dot(u), t) == r.diff(t).dot(u) + r.dot(u.diff(t))

r_esp = sp.Matrix([sp.sin(t), sp.cos(t), t])
u_esp = sp.Matrix([t**2, sp.exp(t), sp.log(t)])

resultado_problema1 = problema1(r_esp, u_esp)
print("Problema 1: Verificar la regla del producto punto para dos vectores específicos")
sp.pprint(resultado_problema1)
print("\n")

# Problema 2: Comprobar la regla del producto cruz para dos vectores específicos
def problema2(r, u):
    return sp.diff(r.cross(u), t) == r.diff(t).cross(u) + r.cross(u.diff(t))

r_esp2 = sp.Matrix([t, sp.sin(t), sp.cos(t)])
u_esp2 = sp.Matrix([sp.exp(t), t**2, sp.log(t)])

resultado_problema2 = problema2(r_esp2, u_esp2)
print("Problema 2: Comprobar la regla del producto cruz para dos vectores específicos")
sp.pprint(resultado_problema2)
print("\n")

# Problema 3: Verificar la regla de la composición de una función con un vector para funciones específicas
def problema3(f, r):
    return sp.Matrix([sp.diff(f.subs(t, r[i]), t) for i in range(r.shape[0])])

f_esp = t**2 + sp.sin(t)
r_esp3 = sp.Matrix([sp.exp(t), sp.log(t), t**3])

resultado_problema3 = problema3(f_esp, r_esp3)
print("Problema 3: Verificar la regla de la composición de una función con un vector para funciones específicas")
sp.pprint(resultado_problema3)
print("\n")