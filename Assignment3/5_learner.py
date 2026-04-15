'''
 Learner Class 
This program takes user input to create an object and then displays the student's details
There are 6 attributes in this Learner class
'''


class Learner:
    # 2. The __init__ method will initialize the attributes for each new student (setup)
    # 'self' allows the class to remember the specific data for each object
    def __init__(self, roll_no, full_name, address, enrollment_year, program, group):
        self.roll_no = roll_no
        self.full_name = full_name
        self.address = address
        self.enrollment_year = enrollment_year
        self.program = program
        self.group = group

    # this will print the data back to the user in a neat and organized manner
    def show_details(self):
        print("\n--- Learner Details ---")
        print("Roll No:       ", self.roll_no)
        print("Full Name:     ", self.full_name)
        print("Address:       ", self.address)
        print("Enrollment:    ", self.enrollment_year)
        print("Program:       ", self.program)
        print("Group:         ", self.group)
        print("-----------------------")

# organizing the required attributes for easier code understanding
r = input("Enter Roll No: ")
n = input("Enter Full Name: ")
a = input("Enter Address: ")
y = input("Enter Enrollment Year: ")
p = input("Enter Program: ")
g = input("Enter Group: ")

# object is created
# all the user's inputs is passed into the Learner class here
student1 = Learner(r, n, a, y, p, g)

# this method will display the information
student1.show_details()