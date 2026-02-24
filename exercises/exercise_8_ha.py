# Robert Jerye


class residue_class:

    def __init__(self, z: int, n: int):
        self.z = z
        self.n = n

    def __add__(self, additor: int):
        return residue_class((self.z + additor) % self.n, self.n)

    def __sub__(self, subtractor: int):
        return residue_class((self.z - subtractor) % self.n, self.n)

    def __mul__(self, scalar: int):
        return residue_class((self.z * scalar) % self.n, self.n)


class residue_class_prime(residue_class):

    import sympy

    def __truediv__(self, n: int):
        if sympy.isprime(n) != 1:
            raise ValueError(
                "__truediv__ is only avalailable when 'n' is a prime number"
            )
        else:
            return residue_class(self.z % n, self.n)
