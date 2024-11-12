# Create user-defined funtions 

# Defined a non-value returning function
def my_aniaml(name, sound, pound_food):
    print(f"The {name} makes a {sound} noise!")
    print(f"The {name} eats {pound_food} pounds of food a day")
    print(f"The {name} eats {pound_food * 7} pounds of food a week")


# Create a main function - all logic goes here 
def main():
    print("the main function is executing!")
    print()
    # Calling the my_aniaml
    my_aniaml("Cow", "Moo", 110) 

# Call the main function 
if __name__ == "__main__":
    main()
