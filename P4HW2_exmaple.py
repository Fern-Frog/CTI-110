# An similar example to P4HW2
# Add items to a cart abd at the end, show total number of items and total cost

# In Hw the name should controll the loop
product = input('Enter a product or "Exit" to end: ')

#Create Incrementer variables, in Hw ther will be 4
num_products = 0
total_cost = 0

# the loop to control the program 
while product.lower() != "exit":
    num_products += 1
    #num_products = num_products + 1
    cost = float(input(f"What is the cost of {product}: $"))
    total_cost += cost
    print()
    product = input('Enter a product or "Exit" to end: ')

#loop ends here
print(f"Total number of items purchased: {num_products}")
print(f"Total cost of items purchased: ${total_cost:.2f}")
    
#print("Program is ending...")
    



