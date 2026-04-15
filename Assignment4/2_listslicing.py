'''
List sorting and slicing
Takes 12 numbers, sorts them, and performs slicing
'''

numbers = input("Enter at least 12 numbers: ").split() #splits the string into a list of strings
numbers = [int(x) for x in numbers] #string elements are converted to integer for sorting

numbers.sort()

print("Sorted list:", numbers)

print("3-6:", numbers[3:7]) #slicing follows the [start::stop] format
print("6-9:", numbers[6:10])
print("4-10:", numbers[4:11])