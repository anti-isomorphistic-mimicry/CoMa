# import
from time import time
from math import floor, ceil

# start runtimer
stimer = time()


def perfect_shuffle(ls: list):

    split_1, split_2 = [], []

    if not len(ls) % 2 == 0:
        split_1 = ls[0 : ceil(len(ls) / 2) + 1]
        split_2 = ls[ceil(len(ls) / 2) : len(ls)]
    else:
        split_1 = ls[0 : floor(len(ls) / 2)]
        split_2 = ls[ceil(len(ls) / 2) : len(ls)]

    new_list = []
    for i in range(floor(len(ls) / 2) + 1):
        try:
            new_list.append(split_1[i])
        except:
            break
        try:
            new_list.append(split_2[i])
        except:
            break

    return new_list


# test section
ls = range(19)
ls_2 = range(20, 0, -1)

print("shufffle list 1 = range(19):\n", perfect_shuffle(ls=ls))
print("shuffle list 2 = range(20,0,-1):\n", perfect_shuffle(ls=ls_2))

print("runtime:\n", time() - stimer, "sec")
