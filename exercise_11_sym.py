import sympy
from sympy import oo

print("Aufgabe 1")


n = sympy.symbols("n")
print(sympy.limit(((1 + 1 / n) ** n), n, oo))

print("-----------------------------")
print("Aufgabe 2")

n = sympy.symbols("n", integer=True)  # n sei eine natuerliche Zahl
x = sympy.symbols("x")
exp_xn = x**n / sympy.factorial(n)

print(sympy.summation(exp_xn.subs({x: 3}), [n, 0, oo]).evalf() == sympy.exp(3).evalf())

print("-----------------------------")
print("Aufgabe 3")


m_0 = sympy.Matrix(3, 3, list(range(1, 10)))
m_1 = sympy.Matrix(4, 4, list(range(1, 17)))
m_2 = sympy.Matrix(10, 10, list(range(1, 101)))

x_1, x_2, x_3 = sympy.symbols("x_1,x_2,x_3")
print(sympy.linsolve((m_0, sympy.Matrix([0, 0, 0])), [x_1, x_2, x_3]))

print("-----------------------------")
print("Aufgabe 4")


f_x = 1 / (x**3 - 1)
print(sympy.singularities(f_x, x))

print("-----------------------------")
print("Aufgabe 5")


sin_x = sympy.sin(x)

domain = sympy.Interval(-sympy.pi, (sympy.pi) / 4)

print(sympy.maximum(sin_x, symbol=x, domain=domain))
