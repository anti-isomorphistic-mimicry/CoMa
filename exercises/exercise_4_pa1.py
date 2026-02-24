# Robert Jerye

import math
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(start=0,
                stop=2*math.pi,
                num=100)
n = 8

def my_sin (x_values, n_iterations):
    
    def sin_polynomial (x, n):
        return math.pow(-1,n)*((math.pow(x,2*n+1))/(math.factorial(2*n+1)))
    
    result = []
    for i in x_values:

        x_result = 0
        
        for j in range(n_iterations+1):
            x_result = x_result+sin_polynomial(i,j)
        
        result.append(x_result)


    return result#

def comp_list_sins (x_values, n_iterations):

    approx_list = my_sin(x_values,n_iterations)

    sin_list = []
    for i in x_values: 
        sin_list.append(math.sin(i))
    
    return [x_values, approx_list, sin_list]

fig = plt.figure()

ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

ax.plot(comp_list_sins(x,n)[0], comp_list_sins(x,n)[1], label='approx')
ax.plot(comp_list_sins(x,n)[0], comp_list_sins(x,n)[2], label='math.sin')
ax.legend()

plt.show()
