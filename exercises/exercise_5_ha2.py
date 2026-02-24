# Robert Jerye

def divide(dividen:(list),divisor:(list)):
    
    result = []
    remainder = dividen.copy()

    # calulating the degree of each polynomial
    degree_p = len(dividen) - 1
    degree_q = len(divisor) - 1

    # determine the amount of steps
    steps = degree_p - degree_q

    for _ in range(steps + 1):
        if len(remainder) < len(divisor):
            break

        # divide the two polynomials
        factor = remainder[0] / divisor[0]
        result.append(factor)

        # subtract the devised polynomial from the remainder
        for i in range(len(divisor)):
            remainder[i] -= factor * divisor[i]

        # remove all leading zeroes
        while len(remainder) > 0 and remainder[0] == 0:
            remainder.pop(0)

    return result, remainder

i =[1,2,1]
j =[1,1]

print(divide(i,j))