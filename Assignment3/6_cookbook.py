'''
Dish and Cookbook
This program shows how one class can store information created
by abother class
In this case class Cookbook stores information from Dish
'''

class Dish:
    def __init__(self, name):
        self.name = name


class Cookbook:
    def __init__(self):
        self.list = [] #empty so as to hold dish names

    def add(self, dish): #this will take a Dish object and add its 'name' to the list
        self.list.append(dish.name)

    def show(self): #this will print the final list of dishes
        print(self.list)


c = Cookbook() #creating cookbook
c.add(Dish(input("Dish: ")))
 #takes user input to create a dish and adds it to the cookbook
#the above method will create an object and c.add will store it
c.add(Dish(input("Dish: ")))

c.add(Dish(input("Dish: ")))

c.show()