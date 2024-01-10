""" 
Part 2: List of classes

Write a program that asks for the names of all the classes you are taking this semester
Save these class names in a list.
Print all the items in the list, one per line"""

classList = []  # empty list

# print("Enter the names of all the classes you are taking this semester: ")

while True:
    newClass = input("Enter class name: \n")
    if newClass == "":  # this so the person can do enter after finishing writing all there classes
        break
    classList.append(newClass)  # this adding the names of the class in the list

print("List of the names you taking this semester: ")
for name in classList:  # this will write each name in the list
    print(name)
