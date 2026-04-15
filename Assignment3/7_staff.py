'''
 Staff Management System
This program asks user input for a specific number of staff members,
collects their details, and saves them into a CSV file.
'''

file = open("staff.csv", "w") #opens or creates the file staff.csv in wirte mode

n = int(input("How many staff? "))

for i in range(n): #use a for loop to ensure loop repeats n number of times
    emp = input("ID: ")
    name = input("Name: ")
    salary = input("Salary: ")

    file.write(emp + "," + name + "," + salary + "\n")

file.close() #close the file to save all the data properly

print("Saved")

file = open("staff.csv", "r") #reopen file in read mode to check results
print(file.read())
file.close()