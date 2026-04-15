'''
NumPy reshape
Creates random array, sorts it, and reshapes into matrix
'''

import numpy as np

arr = np.random.randint(1, 100, 12)
#this generates an array with 12 random integers between 1-100

print("Original:", arr)

arr.sort()

print("Sorted:", arr)

matrix = arr.reshape(3, 4)

print("Reshaped (3x4):")
print(matrix)