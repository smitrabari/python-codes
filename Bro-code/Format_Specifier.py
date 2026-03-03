# Format Specifier
import math
price = 23.3455
price1 = 5274819927
num = 99.99
pi = math.pi
num1 = -99.909
print(f"The price is ${price:.1f}") # Digit after decimal
print(f"The pi is ${pi:10.3f}") # Spacing
print(f"The pi is ${pi:010.3f}") # Zero before digit
# Alignment flags
print(f"{num:<10}") # Left
print(f"{num:>10}") # Right
print(f"{num:^10}") # Center
# Sign of number
print(f"{num:+}")
print(f"{num1:+}")
# Spacing Sign
print(f"{num: }")
print(f"{num1: }")
# Comma after evry 1000
print(f"{price1:,}")