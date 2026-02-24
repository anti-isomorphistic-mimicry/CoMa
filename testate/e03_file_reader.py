#imports
from time import time

#start runtimer
stimer =time()

#open plain text file 
def rein():

    number_list = []

    with open("/home/robert/Documents/uni_sync/CoMa/Prüfungsvorbereitung/e03_nums", "r") as file:
        for line in file:
            number_list.append(line.strip())


    return number_list


# test section 1

print("print result for rein():\n", rein())

#part2
def grosse(ls: list):

    selection = []
    for item in ls:
        convert = float(item)
        if abs(convert) > 1:
            selection.append(convert)

    return selection


# test section 2

print("print result for grosse(ls): \n", grosse(rein()))

print("print result for grosse(rein()) sorted: \n", sorted(grosse(rein())))

print("runtime:\n", time()-stimer, "sec")