#imports
from time import time

#start runtimer
stimer = time()

def soso(l: list) -> list:
    even = []
    odd = []
    for index in range(len(l)):
        if l[index] % 2 == 0:
            even.append(l[index])
        else:
            odd.append(l[index])

    result = sorted(even) + sorted(odd)

    return result


print("Test for range(20): \n", soso(range(20)))
print("Test for range(1,20,2): \n", soso(range(1, 20, 2)))
print("Test for range(0,21,2): \n", soso(range(0, 21, 2)))
print("runtime: \n", time() - stimer, "sec")