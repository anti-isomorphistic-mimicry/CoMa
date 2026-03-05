# imports
from time import time
from math import comb, pow, pi
from fractions import Fraction

# start timer
stimer = time()


def glied(k: int):

    comb_factor = int(pow(comb(2 * k, k), 2))

    fac_1 = Fraction(comb_factor, k + 1)
    fac_2 = Fraction(1, 16**k)
    return fac_1 * fac_2


def sequence(n: int):
    seq_sum = sum([glied(i) for i in range(n + 1)])
    seq_sum = seq_sum * Fraction(1, 4)
    return seq_sum


for approx in range(20):
    print("difference '1/pi - sequence(", approx, ")':", (1 / pi) - sequence(approx))

print("runtime:\n", time() - stimer, "sec")
