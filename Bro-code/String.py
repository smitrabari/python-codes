# String Functions
name = input("Enter your name: ")
# Input of string
result = len(name) # Length of the name variable.
print(result)
result = name.find(" ") # These will find space from the input string.
print(result)
result = name.capitalize() # To make upper case of first letter.
print(result)
result = name.upper() # To make Upper-case of all letters.
print(result)
result = name.lower() # To make Lower-case of all letters.
print(result)
result = name.isdigit() #only digit Will give True, else false.
print(result)
result = name.isalpha() #have any space in string then it will print true, else false.
print(result)
result = name.count("i") # this will find "i" in given string.
print(result)
result = name.replace("i","ii") # This will replace i to ii
print(result)

print(help(str)) # To get all info of String methods