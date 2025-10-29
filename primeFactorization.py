from sympy import isprime
from collections import defaultdict

print('Gib eine positive ganze Zahl ein: ', end='')
variable =7175591945 #int(input())
rest = variable
"""prime_candidates=[]

for i in range(2,variable+1):
    if isprime(i) == True: 
        prime_candidates.append(i)


prime_list = []
for i in prime_candidates:
    if variable%i==0: prime_list.append([i,0])


for i in range(len(prime_list)):
    while (variable%prime_list[i][0]==0):
        prime_list[i][1]=prime_list[i][1]+1
        variable=variable/prime_list[i][0]

print('Die Primfaktorzerlegung von ', var_org, ' ist:')
for i in range(len(prime_list)):
    if prime_list[i][0]==prime_list[len(prime_list)-1][0]:
        print(prime_list[i][0])
    else:
        if prime_list[i][1] ==1:
            print(prime_list[i][0],end=' * ')
        else:
            print(prime_list[i][0],prime_list[i][1],sep='^',end=' * ')"""

#prime numbers till 100
small_fish = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
    31, 37, 41, 43, 47, 53, 59, 61, 67,
    71, 73, 79, 83, 89, 97
]

#dict prime factors till 100
white_donkey = {}
for i in small_fish:
    white_donkey[i]=0
    while (rest%i==0):
        white_donkey[i] = white_donkey[i]+1
        rest=rest/i
counter =0
for i in range(int(rest),100,-1):
    if isprime(int(rest))==True:
        counter = counter+1
        while (rest%i==0):
            print(i)
            #white_donkey[i]=white_donkey[i]+1
            rest=rest/i

print(white_donkey)
print(counter)