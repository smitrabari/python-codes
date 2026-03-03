# Simple Calculator
choose = input("Choose the Following : \n"
      "1. {+} \n"
      "2. {-} \n"
      "3. {*} \n"
      "4. {/} \n"
               "")
a = float(input("Enter a number : ")) # User input
b = float(input("Enter another number : "))
# Choosing operator
if choose == "1":
    answer = a + b
    print(answer)
elif choose == "2":
    answer = a - b
    print(answer)
elif choose == "3":
    answer = a * b
    print(answer)
elif choose == "4":
    answer = a / b
    print(answer)
else :
    print("Sorry, I did not understand")