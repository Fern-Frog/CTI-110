# In-class dictionary examples

# Dictionary hold key: value pairs

# Create a dictionary
person1 = {"name":"Rob", "age":34, "height":50.2}

# Get values from dictonary
print(person1["age"])
print()

print(f"The student's name is {person1['name']}")

# Add a key: value pair to the dictionary
person1["sID"] = 509

person1.update({"b_day":"3/8/1018","address":"345 Main Dr."})

print(person1)

'''
# Update exsting value
person1.update({"age":"50"})

print(person1)

print("\n \n")

# Remove a key:value pair  from the dictionary
del person1["height"] 
print(person1)
'''
print("\n \n")

# Print all the keys in the dictionary
print(person1.keys()) 
print()
# Prompt the user to give one of the keys
chosen_key = input("Input key to request value: ")

# Get the value from the key and save it in a variable
chosen_value = (person1[chosen_key])

# Diplay requested value to user
print(f"The key you gave is {chosen_key} the value is {chosen_value}")
print("\n\n")

# Allow the user to give a key and value to add to the dictionary 

new_key = input("Give a new key to add: ")
print()
new_value = input(f"Give a value for {new_key}: ")
print()

# Add user input to dictionary
person1.update({new_key:new_value})

print(person1)

