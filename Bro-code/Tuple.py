# Tuple - these are Faster than list

names = ("dhoni","virat","rohit","rahul","hardik","pant","siraj")
print(names) # prints all list values
print(names[1]) # printing virat as a index value
print(f"Top oder batters{names[0:3]}") # printing first three values.
print(names[::2]) # printing every second element.
print(dir(names)) # shows all the attributes
print(help(names)) # shows the documentation of an object
print(len(names)) # length of list
print(len(names[1])) # length of element
# to see whether the element is present in list or not
print("virat" in names) # will print true
print("pujara" in names) # will print false
# Index method
print(names.index("siraj"))
# Count method
print(names.count("virat"))