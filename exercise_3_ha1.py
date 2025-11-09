# Robert Jerye

from sympy import isprime

# CoMa week 3 ha 1 Primzahllücke

# exercise 1.1
def primesInRange(start= int, end=int):
    if end<start: 
        raise TypeError('start>end')
        return None
    
    prime_list =[]
    for i in range(start,end):
        if isprime(i): prime_list.append(i)

    return prime_list

# exercise 1.2
def primeGaps(primes=list):
    gap_list =[]
    for i in range(len(primes)-1):
        gap_list.append(primes[i+1]-primes[i])

    return gap_list

# exercise 1.3
def analyze_prime_gaps(start_value=int,end_value=int):
    prime_list = primesInRange(start=start_value, end=end_value)
    gap_list = primeGaps(prime_list)
    prime_dict ={'primes':prime_list,
                 'gaps':gap_list,
                 'maxGap':max(gap_list),
                 'avgGap':(sum(gap_list)/len(gap_list))}
    return prime_dict


# test  section
print(analyze_prime_gaps(start_value=1,end_value=50))

"""result = analyze_prime_gaps (start_value=10 ,end_value= 100)
print ( result ['primes' ][:10])

print ( result ['gaps' ][:10])

print ( result ['maxGap'])

print ( result ['avgGap'])"""

