# while loop
name = input("Enter your name: ")
while name == "": # While loop started
    print("Please enter a valid name")
    name = input("Enter your name: ")
print(f"Welcome {name}")

age = int(input("Enter your age: "))
while age < 0: # While loop started
    print("Please enter a valid age")
    age = input("Enter your age: ")
print(f"Your age is {age} years old")

food = input("Enter your Fav. food(q/Q to quit): ")
while not food == "q": # While loop started
    print(f"you like {food}")
    food = input("Enter another your Fav. food(q/Q to quit): ")
print("Bye")