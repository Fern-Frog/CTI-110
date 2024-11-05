# Alta Schwab
# 11/5/2024
# P4HW1
# collect each score, use a loop, display score average(after dropping lowest score), display a letter grade for the calculated average

numScores = int(input("How many scores do you want to enter? "))

for score in range(numScores):
    userInput = float(input (f"Enter score #{score + 1}: "))
    while userInput < 0 or userInput > 100:
        print()
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        userInput = float(input(f"Enter score #{score + 1} again: "))
    
