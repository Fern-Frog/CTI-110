# Alta Schwab
# 10/3/2024
# P2LAB2
# Uses a dictionary to store user input and displays output to the user

# Create the dictionary
car_MPG = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}

# Variable that holds all the keys
keys = car_MPG.keys()

# Show all keys to user
print(keys)
print()

# Prompt the user to give one of the keys

chosen_key = input("Enter a vehicle to see it's mpg: ")

# Get the value from the key and save it in a variable
corresponding_value = (car_MPG[chosen_key])
print()

# Display requested value 
print(f"The {chosen_key} gets {corresponding_value} mpg.")
print()

# Prompt the user to enter the number of miles that they will drive the vehicle
miles = float(input(f"How many miles will you drive the {chosen_key}? "))
print()

# Calculate the gallons of gas needed to drive the specified vehicle the given number of miles.

gas_needed = miles / corresponding_value

# Display the gallons of gas needed
print(f"{gas_needed:.2f} gallon(s) of gas are needed to drive the {chosen_key} {miles} miles")
