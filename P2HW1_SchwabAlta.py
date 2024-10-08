# Alta Schwab
# 9/24/2024
# P1HW2
# Basic math on numbers that are entered by the user

print("This program calculates and displays travel expenses")

# Get the info from the user
first_budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas_price = float(input("How much do you think you will spend on gas? "))
accommodation_price = float(input("Approximately, how much will you need for accomodation/hotel? "))
food_price = float(input("Last, how much do you need for food? "))

print()
# Calculation

total_cost = gas_price + accommodation_price + food_price

remaining_budget = first_budget - total_cost

# The calculation resuals display

print("----------Travel Expenses----------")
print(f"{'Location:':<18} {destination:<}")
print(f"{'Initial Budget:':<18} ${first_budget:<,.2f} \n")
print(f"{'Fuel:':<18} ${gas_price:<,.2f}")
print(f"{'Accommodation:':<18} ${accommodation_price:<,.2f}")
print(f"{'Food:':<18} ${food_price:<,.2f} \n")
print(f"{'Remaining Balance:':<18} ${remaining_budget:<,.2f}")
