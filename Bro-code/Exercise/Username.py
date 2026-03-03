# Username Detector
username = input("Enter your username: ")
if len(username) > 12: # Username should not carry more than 12
    print("Your username is too Long!!")
elif not username.find(" ") == -1: # Username should not carry Spaces
    print("Your username Should not contain Space!!")
elif not username.isalpha(): # Username should not carry Numbers
    print("Your username should be a number")
else:
    print("Your username is valid")