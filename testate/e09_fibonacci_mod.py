# imports
from time import time

# program timer
start_timer = time()


def F(number: int, modulo: int):
    if number == 1:
        return 1
    elif number == 2:
        return 2
    else:
        a = 1
        b = 2
        for i in range(3, number + 1):
            a = b
            b = (a + b) % modulo
        return b


folge_glieder = [F(i, 37) for i in range(41)]

print("first 40 elements of the sequence:\n", folge_glieder)
print("average of the first 40 elements:\n", sum(folge_glieder) / len(folge_glieder))

print("runtime:\n", time() - start_timer, "sec")
