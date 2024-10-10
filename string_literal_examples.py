# In-class examples using strings 

# Create a string
my_string = "SquiD!!"

# Print each character in the list
for char in my_string:
    print(char)
print()    

# Return a character by its index
print(my_string[5])

# Return a series of characters
# Ending index is not inclusive, so add 1 (it won't inclue last index as part of what to show)
print(my_string[5:7])

# From index 0 ending with index 6
print(my_string[:7])
# Just playing arould 
print(my_string[2:])
print(my_string[:4])
print()

#Getting the number of characters in the string
print(f"There are {len(my_string)} characters in the string!")

