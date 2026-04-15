'''
NumPy array operations
Creates a NumPy array and finds sum, mean, max, and min values
'''

import numpy as np

arr = np.array([10, 20, 30, 40, 50]) #1D array created

print("Array:", arr)

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))