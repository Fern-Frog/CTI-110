# In class example using loops to validate user inputs

numItems =  int(input("HOw many items will you purchase? "))

# Making the lists
storeItems = ["Coconut","Eggs", "Soup", "Beans", "Bagel","Brooms",
              "Coffee", "Dishwasher", "Lobster", "Newspaper", "TVs", "Games",
              "Apples", "Pasta", "Butter", "Tuna"]

cart=[]


#Show user list
print(*storeItems)


# For loop to iterate numItems times
for item in range(numItems):
    userInput = input (f"Enter item #{item + 1}: ")
    while userInput not in storeItems:
        print(f"{userInput} is not in stock!")
        userInput = input(f"Enter item #{item}: ")
    #Once valid inpput is given, add it to a list
    cart.append(userInput)

print()
print("You are done with shopping!!")
print()
print("Here are the items you purchased")
#Loop through cacrt and print each item
for i in cart:
    print(i)
        
        
    
