#imports
from fractions import Fraction
import math
from time import time

#start runtimer
stimer = time()

def fac(n):
    if n == 0:
        return 1
    return n * fac(n - 1)

def glied(k):
    return Fraction(fac(4 * k), fac(k) ** 4) * Fraction(
        26390 * k + 1103, 396 ** (4 * k)
    )

def ramapi(k):

    sum = 0

    for i in range(k + 1):
        sum = sum + glied(i)

    factor = math.sqrt(8) * Fraction(1, 9801)
    sum = factor * sum
    return sum

#test section
print("difference betweenabs((1 / math.pi) - ramapi(4): \n",
    (1 / math.pi) - ramapi(4))
print("Program runtime:\n", time() - stimer, "sec")