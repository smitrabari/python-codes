# Set

names = {"dhoni","virat","rohit","rahul","hardik","pant","siraj"}
print(names) # prints all list values
# print(names[1]) # Set is unordered.
# print(f"Top oder batters{names[0:3]}") # Hence, its unordered ide cannot pic the correct one
# print(names[::2]) # Similarly
print(dir(names)) # shows all the attributes
print(help(names)) # shows the documentation of an object
print(len(names)) # length of list
# print(len(names[1])) # unordered set
# adding a value to list
# Hence we can add or remove elements.
# no Append method, just add method
names.add("virat")
print(names)
# Remove method
names.remove("virat")
print(names)
