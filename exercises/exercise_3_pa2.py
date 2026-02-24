# Robert Jerye

# CoMa week 3 exercise 2 merge sort


def merge_sort (input_list=list):

    # check if the list lenght is uneven if so save the last element and remove it fro the list
    last_element = 0
    if len(input_list)%2 != 0 :
        last_element = input_list[len(input_list)]
        input_list.pop
    
    # deternime number of iterations 
    while len(input_list) != 1 :
        