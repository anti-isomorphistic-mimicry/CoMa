# imports
from time import time
from random import uniform
from math import sqrt, log

# start runtimer
stimer = time()


def cm():

    a, b, c = 0, 0, 2

    while c > 1:
        a = uniform(-1, 1)
        b = uniform(-1, 1)
        c = a * a + b * b

    result = a * sqrt((-2 * log(c)) / c)
    return result


# test section

values = [cm() for _ in range(1000)]
print(sum(values) / (len(values)))
print("runtime: \n", time() - stimer, "sec")
