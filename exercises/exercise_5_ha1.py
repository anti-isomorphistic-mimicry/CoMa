# Robert Jerye

import numpy as np


def multiply(p: list, q: list):

    # Create a list to hold all the coefficients and initialize them with zeroes
    coeff = np.zeros(len(p) + len(q) - 1)

    # the combination of indices of the original lists determine the exponent of the polynomial
    for i in range(len(p)):
        for j in range(len(q)):
            coeff[i + j] = coeff[i + j] + (p[i] * q[j])

    return coeff


# test environment

i = [-4, 3, 2, 1, 1, 1]
j = [5, 3, 1, 0, 4]


print(multiply(i, j))
