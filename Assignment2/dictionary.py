'''Returns the frequency of numbers in a list in the form of dictionary'''
def count_frequency(numbers):
    freq = {}  # empty dictionary

    for num in numbers:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    return freq


list1 = [1, 2, 2, 3, 3, 3]
print("List 1:", list1)
print("Frequency:", count_frequency(list1))
print()

list2 = [5, 5, 5, 1, 2, 2]
print("List 2:", list2)
print("Frequency:", count_frequency(list2))
print()

list3 = [10, 20, 10, 30, 20, 10]
print("List 3:", list3)
print("Frequency:", count_frequency(list3))

list4 = [25, 20, 20, 25, 20, 3]
print("List 4:", list3)
print("Frequency:", count_frequency(list4))