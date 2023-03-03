names = ["John", "Mary", "Zoe","Alex","Séamas"]
# creating a list of names

name = input("Enter lookup name: ")
# seeking user input

found = False # initiate the boolean data type to false
index = 0 # initiate the counter

# create a while loop that the program will execute until searched item is found or list has been checked throughout 

while (not found) and (index != len(names)): # second part here will allow len of list to be amended 
    if name == names[index]: 
        found = True # when found change boolean data type to true, break loop take us to line 18
    else:
        index = index + 1 # otherwise, search next list item
        
print("Result:", index) # tell me where item is 