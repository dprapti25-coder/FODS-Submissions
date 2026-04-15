'''Check if number user inputs is Armstrong number'''
def is_armstrong(num):
    power = len(str(num))
    total = sum(int(d)**power for d in str(num))
    return total == num

num = int(input("Enter number: "))
print("Armstrong" if is_armstrong(num) else "Not Armstrong")