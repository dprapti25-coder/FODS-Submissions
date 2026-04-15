'''
Library Management System
This program checks if a book exists in the library
It allows the user to search for a specific title.
'''

books = ["The Secret History", "If We Were Villians", "Alone With You In the Ether", "Crush", "On Earth We're Briefly Gorgeous"] #database of books in a list

print("Books:", books) #this displays the collection to the user

search = input("Search book: ")

if search in books: #the in keyword checks if the book user inputs is within our list/library
    print("Book found")
else:
    print("Not found")