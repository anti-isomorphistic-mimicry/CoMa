s = input("Gib eine positive ganze Zahl ein: ")
n = int(s)

print("Die Primfaktorzerlegung von", n, "ist:")

teiler = 2
pfz = ""  # Hier speichere ich die PFZ während der while-Schleife

while n > 1:
    k = 0
    while n % teiler == 0:
        k = k + 1
        n = n // teiler
    if k > 0:
        if pfz != "":
            pfz = pfz + " * "
        if k == 1:
            pfz = pfz + str(teiler)
        else:
            pfz = pfz + str(teiler) + "^" + str(k)
    teiler = teiler + 1

print(pfz)
