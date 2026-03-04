# Compound Interest Calculator

principle = 0
rate = 0
time = 0

while principle <=0:
    principle = float(input("Enter Principle: "))
    if principle <=0:
        print("Principle Error")

while rate <=0:
    rate = float(input("Enter Rate: "))
    if rate <=0:
        print("Rate Error")

while time <=0:
    time = int(input("Enter Time: "))
    if time <=0:
        print("Time Error")

total = principle*(1+rate/100)**time
print(f"Total: ${total:.2f}")