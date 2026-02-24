#Robert Jerye

import random
import math
import time

start_time =time.time()

#Präsenzaufgabe 1

iterations = 100000
count = 0

for i in range(iterations):
    if math.sqrt(math.pow(random.random(),2)+math.pow(random.random(),2)) <= 1:
        count = count +1

print((count/iterations)*4,end='\n\n\n')

#Präsenzaufgabe 2

from decimal import Decimal, getcontext
getcontext().prec = 1001

#actual leibniz formular =4*sum^(inf)_k=0 ((-1)^k)((2*k+1))

variable = [10,20,30]

for i in variable:
    leibniz_approx =0
    for j in range(i):
        leibniz_approx = (leibniz_approx+Decimal((math.pow(-1,j)))/(Decimal(2*j+1)))
    leibniz_approx = leibniz_approx*4
    print('The PI approximation with n=', i, 'is:', leibniz_approx ,'\n\n\n\n')

#Präsenzaufgabe 3

number_full = int(math.pow(10,8))
number = int(math.pow(10,8)/2)

#mark_list
sieve = [True] * (number + 1)
sieve[0] = sieve[1] = False
for i in range(2, int(number ** 0.5) + 1):
    if sieve[i]:
        sieve[i*i : number+1 : i] = [False] * len(sieve[i*i : number+1 : i])

"""#save prime numbers to list
counter = 0
primes = [i for i, is_prime in enumerate(sieve) if is_prime]
for i in range(len(primes)):
    for j in range(len(primes)-i):
        if primes[i]*primes[i+j]<number_full:
            counter=counter+1

print('prime tuple count:', counter )
"""

print('runtime:',time.time()-start_time)