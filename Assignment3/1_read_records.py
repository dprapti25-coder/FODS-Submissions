'''
This program reads data from "records.csv" and displays
student details such as name, roll number, program, year, and group.
'''

import csv #used to read CSV easily

try: #used to handle errors(e.g file not found errors)
   with open("records.csv", "r") as file:

        reader = csv.reader(file) #creates an object and also converts each line of the file into a list of words

        print("Student Records:\n")

        for row in reader: #used to look at every row in the file
            if len(row) < 5: #if there is missing data/empty row this skips it
                continue

            print("Name:", row[0])
            print("Roll No:", row[1])
            print("Program:", row[2])
            print("Year:", row[3])
            print("Group:", row[4])
            print("---------------------")

except FileNotFoundError: #if file doesn't exist then the try block stops and this code will be excuted
    print("Error: records.csv file not found!")