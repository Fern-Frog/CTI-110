# Alta Schwab
# 9/24/2024
# In-class Example
# simulate shopping for 3 items and receipt

print("Welcome to ShopCo!\n")

print("You are going to purchase three items \n")

# Get the first item info from user 
item1 = input("Enter name of first item: ")

item1_price = float(input(f"Enter the price of {item1}: "))

item1_quantity = int(input(f"Enter the quantity of {item1}: "))

print()
# Get the second item info from user 
item2 = input("Enter name of second item: ")

item2_price = float(input(f"Enter the price of {item2}: "))

item2_quantity = int(input(f"Enter the quantity of {item2}: "))

print()

# Get the third item info from user 
item3 = input("Enter name of third item: ")

item3_price = float(input(f"Enter the price of {item3}: "))

item3_quantity = int(input(f"Enter the quantity of {item3}: "))

print()
# First half of receipt
print("-----ShopCo Receipt----- \n\n")
print(f"{item1}     {item1_quantity}     ${item1_price * item1_quantity:.2f} \n")

print(f"{item2}     {item2_quantity}     ${item2_price * item2_quantity:.2f} \n")

print(f"{item3}     {item3_quantity}     ${item3_price * item3_quantity:.2f} \n")

print("************************")
# Calculate subtotal
subtotal = (item1_price * item1_quantity) + (item2_price * item2_quantity) + (item3_price * item3_quantity)
# Calculate tax
tax_owed = 0.07 * subtotal
# Calculate final total owed
total_owed = subtotal + tax_owed 

# Second half of receipt
print(f"Subtotal:     ${subtotal:.2f} \n")
print(f"Tax owed:     ${tax_owed:.2f} \n\n")
print(f"Total owed:     ${total_owed:.2f}")
