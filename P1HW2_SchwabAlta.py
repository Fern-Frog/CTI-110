# Alta Schwab
# 9/24/2024
# P1HW2
# Basic math on numbers that are entered by the user

print("This program calculates and displays travel expenses")

# Get the info from the user
first_budget = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas_price = int(input("How much do you think you will spend on gas? "))
accommodation_price = int(input("Approximately, how much will you need for accomodation/hotel? "))
food_price = int(input("Last, how much do you need for food? "))

print()
# Calculation

total_cost = gas_price + accommodation_price + food_price

remaining_budget = first_budget - total_cost

# The calculation resuals

print("----------Travel Expenses----------")
print(f"Location: {destination}")
print(f"Initial Budget: {first_budget} \n")
print(f"Fuel: {gas_price}")
print(f"Accommodation: {accommodation_price}")
print(f"Food: {food_price} \n")
print(f"Remaining Balance: {remaining_budget}")
