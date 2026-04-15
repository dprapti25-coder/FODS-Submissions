'''Calculates factorial and validates user input'''
num = input("Enter a number: ")

if num.isdigit():
    num = int(num)
    fact = 1
    for i in range(1, num+1):
        fact *= i
    print("Factorial:", fact)
else:
    print("Invalid input!")