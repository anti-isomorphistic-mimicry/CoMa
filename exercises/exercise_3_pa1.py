# Robert Jerye


# CoMa week 3 exercise 1 bubble sort


def bubble_sort(input_list=list):
    """
    takes a list as an arguement, iterates over the list until it is fully sorted and returns the fully sorted list
    """
    # check if the input_list is already sorted
    for i in range(len(input_list) - 1):
        for i in range(len(input_list) - 1):
            if input_list[i] > input_list[i + 1]:
                short_storage = input_list[i]
                input_list[i] = input_list[i + 1]
                input_list[i + 1] = short_storage

    return print(input_list)


# test area
numbers = [1, 235, 2, 563, 236, 93, 125, 61]

bubble_sort(numbers)
