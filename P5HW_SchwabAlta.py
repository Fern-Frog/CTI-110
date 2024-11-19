#Alta Schwab
#11/19/2024
#P5HW 
#Create text base game using functions


# import libarys
import clrprint


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

# display character code
def display_character(character):
    for key, value in character.items():
        if key == "health":
            health_value = int(value)
            # Determine health color
            if health_value <= 20:
                clrprint.clrit(f"{key.capitalize()}: {value}", color="red")
            elif 21 <= health_value <= 50:
                clrprint.clrit(f"{key.capitalize()}: {value}", color="yellow")
            else:
                clrprint.clrit(f"{key.capitalize()}: {value}", color="green")
        else:
            print(f"{key.capitalize()}: {value}")



# the main boy
def main():
    print("Game is starting....")
    print()
    char1 = create_character()
    #char2 = create_character()
    print()
    display_character(char1)
    print()
   # display_character(char2)
    print()
   

    
    
if __name__ == "__main__":
    main()
