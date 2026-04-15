''' Takes student details as input and appends them to records.csv'''

import csv #handles CSV files

student_name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
program = input("Enter program: ")
year = input("Enter year: ")
group = input("Enter group: ")

with open("records.csv", "a", newline="") as file: #file opened in append mode #'newline' prevents any addition of extra unneccessary rows
    writer = csv.writer(file) #this method will automatically put in the commas so you don't have to e.g name, roll, etc
    writer.writerow([student_name, roll_no, program, year, group])

print("Record added successfully!")