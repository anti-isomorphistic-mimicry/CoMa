#imports
from time import time

#start runtimer
stimer = time()

def pro(ls: list):

    switch = False

    for index in range(int(len(ls) - 2)):
        if (ls[index] + 2 == ls[index + 1]) and (ls[index] + 1 == ls[index + 2]):
            switch = True

    return switch

#test section

test_list_1 = [1, 2, 3, 3, 4, 4, 8, 1]
test_list_2 = [1, 3, 2, 4, 4, 4, 4, 4]
test_list_3 = [4, 4, 4, 4, 1, 3, 2]

print("list_1:\n", test_list_1, "\n", pro(test_list_1))
print("list_2:\n", test_list_2, "\n", pro(test_list_2))
print("list_3:\n", test_list_3, "\n", pro(test_list_3))

print("runtime:\n", time() - stimer, "sec")
