"""# imports
from time import time

# program timer
start_timer = time()


def F(number: int, modulo: int):
    if number == 1:
        return 1
    elif number == 2:
        return 2
    else:
        a = 1
        b = 2
        for i in range(3, number + 1):
            a = b
            b = (a + b) % modulo
        return b


folge_glieder = []
for i in range(41):
    folge_glieder.append(F(i, 37))

print("first 40 elements of the sequence:\n", folge_glieder)
print("average of the first 40 elements:\n", sum(folge_glieder) / len(folge_glieder))

print("runtime:\n", time() - start_timer, "sec")"""


def F(n, m):
    if n == 1:
        return 1 % m
    elif n == 2:
        return 2 % m
    # iterative Berechnung, damit es effizient bleibt
    f1 = 1 % m  # F(1,m)
    f2 = 2 % m  # F(2,m)
    for _ in range(3, n + 1):
        f1, f2 = f2, (f1 + f2) % m
    return f2


m = 37
werte = [F(n, m) for n in range(1, 41)]
durchschnitt = sum(werte) / len(werte)

print("Erste 40 Werte für m = 37:")
print(werte)
print("Durchschnitt:", durchschnitt)
