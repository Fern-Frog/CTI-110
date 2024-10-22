# Alta Schwab
# 10/17/2024
# P3LAB
# Calculate coin combibnations for given value

'''
# Regular Divison
print(100/3)

# Floor Division - returns the whole number
print(100//3)

# Modulus Division - return the remainder only as an integer
print(100%3)
print(7%4)
'''

# Get money value from the user
money = float(input("Enter the amount of money as a float: $"))

# Convert money to a whole number
money = int(round(money * 100))

'''
print(money)
'''

# Calcutlate the amount of dollar in the money variable
dollars = money // 100
'''
print(f"Dollars: {dollars}")
'''

# Remove the dollars from the money variable
money = money - (dollars * 100)

# Calcutlate the amount of quarters in the money variable
quarters = money // 25
'''
print(f"Quarters: {quarters}")
'''

# Remove the quarters from the money variable
money = money - (quarters * 25)

# Calcutlate the amount of dimes in the money variable
dimes = money // 10
'''
print(f"Dimes: {dimes}")
'''

# Remove the dimes from the money variable
money = money - (dimes * 10)

# Calcutlate the amount of nickel in the money variable
nickels = money // 5
'''
print(f"Nickels: {nickels}")
'''

# Remove the nickels from the money variable
money = money - (nickels * 5)

# Create a variable for pennies
pennies = money
'''
print(f"Pennies: {pennies}")
'''

# Print dollar amount gramatically correct
if dollars > 0:
    if dollars == 1:
        print(f"{dollars} Dollar")
    else:# variable is greater than one
        print(f"{dollars} Dollars")

# Print quarter amount gramatically correct
if quarters > 0:
    if quarters == 1:
        print(f"{quarters} Quarter")
    else:# variable is greater than one
        print(f"{quarters} Quarters")

# Print dime amount gramatically correct
if dimes > 0:
    if dimes == 1:
        print(f"{dimes} Dime")
    else:# variable is greater than one
        print(f"{dimes} Dimes")

# Print nickel amount gramatically correct
if nickels > 0:
    if nickels == 1:
        print(f"{nickels} Nickel")
    else:# variable is greater than one
        print(f"{nickels} Nickels")

# Print pennie amount gramatically correct
if pennies > 0:
    if pennies == 1:
        print(f"{pennies} Penny")
    else:# variable is greater than one
        print(f"{pennies} Pennies")
