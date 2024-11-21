#Alta Schwab
#11/19/2024
#P5HW 
#Create text base game using functions


# import libarys
from clrprint import *


# character create function
def create_character():
    # Prompt the user for character details
    name = input("Enter character name: ")
    health = input("Enter character health: ")
    mana = input("Enter character mana: ")

    # Create the character dictionary
    character = {
        "name": name,
        "health": health,
        "mana": mana
    }

    return character

def display_character(character):
    #Display character information with color-coded health based on its value.

    # Extract values from the dictionary
    name = character.get("name", "Unknown")
    health = int(character.get("health", 0))
    mana = int(character.get("mana", 0))
    
    # Determine health color
    if health > 50:
        health_color = "green"
    elif 21 <= health <= 50:
        health_color = "yellow"
    else:  # health <= 20
        health_color = "red"
    
    # Display character info
    clrprint(f"Name: {name}", clr="white")
    clrprint(f"Health: {health}", clr=health_color)
    clrprint(f"Mana: {mana}", clr="blue")

# the main boy
def main():
    print("Game is starting....")
    print()
    char1 = create_character()
    print("---"*7)
    char2 = create_character()
    print()
    display_character(char1)
    print()
    display_character(char2)
    print()
   

    
    
if __name__ == "__main__":
    main()


