# imports
from time import time
from math import floor, sqrt

# start runtimer
stimer = time()


def pentagon(k):

    return (k * (3 * k - 1)) / 2


def partition(n):

    if n == 0:
        return 1
    if n < 0:
        return 0

    uppper_boundary = int(1 + floor(sqrt((24 * n) + 1) / 6))

    pentagon_list_kpos = [pentagon(r) for r in range(uppper_boundary + 1)]
    pentagon_list_kneg = [pentagon(-1 * r) for r in range(uppper_boundary + 1)]

    k = 1
    summation = 0
    while k <= uppper_boundary:
        summation += (-1) ** (k - 1) * (
            partition(n - pentagon_list_kpos[k]) + partition(n - pentagon_list_kneg[k])
        )
        k += 1

    return summation


plist = []
for run in range(1, 50):
    plist.append(partition(run))

print(plist)
