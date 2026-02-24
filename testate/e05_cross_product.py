#imports
from time import time

#start runtimer
stimer = time()

def cross(vector_1: list, vector_2: list):

    if (not len(vector_1) == 3) and (not len(vector_2) == 3):
        raise Exception("only 3d-vectors supported")

    resulting_vector = [0, 0, 0]
    resulting_vector[0] = vector_1[1] * vector_2[2] - vector_1[2] * vector_2[1]
    resulting_vector[1] = vector_1[2] * vector_2[0] - vector_1[0] * vector_2[2]
    resulting_vector[2] = vector_1[0] * vector_2[1] - vector_1[1] * vector_2[0]

    return resulting_vector

def add(vector_1: list, vector_2: list):

    if (not len(vector_1) == 3) and (not len(vector_2) == 3):
        raise Exception("only 3d-vectors supported")

    resulting_vector = [0, 0, 0]
    resulting_vector[0] = vector_1[0] + vector_2[0]
    resulting_vector[1] = vector_1[1] + vector_2[1]
    resulting_vector[2] = vector_1[2] + vector_2[2]

    return resulting_vector


# Jacobi-identity

a = [1, 0, 0]
b = [0, 1, 1]
c = [1, 1, 1]

cp_bc = cross(b, c)
cp_ca = cross(c, a)
cp_ab = cross(a, b)

s_0 = cross(a, cp_bc)
s_1 = cross(b, cp_ca)
s_2 = cross(c, cp_ab)

jacobi_identity = add(s_0, add(s_1, s_2))

#test section
print("jacobi_identity == [0,0,0]:\n", jacobi_identity == [0,0,0])
print("runtime:\n", time()-stimer, "sec")