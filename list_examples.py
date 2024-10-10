# In-class examples using lists

# Create empty list, lists start at index 0
octopuses = ["Giant Pacific octopus", "Common octopus", "Mimic octopus", "Coconut octopus", "Blue-Ringed octopus", "Dumbo octopus",
             "Bimac octopus","Blanket octocpus"]

#Get number of item in list
print(f"There are {len(octopuses)} octopuses in my list.\n")

# Get Mimic octopus from the list
print(octopuses[2])
print()

# Get 2 tpye of octopuses
print(octopuses[3:5])
print()

# Print all items in list
for friend in octopuses:
    print(friend)
print()
print()
print()


# Allow user to give list items
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
num3 = float(input("Enter a number: "))
num4 = float(input("Enter a number: "))

'''
# Create empty list
num_list = []

# Add variables to the list
num_list.append(num1)
num_list.append(num2)
num_list.append(num3)
num_list.append(num4)

# Print list
print(num_list)
'''

# Create list with variables
num_list = [num1, num2, num3, num4]

# Print list
print(num_list)
print()

# Using functions with a list
print(f"The lowest value is {min(num_list)}!")
print(f"The highest value is {max(num_list)}!")
print(f"The sum of values is {sum(num_list)}!")

