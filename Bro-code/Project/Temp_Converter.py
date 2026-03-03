# Temperature Converter
print("Welcome to the converter")
print("1. K -> °C")
print("2. °C -> K")
choice = input("Enter your choice: ")
# User Input
if choice == "1":
    k = float(input("Enter K: "))
    c = k -272.15
    print(f"{c} °C")
elif choice == "2":
    c = float(input("Enter °C: "))
    k = c + 273.15
    print(f"{k} K")
else:
    print("Please enter your choice")