# shoping cart program

foods = []
price = []
total = 0

while True:
    food = input("What you would like to order(q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input("What is the price of your food: "))
        foods.append(food)
        total += price

price = str(price)
print()
print("---Visit again---")
print("You ordered list -")
for i in range(len(foods)):
    print(foods[i],end=" ")
    for j in range(len(price)):
        print(f" - {price[j]}",end=" ")
    print()
print(f"Your Bill is ${total}")