import numpy as np


class Polynomial:

    def __init__(self, coef: list):
        self.coef = coef

    def calc(self, x):
        result = 0
        for i in range(len(self.coef)):
            result += self.coef[i] * (x**i)
        return result

    def multiply(self: list, q: list):

        # Create a list to hold all the coefficients and initialize them with zeroes
        coeff = np.zeros(len(self.coef) + len(q) - 1)

        # the combination of indices of the original lists determine the exponent of the polynomial
        for i in range(len(self.coef)):
            for j in range(len(q)):
                coeff[i + j] = coeff[i + j] + (self.coef[i] * q[j])

        return Polynomial(coeff)

    def divide(self: list, poly: list):

        result = []
        remainder = self.coef.copy()

        # calulating the degree of each polynomial
        degree_p = len(self.coef) - 1
        degree_q = len(self.coef) - 1

        # determine the amount of steps
        steps = degree_p - degree_q

        for _ in range(steps + 1):
            if len(remainder) < len(poly):
                break

            # divide the two polynomials
            factor = remainder[0] / poly[0]
            result.append(factor)

            # subtract the devised polynomial from the remainder
            for i in range(len(poly)):
                remainder[i] -= factor * poly[i]

            # remove all leading zeroes
            while len(remainder) > 0 and remainder[0] == 0:
                remainder.pop(0)

        return Polynomial(result)

    def add(self, poly: list):

        iter_range = max(len(self.coef), len(poly))
        sum = [0] * iter_range

        for i in range(len(self.coef)):
            sum[i] += self.coef[i]

        for i in range(len(poly)):
            sum[i] += poly[i]

        return Polynomial(sum)

    def subtract(self, poly: list):
        iter_range = max(len(self.coef), len(poly))
        subt = [0] * iter_range

        for i in range(len(self.coef)):
            subt[i] += self.coef[i]

        for i in range(len(poly)):
            subt[i] -= poly[i]

        return Polynomial(subt)

    def __add__(self, poly: list):
        return self.add(poly)

    def __sub__(self, poly: list):
        return self.subtract(poly)

    def __mul__(self, poly: list):
        return self.multiply(poly)

    def degree(self):
        return len(self.coef) - 1

    def __str__(self):
        terms = []
        for i in range(len(self.coef)):
            if self.coef[i] == 0:
                continue
            if i == 0:
                terms.append(f"{self.coef[i]}")
            elif i == 1:
                if self.coef[i] == 1:
                    terms.append("x")
                elif self.coef[i] == -1:
                    terms.append("-x")
                else:
                    terms.append(f"{self.coef[i]}x")
            else:
                if self.coef[i] == 1:
                    terms.append(f"x**{i}")
                elif self.coef[i] == -1:
                    terms.append(f"-x**{i}")
                else:
                    terms.append(f"{self.coef[i]}x**{i}")
        return " + ".join(terms).replace("+ -", "- ")

    def __eq__(self, poly: list):
        return self.coef == poly

    def __neq__(self, poly: list):
        return not self.coef == poly


# Test cases using lists for poly
print("--- Test: Initialisierung und calc ---")
p1 = Polynomial([1, 2, 1])  # 1 + 2x + x²
print(f"p1(2) = {p1.calc(2)}")  # Expected: 9

print("\n--- Test: degree ---")
p2 = Polynomial([0, 0, 3, 4])  # 3x² + 4x³
print(f"Grad von p2: {p2.degree()}")  # Expected: 3

print("\n--- Test: add und __add__ ---")
p3 = Polynomial([1, 2])  # 1 + 2x
p4_coef = [0, 1, 3]  # x + 3x²
result_add = p3.add(p4_coef)
print(f"p3 + p4 = {result_add}")  # Expected: 1 + 3x + 3x²

print("\n--- Test: subtract und __sub__ ---")
p5 = Polynomial([5, 2])  # 5 + 2x
p6_coef = [1, 1]  # 1 + x
result_sub = p5.subtract(p6_coef)
print(f"p5 - p6 = {result_sub}")  # Expected: 4 + x

print("\n--- Test: multiply und __mul__ ---")
p7 = Polynomial([1, 2])  # 1 + 2x
p8_coef = [3, 4]  # 3 + 4x
result_mul = p7 * p8_coef
print(f"p7 * p8 = {result_mul}")  # Expected: 3 + 10x + 8x²

print("\n--- Test: divide ---")
p9 = Polynomial([1, -3, 2])  # 1 - 3x + 2x²
p10_coef = [1, -1]  # 1 - x
result_div = p9.divide(p10_coef)
print(f"p9 / p10 = {result_div}")  # Expected: 2 - x

print("\n--- Test: __eq__ und __neq__ ---")
p11 = Polynomial([1, 2, 3])  # 1 + 2x + 3x²
p12_coef = [1, 2, 3]  # 1 + 2x + 3x²
p13_coef = [1, 2, 4]  # 1 + 2x + 4x²
print(f"p11 == p12_coef: {p11 == p12_coef}")  # Expected: True
print(f"p11 == p13_coef: {p11 == p13_coef}")  # Expected: False
print(f"p11 != p13_coef: {p11 != p13_coef}")  # Expected: True

print("\n--- Test: __str__ ---")
p14 = Polynomial([0.5, 0, 1, 2, -1])  # 0.5 + x² + 2x³ - x⁴
print(f"p14: {p14}")  # Expected: 0.5 + x**2 + 2x**3 - x**4
