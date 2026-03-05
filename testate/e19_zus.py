# imports

from time import time

# start timer

stimer = time()

w = []


def weird_check(u: list, v: list):

    i, j = 0, 0

    while i < len(u) and j < len(v):
        if u[i] < v[j]:
            w.append(u[i])
            i += 1
        else:
            w.append(v[j])
            j += 1

    if len(u) < len(v):
        for i in range(len(u), len(v)):
            w.append(v[i])
    if len(v) < len(u):
        for i in range(len(v), len(u)):
            w.append(u[i])

    return w


test_list_1 = [1, 1, 3, 3, 4, 11]
test_list_2 = [0, 0, 2, 5, 7, 9, 13]

print(weird_check(test_list_1, test_list_2))
print("runtimer: \n", time() - stimer, "sec")
