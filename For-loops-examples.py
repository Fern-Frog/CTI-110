# For loops examples
'''
# Useing the range function with one parameter - range(number of iterations)
for item in range(4):
    print(item)

print()
# Useing the range function with two parameter - range(start, stop)
# The stop value is not inclusive - goes up to, but doesn't include the stop value
for items in range(4,14):
    print(items)

print()
# Useing the range function with three parameter - range(start, stop, step)
for itemss in range(4, 144, 20):
    print(itemss)
'''

rodents = ["Mice", "Rat", "Chipmunks", "Chinchilla", "Beaver", "Gopher", "Capybara","Hamster"]

# Iterate through the list
for rodent_type in rodents:
    print(f"{rodent_type}!")
    print("********")
print("That was a Mouse-terpiece")
print("Loop has ended \n")


# User determines number of times list runs
times_to_run = int(input("How many time to run the loop? "))
for itemsss in range(times_to_run):
    print("program is runing")
    print()


