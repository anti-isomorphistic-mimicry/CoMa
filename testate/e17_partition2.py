# imports
from time import time

# start timer
stimer = time()


def p2(m, k):

    if m == 0 and k == 0:
        return 1

    if m <= 0 or k <= 0:
        return 0

    return p2(m - k, k) + p2(m - 1, k - 1)


# test section 1
print([p2(6, k) for k in range(7)])
print([p2(10, k) for k in range(11)])


def partion(n):
    results = [p2(n, i) for i in range(n + 1)]
    return sum(results)


# test section 2
print([partion(i) for i in range(31)])

print("runtime:\n", time() - stimer, "sec")
