'''
Matrix operations using NumPy
Takes two matrices and performs +, -, * operations
'''

import numpy as np

r = int(input("Rows: "))
c = int(input("Columns: "))

print("Matrix 1:")
m1 = np.array([[int(input()) for j in range(c)] for i in range(r)])
#Matrix 1 is created using for loops
#inner loop handles columns and the outer handles rows

print("Matrix 2:")
m2 = np.array([[int(input()) for j in range(c)] for i in range(r)])

#in numpy '*' does not function as a dot product instead it performs element-wise multiplication
print("Addition:\n", m1 + m2)
print("Subtraction:\n", m1 - m2)
print("Multiplication:\n", m1 * m2)