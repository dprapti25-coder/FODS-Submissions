'''Sorting a list of names in reverse alphabetical order'''
def sort_reverse(names):
    return sorted(names, reverse=True)

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    students.append(name)

sorted_names = sort_reverse(students)

print("\nNames in reverse alphabetical order:")
for name in sorted_names:
    print(name)