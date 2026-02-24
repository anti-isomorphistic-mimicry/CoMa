# Implementieren Sie Ihr eigenes
# linspace(a,b,n)
# was ein Generator sein soll, der n Zahlen
# von a bis b (einschliesslich!) in gleichmaessigen
# Abstaenden liefert.
# Testcase
# list(linspace(1,2,3)) == [1, 1.5, 2]

import time

start_timer = time.time()


def homebrew_linspace(start: float, end: float, steps: int):
    value = start
    increase = (end - start) / (steps - 1)
    for i in range(steps):
        yield value
        value = value + increase


# test cases
print("homebrew_linspace(1,2,3)", list(homebrew_linspace(1, 2, 3)))
print("homebrew_linspace(2,1,3)", list(homebrew_linspace(2, 1, 3)))

print("runtime task 1:", time.time() - start_timer)
start_timer = time.time()


# Loesen Sie
# https://projecteuler.net/problem=2
# mit Generatoren.
# Schreiben Sie dazu einen Fibonacci-Generator fib() und
# einen Generator
#   take(stream, k)
# welcher die ersten k Erzeugnisse des Generators  stream
# einzeln mit yield liefert.
# Benutzen Sie die Funktionen
#  filter
# und
#  sum
# auf ihren Generatoren.


def fib():
    """Generates an infinite sequence of Fibonacci numbers starting 1, 2, ..."""
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b


def take_until_limit(stream, limit):
    """Yields values from the stream as long as they do not exceed the limit."""
    for value in stream:
        if value > limit:
            break
        yield value


fib_stream = fib()

limited_stream = take_until_limit(fib_stream, 4000000)


result = sum(filter(lambda x: x % 2 == 0, limited_stream))

print(f"The sum of even-valued Fibonacci terms below 4,000,000 is: {result}")

print("runtime task 2:", time.time() - start_timer)
start_timer = time.time()

# for control
fib_numbers = [
    0,
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    21,
    34,
    55,
    89,
    144,
    233,
    377,
    610,
    987,
    1597,
    2584,
    4181,
    6765,
    10946,
    17711,
    28657,
    46368,
    75025,
    121393,
    196418,
    317811,
    514229,
    832040,
    1346269,
    2178309,
    3524578,
]

sum = 0
for i in fib_numbers:
    if i % 2 == 0:
        sum = sum + i

print("compare: Is homebrew fib the same as the correct solution?", sum == result)

print("runtime test:", time.time() - start_timer)
