#imports
from time import time
from math import floor, ceil

#messure runtime
stimer = time()


def mq(ls: list):

    #edge case len(list) ==1
    if len(ls) == 1:
        return [ls[0], ls[0], ls[0]]

    # sort list and split into sublists
    sorted_list = sorted(ls)
    split_bottom = sorted_list[0 : floor(len(sorted_list) / 2)]
    split_top = sorted_list[ceil(len(sorted_list) / 2) : len(ls) + 1]

    #helper function for the median
    def med(slist):

        hlen = int(len(slist) / 2)

        if len(slist) % 2 == 0:
            return (slist[hlen - 1] + slist[hlen]) / 2
        else:
            return slist[hlen]

    return [med(split_bottom), med(sorted_list), med(split_top)]


#test section
tsil = [9, 8, 7, 3, 6, 5, 4, 2, 1, 0]
tisl = [1, 2, 3]
l_0 = [1, 2]

print(mq(tsil))
print(mq(tisl))
print(mq(l_0))

print("runtime: \n", time() - stimer, "sec")
