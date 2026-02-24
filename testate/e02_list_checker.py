#imports 
from math import prod
from time import time

#start runtimer
stimer =time()

#check list
def d(array_list: list):
    change_list = [1]
    for index in range(1, len(array_list)):
        if array_list[index - 1] < array_list[index]:
            change_list.append(1)
        else:
            change_list.append(-1)

    return change_list

#using math.prod to determine parity of a permuation
def vo(array_list: list):
    print(prod(d(array_list)))

#test section
test = [1, 2, -3, -7, -1, -2, 4]
print("parity of test sequence:\n", d(test))
print("parity of the test permutation:")
vo(test)
print("runtime:\n", time()-stimer, "sec")
