# Robert Jerye studonid: uz67izax

from sympy import isprime


#algo is pretty bad and ineffiecient for larger numbers but I ran out of time 

print('Gib eine positive ganze Zahl ein: ', end='')
variable =int(input())
var_org = variable
prime_candidates=[]

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
        if prime_list[i][1] !=1:
            print(prime_list[i][0],prime_list[i][1],sep='^')
    else:
        if prime_list[i][1] ==1:
            print(prime_list[i][0],end=' * ')
        else:
            if prime_list[i][1] != 1 & prime_list[i][0] !=prime_list[len(prime_list)-1][0]:
                print(prime_list[i][0],prime_list[i][1],sep='^',end=' * ')
