# Alta Schwab
# 10/17/2024
# P3HW1
# Have the user to enter grades, store the grades entered in a list, and display stuff



# Get input from user

M1_Grade = float(input("Enter grade of Module 1: "))
M2_Grade = float(input("Enter grade of Module 2: "))
M3_Grade = float(input("Enter grade of Module 3: "))
M4_Grade = float(input("Enter grade of Module 4: "))
M5_Grade = float(input("Enter grade of Module 5: "))
M6_Grade = float(input("Enter grade of Module 6: "))

print()

# Create list with variables
grades_list = [M1_Grade, M2_Grade, M3_Grade, M4_Grade, M5_Grade, M6_Grade]


# Make variables
low_grade = min(grades_list)
high_grade = max(grades_list)
sum_grade = sum(grades_list)
num_grade = len(grades_list)
avg_grade = sum_grade / num_grade

# Display results

print("------------Results------------")
print(f"{'Lowest Grade:':<20} {low_grade:.2f}")
print(f"{'Highest Grade:':<20} {high_grade:.2f}")
print(f"{'Sun of Grade:':<20} {sum_grade:.2f}")
print(f"{'Average:':<20} {avg_grade:.2f}")
print("--" *20)

# Branching to determine the letter grade
letter_grade = ""

if avg_grade >= 90:
    letter_grade = "A"
elif avg_grade >= 80:
    letter_grade = "B"
elif avg_grade >= 70:
    letter_grade = "C"
elif avg_grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print()
print(f"Your grade is: {letter_grade}")
