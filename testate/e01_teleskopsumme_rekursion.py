#imports 
from time import time

#start runtimer
stimer = time()


def t(integer: int):
    if integer == 0 or integer == 1:
        return 0
    elif integer == 2:
        return 1
    else:
        return t(integer - 3) + t(integer - 2) + t(integer - 1)

#test section
for index in range(4, 11):
    print(t(index) / t(index - 1))

print("runtime:\n", time()-stimer,"sec")