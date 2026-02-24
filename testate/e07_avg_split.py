#imports
from time import time

#start runtimer
stimer =time()


def avg(l: list):
    return sum(l)/len(l)

#test section 1
print("avg([1.2, 3.2, 2.5])(numerical): \n",avg([1.2, 3.2, 2.5]))

def ws(l: list, n: int):
    result = []
    for index in range(int(len(l) - n + 1)):
        result.append([l[index], l[index + 1], l[index + 2]])

    return result

#test section 2
print("ws([10, 18, 48, 37, 29, 7, 36, 31, 12, 34, 3, 32], 3: \n",
    ws([10, 18, 48, 37, 29, 7, 36, 31, 12, 34, 3, 32], 3))
print("runtime: \n", time()-stimer, "sec")