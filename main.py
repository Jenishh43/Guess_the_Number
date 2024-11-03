import random

MinNum = 0
MaxNum = 100
attempt = 10
PreviousGuesses = []
randomNumber = random.randint(MinNum, MaxNum)
# print(randomNumber)

while attempt != 0:
    try:
        EnteredNum = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter an integer.\n")
        continue

    PreviousGuesses.append(EnteredNum)
    attempt -= 1
    
    if(randomNumber < EnteredNum):
        print(f"Try to Guess Low , Remaining:- {attempt}, Your Previous Guess:- {PreviousGuesses}\n")
    elif(randomNumber > EnteredNum):
        print(f"Try to Guess High, Remaining:- {attempt}, Your Previous Guess:- {PreviousGuesses}\n")
    elif(randomNumber == EnteredNum):
        print(f"You Win, Remaining:- {attempt}, Your Previous Guess:- {PreviousGuesses}\n")
        break
else:        
    print(f"You Lost, Your Previous Guess:- {PreviousGuesses}\n")