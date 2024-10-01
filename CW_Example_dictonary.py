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

person1.update({"b_day":"3/8/1018"})

print(person1)

# Update exsting value
person1.update({"age":"50"})

print(person1)
