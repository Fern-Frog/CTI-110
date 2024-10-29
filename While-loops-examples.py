# While loops example

# While loops requires a conditional statenent

userchoice = input("Want to run the program (y/n)? ").lower()

while userchoice == "y":
    print("The program is running...   ฅ(^•ﻌ•^)ฅ")
    print()
    userchoice = input("Would you like to run the program again (y/n)? ").lower() 
    print()
    
# loop is broken
print("Thanks for runing the program \n")


# Control a while loop using a numeric variable
num = 0

# run the program 5 times 
while num <= 4:
    num += 1 
    print(f"iteration #{num} ")
    
