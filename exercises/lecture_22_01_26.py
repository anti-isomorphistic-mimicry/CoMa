from sympy import *

x, y, z = symbols("x y z")
V = Matrix([[1, x, x**2], [1, y, y**2], [1, z, z**2]])
print(V)
p = V.det()
print(p)
p12 = p.subs({"x": 1, "y": 2})
print(p12)
print(p12.subs({"z": 11}))


import sympy
import numpy as np


def vandermonde(v):
    m = list(range(len(v)))
    for i, w in enumerate(v):
        m[i] = [w**j for j in range(len(v))]
    return m


V = vandermonde([1.0 / i for i in range(1, 16)])

vnp = np.matrix(V)
vsy = sympy.Matrix(V)
print(np.linalg.matrix_rank(V))
print(vsy.rank())


coma.math.fau.de / testate.html
