# Weight Converter
print("Welcome to the converter")
print("1. Kg to Pounds")
print("2. Pounds to Kg")
choice = input("Enter your choice: ")
# User Input
if choice == "1":
    kg=float(input("Enter the kg: "))
    pounds=kg * 2.20462
    print(pounds)
elif choice == "2":
    pounds = float(input("Enter the Pounds: "))
    kg = pounds * 0.453592
    print(kg)
else:
    print("Please enter your choice")