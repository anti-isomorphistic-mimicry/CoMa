# Aufgabe 1
# Schreiben Sie eine Funktion rot(n),
# die eine numpy-Matrix R von Dimensionen (n,n)
# erstellt, welche einen n-Vektor um eins nach rechts
# "dreht":
#  (x_1, x_2, ..., x_(n-1), x_n) * R = (x_n, x_1, x_2, ..., x_(n-1))
#
# Testen Sie Ihre Funktion mit einem Vektor von Laenge mindestens
# fuenf, und lassen Sie sich mit ".getI()" die Inverse der erzeugten
# Matrix anzeigen. Was macht die mit einem Vektor der gleichen Laenge?

import numpy as np


def create_matrix(n: int):
    """
    helper function to create a NxN array matrix with ints
    """

    array_matrix = np.zeros((n, n))
    counter = 1

    for i in range(n):
        for j in range(n):
            array_matrix[i][j] = counter
            counter = counter + 1

    return array_matrix


def rot(matrix):

    m_roll = np.roll(matrix, shift=1, axis=1)

    return np.matrix(m_roll)


print("exercise 1")
r = rot(create_matrix(3))
print("column shifted matrix")
print(r)
print("-----")
print("shifted matrix inverted")
print(r.getI())
print("-----\n")

# Aufgabe 2
# Schreiben Sie eine Funktion reverse(n), welche eine n-mal-n
# numpy-Matrix E erzeugt, welcher die Eintraege eines n-Vektors
# umkehrt:
# (x_1, x_2, ..., x_(n-1), x_n) * E = (x_n, x_(n-1), ... , x_2, x_1)
#
# Ueberlegen Sie kurz, wie die Inverse der Matrix aussehen muss, und
# lassen Sie ".getI()"
# Kombinieren Sie eine solche Matrix E mit einer Matrix R aus Aufgabe 1
# auf verschiedene Arten und lassen Sie die Produkte
# E * R
# R * E
# E * R * E
# R * E * R.getI()
# auf den
# Vektor (1,2,...,n) wirken. Was kommt da raus und warum?


def reverse(matrix):

    m_flip = np.flip(matrix, axis=0)

    return np.matrix(m_flip)


print("exercise 2")
e = reverse(create_matrix(3))
print("row shifted matrix")
print(e)
print("-----")
print("row shifted matrix inverted")
print(e.getI())
print("r*e")
print(r * e)
print("e*r")
print(e * r)
print("e*r*e")
print(e * r * e)
print("r*e*r.getI()")
print(r * e * r.getI())
print("-----\n")

# Aufgabe 3
# Schreiben Sie eine Funktion spur(M), welche eine
# n mal n numpy-Matrix M entgegenimmt. Die Funktion
# wandelt die Matrix mit ".reshape(n*n)" in eine
# einzeilige Matrix um. Lassen Sie numpy eine
# einzeilige Matrix S so bauen, dass
# M * S.T die Spur der Matrix M liefert (das ist die
# Summe der Diagonal-Elemente. Sie koennen mit
# "M.trace()" testen, ob Sie richtig lagen.)


def spur(matrix):
    trace = []
    borders = matrix.shape[0]
    shift = 0

    for i in range(borders):
        sum = 0
        col = 0 + shift
        row = 0
        for j in range(borders):
            sum = sum + matrix[row, col % borders]
            col = col + 1
            row = row + 1
        trace.append(sum)
        shift = shift + 1
    return trace


# test environment
print("exercise 3")

test_oject = create_matrix(3)
print("traces of a 3x3 matrix")
print(spur(test_oject))

print("compare spur() method with the numpy buildIn trace")
for i in range(3):
    print(np.trace(np.roll(test_oject, shift=i, axis=1)))
