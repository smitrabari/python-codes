# input from the User!!
name = input("what is your name : ")
age = input("what is your age : ")
# short-cut
gpa = float(input("what is your GPA : "))
# typecasting because input store value in string
age = int(age)
# printing the values
print(f"Hello {name}")
print(f"You are {age} years old")
print(f"Your GPA is {gpa}")