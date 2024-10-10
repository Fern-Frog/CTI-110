# Alta Schwab
# 10/10/2024
# P2HW2
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
