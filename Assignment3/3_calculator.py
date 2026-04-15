'''Performs arithmetic operations on user input numbers,
stores results with timestamp in a file, and displays history on exit'''

from datetime import datetime #this gets the current date & time

file_name = "results.txt"

while True: #keeps the program running in a lopp
    numbers = input("Enter numbers separated by space: ")
    num_list = list(map(float, numbers.split()))
#this gets numbers as strings, splites them and makes them to float type

    print("\n1.Add 2.Subtract 3.Multiply 4.Divide")
    choice = input("Choose operation: ")

    if choice == "1":
        result = sum(num_list)

    elif choice == "2":
        result = num_list[0]
        for n in num_list[1:]:
            result -= n

    elif choice == "3":
        result = 1
        for n in num_list:
            result *= n

    elif choice == "4":
        try:
            result = num_list[0]
            for n in num_list[1:]:
                result /= n

        except ZeroDivisionError:
            print("Cannot divide by zero!")
            continue
    else:
        print("Invalid choice")
        continue

    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #this creates a timestamp

    with open(file_name, "a") as f:
        f.write(f"{time_now} | {num_list} | Result: {result}\n")

    cont = input("Continue? (yes/no): ").lower()
    if cont == "no":
        break

print("\n--- FILE CONTENTS ---\n")

with open(file_name, "r") as f:
    print(f.read())