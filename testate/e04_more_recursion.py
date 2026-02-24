#imports
from time import time

#start runtimer
stimer = time()


def F(n: int):
    if n == 0:
        return 0
    elif n > 0:
        return n - F(F(n - 1))


#test section
test_list = []
for i in range(31):
    test_list.append(F(i))
print("F(0) till F(30):\n", test_list)
print("program runtime:\n", time()-stimer, "sec")
