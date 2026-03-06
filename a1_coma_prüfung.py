"""
name:           Robert Jerye
matrikelnummer: 21836685
studonid:       uz67izax
date:           06/03/2026
subject:        CoMa 1
"""

# imports
from time import time
from fractions import Fraction
import math

# start runtimer
stimer = time()


def glied(k: int):

    result = 0

    return result


def seq_approx(n: int):

    result = 0

    for i in range(n + 1):
        result += glied(i)

    return result


print("program runtime:\n", time() - stimer, "sec")
