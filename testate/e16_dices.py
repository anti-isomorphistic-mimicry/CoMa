# imports

from random import randint
from time import time

# start runtimer

stimer = time()

print("please enter the dices rolles:")
text = input()

# split up the string
split_text = text.split("+")
split_text = [split_text[i].split("d") for i in range(len(split_text))]

sum = 0

for i in range(len(split_text)):

    # case for dice rolls
    if len(split_text[i]) == 2:

        if split_text[i][0] == "":
            split_text[i][0] = 1  # type: ignore

        # convert to int
        split_text[i][0] = int(split_text[i][0])
        split_text[i][1] = int(split_text[i][1])

        # sum up the rolls
        for j in range(int(split_text[i][0] + 1)):
            pass
            sum = sum + randint(1, split_text[i][1])

    # adding cosntants
    if len(split_text[i]) == 1:
        pass
        split_text[i] = int(split_text[i][0])
        sum += split_text[i]

# return results
print("result of the dice roll:\n", sum)
print("runtime: \n", time() - stimer, "sec")

