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


def shuffle_ord(ls: list):
    counter = 0

    once = perfect_shuffle(ls)

    while not once == ls:
        once = perfect_shuffle(once)
        counter = counter + 1

    return counter


lst1 = range(1, 12)
print(shuffle_ord(lst1))
