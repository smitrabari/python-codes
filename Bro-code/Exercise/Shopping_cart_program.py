# Shopping Cart Program

# input from user
item = input("Enter Name of the item : ")
price = float(input("Enter Price of that item : "))
Quantity = int(input("Enter no. of items you bought : "))

# billing program
bill = price * Quantity

print(f"You Bought {item}"
      f"Your Total Bill is ${bill}")