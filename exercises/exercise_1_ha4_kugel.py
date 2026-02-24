# Robert Jerye studonid: uz67izax

import math

"""
"math" out U_K

Bogensegment: l=r*alpha
sin(alpha)=r_K/r => r_K=r*sin(alpha)
U_K = abs(2*PI*r_K) => U_K = abs(2*PI*r*sin(l/r))
"""
# user input, calulations and output
print("Radius r der Kugel[cm]: ", end="")
r = float(input())
print("Länge l der Schnur[cm]: ", end="")
l = float(input())
print("Der Kreisumfang beträgt ", end="")
print(abs(2 * math.pi * r * math.sin(l / r)), "cm", sep="")

