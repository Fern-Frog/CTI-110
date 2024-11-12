# Create user-defined funtions 

# Defined a non-value returning function
def my_aniaml(name, sound, pound_food):
    print(f"The {name} makes a {sound} noise!")
    print(f"The {name} eats {pound_food} pounds of food a day")
    print(f"The {name} eats {(pound_food * 7):.2f} pounds of food a week")

def getName():
    name = input("Enter your name: ")
    return name + "*-*-*-*-*"

def displayName(first):
    lastName = input("Enter your last name: ")
    fullName = first + " " + lastName
    return fullName + "*-*-*-*-*"

# Create a main function - all logic goes here 
def main():
    print("the main function is executing!")
    print()
    # Calling the my_aniaml
    my_aniaml("Cow", "Moo", 110) 
    print()
    my_aniaml("Deer", "Bleats", 5)
    print()

    # Call the value-returning function 
    myName = getName()
    print(myName)
    print()

    print(displayName(myName))

# Call the main function 
if __name__ == "__main__":
    main()
