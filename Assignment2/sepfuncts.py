'''Separate functions for arithmetic operations'''
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def floor_divide(a, b):
    if b != 0:
        return a // b
    else:
        return "Cannot divide by zero"

def power(a, b):
    return a ** b


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


print("\n--- Results ---")
print("Addition:", add(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))
print("Floor Division:", floor_divide(num1, num2))
print("Exponentiation:", power(num1, num2))