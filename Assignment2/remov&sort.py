'''Accepts list, removes duplicates, and sorts ascending.'''
def remove_duplicates_sort(numbers):
    unique_numbers = list(set(numbers))

    # Sort the list in ascending order
    unique_numbers.sort()

    return unique_numbers


numbers = []

n = int(input("Enter how many numbers: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

result = remove_duplicates_sort(numbers)

print("\nList after removing duplicates and sorting:")
print(result)