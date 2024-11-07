# Alta Schwab
# 11/5/2024
# P4HW1
# collect each score, use a loop, display score average(after dropping lowest score), display a letter grade for the calculated average

grades = []

numScores = int(input("How many scores do you want to enter? "))

for score in range(numScores):
    userInput = float(input (f"Enter score #{score + 1}: "))
    while userInput < 0 or userInput > 100:
        print()
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        userInput = float(input(f"Enter score #{score + 1} again: "))
    grades.append(userInput)

#Math stuff
lowScore = min(grades)

grades.remove(lowScore)

gradeAvg = sum(grades) / (numScores - 1)

#Findin out what letter grade
letter_grade = ""

if gradeAvg >= 90:
    letter_grade = "A"
elif gradeAvg >= 80:
    letter_grade = "B"
elif gradeAvg >= 70:
    letter_grade = "C"
elif gradeAvg >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

#Showing the result
print()
print("----------Result----------")
print(f"{'Lowest Score':<14} : {lowScore}")
print(f"{'Modified List':<14} : {grades}")
print(f"{'Scores Average':<14} : {gradeAvg}")
print(f"{'Grade':<13} : {letter_grade}")
print("-"*27)

