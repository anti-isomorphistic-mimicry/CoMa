# Robert Jerye 

import numpy as np

def squares(n):
    return n * n

def makeSquare(size):

    """
    My idea is to move from the outside inwards
    """
    # Generate square values up to size^2
    square_values = [squares(i) for i in range(1, size * size + 1)]
    # reverse the order
    square_values = sorted(square_values, reverse=True)  

    #initialize the matrix with all zeroes
    matrix = np.zeros((size, size), dtype=int)

    #counter to keep track of the current square value
    counter = 0

    #boundary variables
    left =0
    right = size-1
    top = 0
    bottom = size - 1

    # break condition
    while left <= right and top <= bottom:

        # Move right
        for i in range(left, right + 1):
            matrix[top][i] = square_values[counter]
            counter += 1
        
        # reducing boundary
        top += 1

        # Move down
        for i in range(top, bottom + 1):
            matrix[i][right] = square_values[counter]
            counter += 1
        
        # reducing boundary
        right -= 1

        # Move left
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = square_values[counter]
            counter += 1
        
        # reducing boundary
        bottom -= 1

        # Move up
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = square_values[counter]
            counter += 1
        
        # reducing boundary
        left += 1

    return matrix


print(makeSquare(3))
print('-----------------------')
print(makeSquare(4))
print('-----------------------')
print(makeSquare(11))