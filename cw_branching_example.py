# Branching in class examples

# if statement has a condition that can be True or False
# > greater than, < less then
# >= greater than or equal to, <= less than or equal to
# == is equal to, != not equal to

# else statement never has a condition
'''
if 10 < 9:
    print("10 not less then 9")
if 87 != 87:
    print("Fales, 87 is 87!")

else:
    print("The statement is False")
    
'''


# Branching using a variable
'''
age = 2

if age > 0 and age <=5:
    print("You are a toddler!")
elif age > 5 and age <= 12:
    print("No longer a toddler, you are a child")
elif age > 12 and age <=17:
    print("You are a teenager")
elif age >= 18 and age <=64:
    print("You are an adult")
elif age >= 65:
    print("You are a senior")
else:
    print("You are a little baby or a time traveler")
'''

# If the string is not empty, it is True
student = "Jon Applebees"

if student:
    print("Student exists")

if True:
    print("Always True")

# Creation of variables inside if statement
myVar = False
if 10 == 80:
    myVar = True
else:
    myVar = False

print(f"The statment is: {myVar}")
