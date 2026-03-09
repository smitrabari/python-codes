# Quiz Game

question = ("Who won t20i WC 2026?",
            "Who is best batter of all time?",
            "Which team has most t20i WC tittle?")

options = (("A. NZ","B. AUS","C. IND"),
           ("A. Root","B. Virat","C. Dhoni"),
           ("A. AUS","B. SRI","C. IND"))

answer = ("C","B","C")
choices = []
score = 0
question_num = 0

for question in question:
    print("------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    choice = input("Guess the option: ").upper()
    choices.append(choice)
    if choice == answer[question_num]:
        print("Correct!")
        score += 1
    else:
        print(f"The correct answer was {answer[question_num]}")
        print("Wrong!")
    question_num += 1


print("Your Total Score is = ", score)