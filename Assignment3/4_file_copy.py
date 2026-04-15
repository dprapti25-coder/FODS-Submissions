'''
Copy file contents
This program will read text from one file and write it into another
'''

try:
    #user input for the name of the file to read from
    # open it in read mode
    f1 = open(input("Input file: "), "r")
    
    # user input for the name of the file to create/write to
    # open in write mode
    f2 = open(input("Output file: "), "w")

    # read everything from the first file and immediately write it to the second
    # f1.read() gets the text; f2.write() puts it in the new file
    f2.write(f1.read())

    # close files to save the changes and free up memory
    f1.close()
    f2.close()

    print("Copied!")

# if input file doesn't exist or any other error happens, 
# the program jumps here instead of crashing.
except:
    print("Error occurred")