#Alta Schwab
#11/19/2024
#P5HW 
#Create text base game using functions

# import libarys

import textwrap
import time
import random
import sys
# character create function
def create_character():
    # Prompt the user for character details
    name = input("Enter character name: ")
    health = int (input("Enter character health: "))
    sanity = int (input("Enter character sanity: "))

    # Create the character dictionary
    character = {
        "name": name,
        "health": health,
        "sanity": sanity,
         # Track if the player has already fought in the kitchen
        "has_fought_kitchen": False,
        "has_brass_key": False,
        "has_looked_at_painting": False,
        "has_rat": False,
        "has_fought_garden": False,
        "has_owl_ally": False
    }

    return character

def check_status(character):
    character["health"] = max(character["health"], 0)  # Ensure health is not negative
    character["sanity"] = max(character["sanity"], 0)  # Ensure sanity is not negative
    
    if character["health"] <= 0:
        print("\nYour health has dropped to 0. You collapse and the world fades to black.")
        print("GAME OVER")
        sys.exit()  # End the game
    
    if character["sanity"] <= 0:
        print("\nYour sanity has dropped to 0. You lose yourself to the madness of this cursed house.")
        print("GAME OVER")
        sys.exit()  # End the game


def display_character(character, previous_function):
    #Display character information with color-coded health based on its value.

    # Extract values from the dictionary
    name = character.get("name", "Unknown")
    health = int(character.get("health", 0))
    sanity = int(character.get("sanity", 0))

    # Display character info
    print(f"Name: {name}")
    print(f"Health: {health}")
    print(f"Sanity: {sanity}")

    input("\nPress Enter to return...")
    previous_function()

# Reusable menu function
def display_menu(prompt, options, width=70):
    print("\n" + "\n".join(textwrap.wrap(prompt, width)))  # Display the story or prompt
    print("What do you do?\n")
    
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")  # Numbered list of options
    
    while True:
        try:
            choice = int(input("\nEnter the number of your choice: ")) - 1
            if 0 <= choice < len(options):
                return choice
            else:
                print("Invalid choice. Please choose a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Inventory system
inventory = {}

def inventory_menu(character, previous_function, combat_mode=False, owl_combat=False, enemies=None, boss_combat=False):
    # Display the current inventory
    if not inventory:
        print("Your backpack is empty.")
    else:
        print("You take a look into your backpack and see:")
        inventory_list = list(inventory.items())

        # Print the inventory with a numbered list
        for idx, (item, description) in enumerate(inventory_list, 1):
            print(f"{idx}. {item}: {description}")

        try:
            choice = int(input("\nEnter the number of the item to interact with (or 0 to exit): "))
            if choice == 0:
                print("\nYou close your backpack.")
            elif 1 <= choice <= len(inventory_list):
                selected_item = inventory_list[choice - 1][0]

                # Pass combat-specific parameters if in combat
                if combat_mode:
                    return interact_with_item(selected_item, character, owl_combat=owl_combat, enemies=enemies, boss_combat=boss_combat)
                else:
                    interact_with_item(selected_item, character)
            else:
                print("\nInvalid choice. Please select a valid item number.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

    # Prompt to return to the previous menu if not in combat
    if not combat_mode:
        input("\nPress Enter to return...")
        previous_function()


    # Prompt to return to the previous menu
    input("\nPress Enter to return...")
    previous_function()


def interact_with_item(item_name, character, owl_combat=False, enemies=None, boss_combat=False):
    if item_name == "Magic Orb":
        use_magic_orb(character)  # Handle using the Magic Orb
    elif item_name == "Brass Key":
        print("\nThe Brass Key feels cold to the touch. It might unlock something important.")
    elif owl_combat and item_name == "Dead Rat":
        print("\n" + "\n".join(textwrap.wrap(
            "You hold out the dead rat. The owl pauses mid-strike, its glowing eyes narrowing as it sniffs the air. "
            "'A worthy offering,' it says, taking the rat with its talons and consuming it swiftly. "
            "'You are not an enemy, but a traveler in search of something greater. I shall aid you.'"
        )))
        character["sanity"] += 30
        remove_item("Dead Rat")
        return "befriended"
          
    elif (owl_combat or boss_combat) and item_name == "Bomb":
        if enemies is not None:  # Ensure enemies are provided
            use_bomb(character, enemies)
        else:
            print("There are no enemies to target with the bomb.")
    else:
        print(f"\nYou inspect the {item_name}, but nothing happens.")


def use_bomb(character, enemies):
    bomb_damage = 50
    if enemies:  # Ensure enemies list is valid
        for enemy in enemies:
            if enemy["health"] > 0:  # Apply damage only to active enemies
                enemy["health"] -= bomb_damage
                print(f"The bomb explodes, dealing {bomb_damage} damage to {enemy['name']}!")
                remove_item("Bomb")
    else:
        print("There are no enemies to attack with the bomb.")



def add_item(item_name, item_description):
    #Add an item to the inventory.
    inventory[item_name] = item_description
    print(f"You have obtained: {item_name}.")

    

def remove_item(item_name):
    #Remove an item from the inventory.
    if item_name in inventory:
        del inventory[item_name]
        print(f"You have used: {item_name}.")
    else:
        print(f"{item_name} is not in your inventory.")
    
# Front door path
def front_door_path(character, previous_function):
     story_text = (
         "You turn to the front door. You see where the doorknob should be but there is nothing."
         "There is only a spyhole on the door. You look through it but don’t see anything but "
         "a black abyss that stretches as far as you can see. But even after seeing this you feel "
         "no fear, only the feeling of yearning growing."
         "You turn back towards the room more determined to find answers.")
     # Update sanity value
     character["sanity"] = max(0, character["sanity"] - 5)
     check_status(character)
     
     
     choices = [
         "Go the the kitchen", 
         "Go to the library", 
         "Go to the dungeon", 
         "Look around the entryway", 
         "Look in inventory",
         "Display Character"
    ]

     selected_option = display_menu(story_text, choices)
    
     if selected_option == 0:
        kitchen_path(character, front_door_path)
     elif selected_option == 1:
        library_path(character)
     elif selected_option == 2:
        dungeon_path(character)
     elif selected_option == 3:
        look_entryway(character)
     elif selected_option == 4:
        inventory_menu(character, lambda: front_door_path(character))
     elif selected_option == 5:
        display_character(character, lambda: front_door_path(character))
     else:
        print("\nSomething went wrong!")

# Combat function with rat and utensils
def combat_rat(character):
    print("\n" + "\n".join(textwrap.wrap(
        "From out of the dark corner of the room you see a huge rat scurrying toward you."
        "It stops a few paces from you sitting on their haunches and squeals. 'You dare enter my kitchen? "
        "Prepare to face my wrath!' The rat lifted their claw and pointed at you. "
        "You hear utensils clatter around you as they move to attack you!"
    )))

    # Combat stats
    enemies = [
        {"name": "Rat", "health": 30, "attack": (6, 10)},
        {"name": "Animated Utensils", "health": 10, "attack": (4, 6)},
    ]

    character["health"]
    base_damage = 5  # Base player damage
    weapon_bonus = 0

    # Check if the player has a weapon equipped
    if "Weapon" in inventory:
        weapon_bonus = 10
        print(f"You are wielding {inventory['Weapon']}! Damage bonus: {weapon_bonus}")

    # Combat loop
    while character["health"] > 0 and any(enemy["health"] > 0 for enemy in enemies):
        # Display player's health and enemies' status
        print(f'\nYour health: {character["health"]}')
        print("Enemies:")
        for i, enemy in enumerate(enemies):
            status = f"{enemy['health']} HP" if enemy["health"] > 0 else "Defeated"
            print(f"{i + 1}. {enemy['name']} ({status})")

        # Player's turn
        print("\nChoose your action:")
        print("1. Attack an enemy")
        print("2. Use an item from inventory")
        
        choice = input("\nEnter the number of your choice: ")

        if choice == "1":  # Attack an enemy
            # Let the player choose which enemy to attack
            target_index = None
            while target_index is None:
                try:
                    target_index = int(input("Choose an enemy to attack (enter the number): ")) - 1
                    if not (0 <= target_index < len(enemies)) or enemies[target_index]["health"] <= 0:
                        print("Invalid choice. Choose a living enemy.")
                        target_index = None
                except ValueError:
                    print("Invalid input. Enter a number.")

            # Attack the chosen enemy
            damage = random.randint(base_damage, base_damage + 5) + weapon_bonus
            enemies[target_index]["health"] -= damage
            print(f"You attack {enemies[target_index]['name']} for {damage} damage!")

            if enemies[target_index]["health"] <= 0:
                print(f"{enemies[target_index]['name']} is defeated!")
                
                # Check if the rat is defeated
                if enemies[target_index]["name"] == "Rat":
                    print("With the rat defeated, the animated utensils clatter lifelessly to the floor!")
                    for enemy in enemies:
                        enemy["health"] = 0  # All enemies are defeated
        elif choice == "2":  # Use an item
            # Display a numbered list of items
            if inventory:
                print("\nYour inventory:")
                inventory_items = list(inventory.keys())
                for idx, item in enumerate(inventory_items, 1):
                    print(f"{idx}. {item.capitalize()}")

                # Let the player choose an item by number
                item_index = None
                while item_index is None:
                    try:
                        item_index = int(input("Choose an item to use (enter the number): ")) - 1
                        if not (0 <= item_index < len(inventory_items)):
                            print("Invalid choice. Select an available item.")
                            item_index = None
                    except ValueError:
                        print("Invalid input. Enter a number.")

                item_choice = inventory_items[item_index]
                if item_choice == "Magic Orb":
                    use_magic_orb(character)
                elif item_choice == "Bomb":
                    bomb_damage = 15
                    for enemy in enemies:
                        if enemy["health"] > 0:
                            enemy["health"] -= bomb_damage
                    print(f"You used {item_choice} and dealt {bomb_damage} damage to all enemies!")
                    remove_item(item_choice)
                else:
                    print(f"{item_choice} has no effect in combat.")
            else:
                print("Your inventory is empty!")
        else:
            print("Invalid action. Choose 1 or 2.")

        # Enemies' turn
        for enemy in enemies:
            if enemy["health"] > 0:
                damage = random.randint(*enemy["attack"])
                character["health"] -= damage
                print(f"{enemy['name']} attacks you for {damage} damage!")

        # Check player's status
        character["health"] 
        check_status(character)

    # Return the battle result
    if all(enemy["health"] <= 0 for enemy in enemies):
        print("\nYou have defeated all enemies!")
        return True
    return False
        
def kitchen_path(character, previous_function):
    if not character["has_fought_kitchen"]:  # If the player hasn't fought yet
        story_text = (
            "You open the door to the kitchen and take your first step inside. "
            "When out of the corner of your eyes, you see a fast, dark blur."
        )
        choices = [
            "Enter battle",
            "Go back"
        ]

        selected_option = display_menu(story_text, choices)

        if selected_option == 0:
            # Only call combat if the player has not yet fought
            won = combat_rat(character)
            if won:
                character["has_fought_kitchen"] = True  # Set flag so no more combat will happen in the kitchen
                story_text = (
                    "You cover your nose as across the kitchen rotting food and rat feces are scattered about. "
                    "You see a door on the other side of the room."
                )
                choices = [
                    "Go to the door",
                    "Go to the entryway",
                    "Investigate the rat",
                    "Look around the kitchen",
                    "Look in inventory",
                    "Display character"
                ]

                selected_option = display_menu(story_text, choices)

                if selected_option == 0:
                    examine_door_kitchen(character, lambda: kitchen_path(character, previous_function))
                elif selected_option == 1:
                    entryway_path(character, lambda: kitchen_path(character, previous_function))
                elif selected_option == 2:
                    examine_rat_kitchen(character, previous_function)
                elif selected_option == 3:
                    look_kitchen(character, previous_function)
                elif selected_option == 4:
                    inventory_menu(character, lambda: kitchen_path(character, previous_function))
                elif selected_option == 5:
                    display_character(character, lambda: kitchen_path(character, previous_function))
                else:
                    print("\nSomething went wrong!")
            else:
                print("\nYou were defeated and can't continue your journey for now.")
                return  # End the function if the player loses the fight

        elif selected_option == 1:
            # If the player chooses to go back
            previous_function()  # Use the provided previous_function
        else:
            print("\nInvalid choice.")
    else:
        print("\nThe kitchen is quiet. You don't see any more enemies.")
        story_text = (
            "You stand in the quiet kitchen, the eerie silence enveloping the space. "
            "The rat's lifeless body lies still, and the room is in disarray."
        )
        choices = [
            "Go to the door",
            "Go to the entryway",
            "Look around the kitchen",
            "Investigate the rat",
            "Look in inventory",
            "Display character"
        ]

        selected_option = display_menu(story_text, choices)

        if selected_option == 0:
            examine_door_kitchen(character, lambda: kitchen_path(character, previous_function))
        elif selected_option == 1:
            entryway_path(character, lambda: kitchen_path(character, previous_function))
        elif selected_option == 2:
            look_kitchen(character, previous_function)
        elif selected_option == 3:
            examine_rat_kitchen(character, previous_function)
        elif selected_option == 4:
            inventory_menu(character, lambda: kitchen_path(character, previous_function))
        elif selected_option == 5:
            display_character(character, lambda: kitchen_path(character, previous_function))
        else:
            print("\nSomething went wrong!")


def examine_door_kitchen(character, previous_function):
    story_text = ("You approach the door at the far end of the kitchen. Its surface is weathered and splintered, and the handle is cold to the touch. "
                  "Just above the handle, a rusted metal sign is nailed to the door. The words are barely legible, but you make them out: "
                  "*'BEWARE: DO NOT STEP OUTSIDE WITHOUT PROPER PROTECTION.'*")
    choices = [
        "Open the door",
        "Step away",
        "Look in inventory",
        "Display character"
    ]
    selected_option = display_menu(story_text, choices)

    if selected_option == 0:
        go_garden_path(character, lambda: examine_door_kitchen(character, previous_function))
    elif selected_option == 1:
        kitchen_path(character, previous_function)
    elif selected_option == 2:
        inventory_menu(character, lambda: examine_door_kitchen(character, previous_function))
    elif selected_option == 3:
        display_character(character, lambda: examine_door_kitchen(character, previous_function))
    else:
        print("\nSomething went wrong!")


def examine_rat_kitchen(character, previous_function):
    story_text = ("")
    
    if not character.get("has_rat", False):  
        print("\nYou kneel down to examine the rat’s body."
              "Though it has shrunk to a normal size, the unnatural gleam in its eyes hasn’t completely faded.")
        pick_up = input("Do you want to pick it up? (yes/no): ").lower()
        if pick_up == "yes":
            character["has_rat"] = True
            add_item("Dead Rat", "the unnatural gleam in its eyes hasn’t completely faded")
        else:
            print("\nYou leave the rat on the floor.")
    else:
        print("\nYou already picked up the rat.")
    look_kitchen(character, previous_function)


def look_kitchen(character, previous_function):
    story_text = ("You look around the kitchen."
                  "The walls are lined with cracked tiles, and the counters are cluttered with rusted utensils, "
                  "broken dishes, and piles of rotting food. "
                  "A few intact jars of spices and strange herbs sit on a high shelf, untouched by time."
                  "The smell is overpowering, and you instinctively cover your face. ")

    choices = [
        "Check the stove",
         "Look at the shelves",
        "Investigate the rat",
        "Go to the door",
        "Go to the entryway",
        "Look in inventory",
        "Display character"
    ]
    selected_option = display_menu(story_text, choices)

    if selected_option == 0:
        examine_oven_kitchen(character, lambda: look_kitchen(character, previous_function))
    elif selected_option == 1:
        examine_shelfs_kitchen(character, lambda: look_kitchen(character, previous_function))
    elif selected_option == 2:
        examine_rat_kitchen(character, previous_function)
    elif selected_option == 3:
        examine_door_kitchen(character, previous_function)
    elif selected_option == 4:
        entryway_path(character, lambda: look_kitchen(character, previous_function))
    elif selected_option == 5:
        inventory_menu(character, lambda: look_kitchen(character, previous_function))
    elif selected_option == 6:
        display_character(character, lambda: look_kitchen(character, previous_function))
    else:
        print("\nSomething went wrong!")


def examine_oven_kitchen(character, previous_function):
    story_text = (
        "You walk toward the old cast-iron stove. The surface is caked in grime, "
        "and the rusted door is stuck shut. You see that in the grime '4: 3' has been written.")
    
    choices = ["Go back"]
    selected_option = display_menu(story_text, choices)
    
    if selected_option == 0:
        previous_function()
    else:
        print("\nSomething went wrong!")


def examine_shelfs_kitchen(character, previous_function):
    if "Bomb" not in inventory:  # Check if the bomb has already been taken
        print("\n" + "\n".join(textwrap.wrap("The kitchen shelves are old, their wooden beams sagging under the weight of various jars and bottles. "
                      "Most of them are covered in dust, but one shelf catches your attention. Among the jars of strange herbs and spices, a **small wooden box** sits, almost hidden behind a large jar of pickles."
                      "Upon opening it, you find a Bomb.")))
        
        pick_up = input("Do you want to pick it up? (yes/no): ").lower()
        if pick_up == "yes":
            add_item("Bomb", "")
        else:
            print("\nYou decided not to take the Bomb.")
    else:
        print("\nThe shelves are empty. You already took the Bomb.")
    previous_function()


def go_garden_path(character, previous_function):
    if "Protective Gear" not in inventory:
        story_text = ("You push the door open, and immediately, an overwhelming feeling of dread washes over you. "
                      "Your vision blurs as you take a step outside, and the world around you dissolves into an endless, yawning void. "
                      "You feel yourself teetering on the edge of sanity as the void stares back, consuming every thought and memory you hold dear.")
        choices = ["Retreat immediately"]
        selected_option = display_menu(story_text, choices)
        
        character["sanity"] -= 20  # Substantial sanity loss for entering without protection
        check_status(character)
        
        if selected_option == 0:
            kitchen_path(character, previous_function)
    else:
        print("\n" + "\n".join(textwrap.wrap(
        "You step into the garden, the protective gear shielding you from the oppressive void outside. "
                    "The air is unnaturally still, and the sky above is a swirling black void. The garden itself is overgrown with twisted, blackened vines and strange, pulsing flowers. "
                    "In the center of the garden, a large, ancient tree looms, its gnarled branches stretching toward the void like skeletal hands. "
            )))

        garden_path(character, previous_function)
        
        

        

def garden_path(character, previous_function):
    if not character["has_fought_garden"]:  # If the player hasn't fought yet
        story_text = (
            "As you approach the tree, you see a pair of glowing eyes staring at you from a hollow in its trunk. "
            "The eyes belong to a large owl with feathers that shimmer like starlight. The owl speaks: "
            "'You dare to tread in my domain? Prove your worth, or face my talons!'"
        )
        choices = [
            "Enter combat",
            "Go back to the kitchen",
            "Look in inventory",
            "Display character"
        ]
        selected_option = display_menu(story_text, choices)

        if selected_option == 0:
            # Only call combat if the player has not yet fought
            owl_outcome = combat_owl(character)
            character["has_fought_garden"] = True  # Flag to indicate owl combat is resolved

            # Record owl's fate
            if owl_outcome == "befriended":
                character["owl_ally"] = True
                character["has_owl_ally"] = True
            elif owl_outcome == "defeated":
                character["owl_ally"] = False 
            garden_path(character, previous_function)

        elif selected_option == 1:
            kitchen_path(character, previous_function)
        elif selected_option == 2:
            inventory_menu(character, lambda: garden_path(character, previous_function))
        elif selected_option == 3:
            display_character(character, lambda: garden_path(character, previous_function))
        else:
            print("\nSomething went wrong!")

    else:
        # Adjust garden description based on owl's fate
        if character.get("owl_ally", False):
            print("\nThe garden is peaceful, and the owl watches over you from its perch. It nods in recognition.")
            print("\n" + "\n".join(textwrap.wrap(
        "With the owl's defeat, the garden is quieter now, though an eerie stillness remains. As you look around, you notice a large pile of withered leaves near the base of the tree. "
"Curious, you approach and carefully push aside the leaves."  
        )))
            if "Star Sigil" not in inventory:  # Check if the orb has already been taken
                print("\nHidden beneath the decaying foliage, you find a star-shaped sigil faintly glowing.")
                pick_up = input("Do you want to pick it up? (yes/no): ").lower()
                if pick_up == "yes":
                    add_item("Star Sigil", "")
                else:
                    print("\nYou decided not to take the Star Sigil.")
            else:
                print("\nThe leaves is empty. You already took the Star Sigil.")
            story_text = ("")
            choices = [
            "Go back to the kitchen",
            "Look in inventory",
            "Display character"
            ]
            selected_option = display_menu(story_text, choices)
            if selected_option == 0:
                kitchen_path(character, previous_function)
            elif selected_option == 1:
                inventory_menu(character, lambda: garden_path(character, previous_function))
            elif selected_option == 2:
                display_character(character, lambda: garden_path(character, previous_function))
            else:
                print("\nSomething went wrong!")
        else:
            print(
                "\nThe garden feels tense, as the dead body of the owl lays there. "
                "The hollow in the tree trunk is empty, a reminder of the battle."
            )
            print("\n" + "\n".join(textwrap.wrap(
        "With the owl's defeat, the garden is quieter now, though an eerie stillness remains. As you look around, you notice a large pile of withered leaves near the base of the tree. "
"Curious, you approach and carefully push aside the leaves."  
        )))
            if "Star Sigil" not in inventory:  # Check if the orb has already been taken
                print("\nHidden beneath the decaying foliage, you find a star-shaped sigil faintly glowing.")
                pick_up = input("Do you want to pick it up? (yes/no): ").lower()
                if pick_up == "yes":
                    add_item("Star Sigil", "")
                else:
                    print("\nYou decided not to take the Star Sigil.")
            else:
                print("\nThe leaves is empty. You already took the Star Sigil.")
            story_text = ("")
            choices = [
            "Go back to the kitchen",
            "Look in inventory",
            "Display character"
            ]
            selected_option = display_menu(story_text, choices)
            if selected_option == 0:
                kitchen_path(character, previous_function)
            elif selected_option == 1:
                inventory_menu(character, lambda: garden_path(character, previous_function))
            elif selected_option == 2:
                display_character(character, lambda: garden_path(character, previous_function))
            else:
                print("\nSomething went wrong!")
        

        


def combat_owl(character):
    print("\n" + "\n".join(textwrap.wrap(
        "The owl swoops down from its perch, its talons gleaming dangerously. As it lands in front of you, its massive wings create a gust of wind that stirs the dark vines around you. "
        "'Your presence is an insult to this sacred place,' it says, preparing to attack."
    )))


    # Combat stats
    enemies = [{"name": "Owl", "health": 60, "attack": (10, 20)}]
    base_damage = 5  # Base player damage
    weapon_bonus = 10 if "weapon" in inventory else 0

    # Combat loop
    while character["health"] > 0 and any(enemy["health"] > 0 for enemy in enemies):
        # Display player's health and enemy's status
        print(f'\nYour health: {character["health"]}')
        print("Enemies:")
        for enemy in enemies:
            status = f"{enemy['health']} HP" if enemy["health"] > 0 else "Defeated"
            print(f"{enemy['name']} ({status})")

        # Player's turn
        print("\nChoose your action:")
        print("1. Attack the owl")
        print("2. Use an item from inventory")

        choice = input("\nEnter the number of your choice: ").strip()

        if choice == "1":  # Attack the owl
            damage = random.randint(base_damage, base_damage + 5) + weapon_bonus
            enemies[0]["health"] -= damage
            print(f"You attack the owl for {damage} damage!")

            if enemies[0]["health"] <= 0:
                print("\nThe owl has been defeated!")
                break

        elif choice == "2":  # Use an item
            outcome = inventory_menu(character, lambda: None, combat_mode=True, owl_combat=True, enemies=enemies)
            if outcome == "befriended":
                print("\nThe owl accepts your offering and becomes your ally!")
                return "befriended"

        else:
            print("Invalid action. Choose 1 or 2.")
            continue

        # Owl's turn
        for enemy in enemies:
            if enemy["health"] > 0:
                damage = random.randint(*enemy["attack"])
                character["health"] -= damage
                print(f"The owl attacks you for {damage} damage!")

        # Check player's status
        if character["health"] <= 0:
            print("\nYou have been defeated by the owl!")
            check_status(character)
            return None

    # Return combat outcome
    if character["health"] > 0:
        print("\nYou defeated the owl!")
        return "defeated"



# Entryway path
def entryway_path(character, previous_function):
    story_text = ("You enter into the entryway.")

    choices = [
         "Go to the kitchen", 
         "Go to the library", 
         "Go to the dungeon",
         "Go to the front door",
         "Look around the entryway", 
         "Look in inventory",
         "Display Character"
    ]

    selected_option = display_menu(story_text, choices)

    if selected_option == 0:
        kitchen_path(character, lambda: entryway_path(character, previous_function))
    elif selected_option == 1:
        library_path(character, lambda: entryway_path(character, previous_function))
    elif selected_option == 2:
        dungeon_path(character, lambda: entryway_path(character, previous_function))
    elif selected_option == 3:
        front_door_path(character, lambda: entryway_path(character, previous_function))
    elif selected_option == 4:
        look_entryway(character, previous_function)
    elif selected_option == 5:
        inventory_menu(character, lambda: entryway_path(character, previous_function))
    elif selected_option == 6:
        display_character(character, lambda: entryway_path(character, previous_function))
    else:
        print("\nInvalid choice.")

# Look around entryway
def look_entryway(character, previous_function):
    story_text = ("You decide to examine the entryway more closely. The warped floorboards groan under your "
                  "weight as you take in the room’s eerie atmosphere. Despite the decay, there are remnants "
                  "of the house’s former elegance. You see a faded family portrait on the wall. A small table "
                  "with a single drawer near the bottom of the stairs. A rug in the center of the room,"
                  "frayed at the edges and covering part of the floorboards. A coat rack, its hooks empty "
                  "except for a dusty cloak.")
    
    choices = [
        "Examine the portrait",
        "Open the drawer on the table",
        "Look under the rug",
        "Inspect the cloak",
        "Go to the kitchen",
        "Go to the library",
        "Go to the dungeon",
        "Look in inventory",
        "Display character"
    ]

    selected_option = display_menu(story_text, choices)

    if selected_option == 0:
        examine_portrait(character, previous_function)  
    elif selected_option == 1:
        examine_drawer_entryway(character, previous_function) 
    elif selected_option == 2:
        examine_rug_entryway(character, previous_function)  
    elif selected_option == 3:
        examine_coat_entryway(character, previous_function)  
    elif selected_option == 4:
        kitchen_path(character, lambda: look_entryway(character, previous_function)) 
    elif selected_option == 5:
        library_path(character, lambda: look_entryway(character, previous_function))  
    elif selected_option == 6:
        dungeon_path(character, lambda: look_entryway(character, previous_function))  
    elif selected_option == 7:
        inventory_menu(lambda: look_entryway(character, previous_function))  
    elif selected_option == 8:
        display_character(character, lambda: look_entryway(character, previous_function))
    else:
        # Fallback for an invalid option, which shouldn't normally happen.
        print("\nSomething went wrong! Please try again.")

# Examine the portrait
def examine_portrait(character, previous_function):
    story_text = ('You step closer to the portrait. The figures in the painting are blurred, '
                  'their faces smeared as if by some unseen hand. Beneath the frame, a small brass plaque reads: '
                  '"The Eldridge Family, 1874. The year the secrets began.”')
    character["has_looked_at_painting"] = True
    
    choices = [
        "Open the drawer on the table",
        "Look under the rug",
        "Inspect the cloak",
        "Go to the kitchen",
        "Go to the library",
        "Go to the dungeon",
        "Look in inventory",
        "Display character"
    ]

    selected_option = display_menu(story_text, choices)

    if selected_option == 0:
        examine_drawer_entryway(character, previous_function) 
    elif selected_option == 1:
        examine_rug_entryway(character, previous_function)  
    elif selected_option == 2:
        examine_coat_entryway(character, previous_function)  
    elif selected_option == 3:
        kitchen_path(character, lambda: look_entryway(character, previous_function)) 
    elif selected_option == 4:
        library_path(character, lambda: look_entryway(character, previous_function))  
    elif selected_option == 5:
        dungeon_path(character, lambda: look_entryway(character, previous_function))  
    elif selected_option == 6:
        inventory_menu(lambda: look_entryway(character, previous_function))  
    elif selected_option == 7:
        display_character(character, lambda: look_entryway(character, previous_function))
    else:
        # Fallback for an invalid option, which shouldn't normally happen.
        print("\nSomething went wrong! Please try again.")


# Examine the entryway drawer
def examine_drawer_entryway(character, previous_function):
    story_text = ("")
    
    if not character.get("has_brass_key", False):  
        print("\nThe drawer resists at first, swollen from years of damp, but you manage to yank it open. "
              "Inside, you find a brass key. You pick it up and notice the letter 'L' engraved on its surface.")
        pick_up = input("Do you want to pick it up? (yes/no): ").lower()
        if pick_up == "yes":
            character["has_brass_key"] = True
            add_item("Brass Key","the letter 'L' engraved on its surface")
        else:
            print("\nYou leave the key in the drawer.")
    else:
        print("\nThe drawer is empty now; you already picked up the key.")

    # Choices for the player
    choices = [
        "Examine the portrait",
        "Look under the rug",
        "Inspect the cloak",
        "Go to the kitchen",
        "Go to the library",
        "Go to the dungeon",
        "Look in inventory",
        "Display character"
    ]

    # Display menu and process selection
    selected_option = display_menu(story_text, choices)

    if selected_option == 0:
        examine_portrait(character, previous_function) 
    elif selected_option == 1:
        examine_rug_entryway(character, previous_function)  
    elif selected_option == 2:
        examine_coat_entryway(character, previous_function)  
    elif selected_option == 3:
        kitchen_path(character, lambda: look_entryway(character, previous_function)) 
    elif selected_option == 4:
        library_path(character, lambda: look_entryway(character, previous_function))  
    elif selected_option == 5:
        dungeon_path(character, lambda: look_entryway(character, previous_function))  
    elif selected_option == 6:
        inventory_menu(lambda: look_entryway(character, previous_function))  
    elif selected_option == 7:
        display_character(character, lambda: look_entryway(character, previous_function))
    else:
        # Fallback for an invalid option, which shouldn't normally happen.
        print("\nSomething went wrong! Please try again.")

# Examine the entryway rug
def examine_rug_entryway(character, previous_function):
    story_text = ("You lift the rug, revealing warped and rotting floorboards beneath."
              "A faint, damp smell lingers, but there's nothing of interest here. "
              "You set the rug back in place.")
    choices = [
        "Examine the portrait",
        "Open the drawer on the table",
        "Inspect the cloak",
        "Go to the kitchen",
        "Go to the library",
        "Go to the dungeon",
        "Look in inventory",
        "Display character"
    ]

    selected_option = display_menu(story_text, choices)

    if selected_option == 0:
        examine_portrait(character, previous_function) 
    elif selected_option == 1:
        examine_drawer_entryway(character, previous_function)  
    elif selected_option == 2:
        examine_coat_entryway(character, previous_function)  
    elif selected_option == 3:
        kitchen_path(character, lambda: look_entryway(character, previous_function)) 
    elif selected_option == 4:
        library_path(character, lambda: look_entryway(character, previous_function))  
    elif selected_option == 5:
        dungeon_path(character, lambda: look_entryway(character, previous_function))  
    elif selected_option == 6:
        inventory_menu(lambda: look_entryway(character, previous_function))  
    elif selected_option == 7:
        display_character(character, lambda: look_entryway(character, previous_function))
    else:
        # Fallback for an invalid option, which shouldn't normally happen.
        print("\nSomething went wrong! Please try again.")

# Examine the coat
def examine_coat_entryway(character, previous_function):

        print("\nIn the pocket, you feel a scrap of paper. "
              "It’s faint, but you can make out the number 2: 3 scrawled in faded ink. ")
            
        story_text = ("")
    # Choices for the player
        choices = [
        "Examine the portrait",
        "Look under the rug",
        "Open the drawer on the table",
        "Go to the kitchen",
        "Go to the library",
        "Go to the dungeon",
        "Look in inventory",
        "Display character"
        ]

    # Display menu and process selection
        selected_option = display_menu(story_text, choices)

        if selected_option == 0:
            examine_portrait(character, previous_function) 
        elif selected_option == 1:
            examine_rug_entryway(character, previous_function)  
        elif selected_option == 2:
            examine_drawer_entryway(character, previous_function)  
        elif selected_option == 3:
            kitchen_path(character, lambda: look_entryway(character, previous_function)) 
        elif selected_option == 4:
            library_path(character, lambda: look_entryway(character, previous_function))  
        elif selected_option == 5:
            dungeon_path(character, lambda: look_entryway(character, previous_function))  
        elif selected_option == 6:
            inventory_menu(lambda: look_entryway(character, previous_function))  
        elif selected_option == 7:
            display_character(character, lambda: look_entryway(character, previous_function))
        else:
            # Fallback for an invalid option, which shouldn't normally happen.
            print("\nSomething went wrong! Please try again.")

    # libary path
def library_path(character, previous_function):
    story_text = ("You step into the library. The air is heavy with the scent of old paper and mildew, "
                  "and the room is cloaked in a dim, somber light.")

    choices = [
        "Look around the room",
        "Go back to the entryway",
        "Look in inventory",
        "Display character"
    ]

    selected_option = display_menu(story_text, choices)

    if selected_option == 0:
        look_libarary(character, lambda: library_path(character, previous_function))
    elif selected_option == 1:
        previous_function()  # Return to the entryway or wherever the player came from.
    elif selected_option == 2:
        inventory_menu(lambda: library_path(character, previous_function))
    elif selected_option == 3:
        display_character(character, lambda: library_path(character, previous_function))
    else:
        print("\nSomething went wrong!")


# looking around the library
def look_libarary(character, previous_function):
    story_text = ("You take a moment to observe your surroundings in detail. "
                  "The library is cramped, with walls lined by sagging bookshelves filled with ancient, dust-covered "
                  "tomes. A heavy desk sits in the far corner of the room, "
                  "its surface cluttered with wax-stained papers, a half-melted candle, and what looks like an old, "
                  "sealed drawer."
                  "To your left, a faded rug sprawls across the floor, covering something uneven beneath it. "
                  "On the right, one particular bookshelf stands out. Its books are arranged too neatly compared "
                  "to the others, as if someone was trying to hide something.")
    
    choices = [
        "Investigate the desk",
        "Check the bookshelf",
        "Lift the rug",
        "Go back to the entryway",
        "Look in inventory",
        "Display character"
    ]
    
    selected_option = display_menu(story_text, choices)
    if selected_option == 0:
        examine_desk_libaray(character, lambda: look_library(character, previous_function))
    elif selected_option == 1:
        examine_bookshelf_library(character, lambda: look_library(character, previous_function))
    elif selected_option == 2:
        examine_rug_library(character, lambda: look_library(character, previous_function))
    elif selected_option == 3:
        entryway_path(character, previous_function)  # Return to the previous area.
    elif selected_option == 4:
        inventory_menu(lambda: look_library(character, previous_function))
    elif selected_option == 5:
        display_character(character, lambda: look_library(character, previous_function))
    else:
        print("\nSomething went wrong!")

# Library Desk Stuff
def examine_desk_libaray(character, previous_function):
    story_text = ("You approach the desk, its surface marred by time and neglect. "
                  "Wax from a long-extinguished candle clings to the wood, pooling around scattered, "
                  "yellowed papers. Faint marks from hurried writing catch your eye, as if someone once worked "
                  "here in desperation. The brass handle on the drawer is tarnished.")
    
    choices = [
        "Look at papers",
        "Try drawer",
        "Go back looking around the room",
        "Look in inventory",
        "Display character"
    ]

    selected_option = display_menu(story_text, choices)
    if selected_option == 0:
        examine_papers_library(character, lambda: examine_desk_library(character, previous_function))
    elif selected_option == 1:
        examine_drawer_library(character, lambda: examine_desk_library(character, previous_function))
    elif selected_option == 2:
        look_libarary(character, previous_function)
    elif selected_option == 3:
        inventory_menu(lambda: examine_desk_library(character, previous_function))
    elif selected_option == 4:
        display_character(character, lambda: examine_desk_library(character, previous_function))
    else:
        print("\nSomething went wrong!")

# Examine Papers in the Library
def examine_papers_library(character, previous_function):
    print("\nAmong the scattered papers on the desk, you find several pages written in a hurried, shaky hand. "
          "The ink has bled in places, and some words are crossed out or smeared, but you can still make out fragments:")

    story_parts = [
        "This house... it feels alive. Every creak, every shadow—it’s watching, waiting. I came here searching for the artifact, but I fear I’ve found something far worse. Its pull... it’s unbearable.",
        "1: 6",
        "The sigils are the key. They hold the power to unlock the tower, but the cost of using them... I fear what it might demand of me. The Sun, the Moon, the Star—they must align, but how? The carvings speak in riddles, and the whispers... they make it hard to think clearly.",
        "Do not trust what you see in the garden. It’s not real, none of it is. The mask—wear it, or the truth will devour you. I learned this too late. The void... oh, the void... there is no escaping it once it sees you.",
        "I thought I could resist the pull of the artifact, but now I’m not so sure. It whispers to me in the night, calls me by my name... I don’t know how it knows my name. I’m afraid to touch it, yet I cannot bear to leave without it. What lies beyond this house? Does it even matter anymore?",
        "The orb glowed with a soothing light, and when I touched it, my wounds vanished. But something else… something darker… slipped into my mind. Use it if you must, but know the cost."
    ]
    
    current_part = 0

    # Loop through story parts
    while current_part < len(story_parts):
        # Get the current story part
         

        # Display the story part with text wrapping
        print("\n" + "\n".join(textwrap.wrap(story_parts[current_part], width=70)))
        
        # Ask if they want to continue
        choice = input("\nDo you wish to continue reading? (Yes/No): ").strip().lower()

        if choice == "yes":
            current_part += 1  # Move to the next part
        elif choice == "no":
            print("\nYou choose not to continue reading.")
            examine_desk_libaray(character, previous_function)  
            return
        else:
            print("\nInvalid choice. Please type 'Yes' or 'No'.")

    print("You read all the notes")
    time.sleep(2.5)
    
    examine_desk_libaray(character, previous_function) 

    

def examine_drawer_library(character, previous_function):
    if "Brass Key" in inventory:
        if "Magic Orb" not in inventory:  # Check if the orb has already been taken
            print("\nYou use the brass key to unlock the desk. Inside, you find a glowing Magic Orb.")
            pick_up = input("Do you want to pick it up? (yes/no): ").lower()
            if pick_up == "yes":
                add_item("Magic Orb", "A blue glowing orb.")
            else:
                print("\nYou decided not to take the Magic Orb.")
        else:
            print("\nThe desk is empty. You already took the Magic Orb.")
    else:
        print("\nThe desk is locked. You need a key to open it.")
        time.sleep(1)
    
    examine_desk_libaray(character, previous_function)
    
def use_magic_orb(character):
    if "Magic Orb" in inventory:
        print("\nYou hold the glowing Magic Orb in your hands.")
        choice = input("Do you want to use the orb? (yes/no): ").strip().lower()
        if choice == "yes":
            heal_amount = random.randint(20, 50)
            character["health"] += heal_amount
            print(f"\nThe orb heals you for {heal_amount} health! Your health is now {character['health']}.")

            # 25% chance to lower sanity
            if random.random() < 0.25:
                sanity_loss = random.randint(5, 10)
                character["sanity"] = max(0, character["sanity"] - sanity_loss)
                print(f"\nBut something feels off....")
            else:
                print("\nYou feel rejuvenated.")

        
        else:
            print("\nYou decide not to use the Magic Orb right now.")
    else:
        print("\nYou don't have the Magic Orb.")

def examine_bookshelf_library(character, previous_function):
    if character.get("has_looked_at_painting", False):
        story_text = ("As you study the bookshelf, your eyes catch on a single title glowing faintly under the dust: "
                      "The Eldridge Legacy, 1874."
                      "The name feels familiar, stirring a connection to the faded portrait in the entryway."
        )
        print("\n".join(textwrap.wrap(story_text, width=70)))
        if "Sun Sigil" not in inventory:  # Check if the sun has already been taken
            print("\n You pull the book, you hear a faint click."
                  "The bookshelf creaks as a hidden compartment opens, revealing the Sun Sigil.")
            pick_up = input("Do you want to pick it up? (yes/no): ").lower()
            if pick_up == "yes":
                add_item("Sun Sigil", "A radiant symbol of light")
            else:
                 print("\n You don't take the Sun Sigil.")
        else:
             print("\n You already took the Sun Sigil.")
    else:
        story_text = (
            "You scan the bookshelf, running your fingers over the dusty spines."
            "Most of the titles are faded beyond recognition, their lettering worn away by time."
            "As you step back, you notice faint scratch marks on the floor beneath the shelf, as if it has "
            "been moved before. "
        )
        print("\n".join(textwrap.wrap(story_text, width=70)))
        
    look_libarary(character, previous_function)
        

def examine_rug_library(character, previous_function):
    story_text = ('You cautiously lift the rug, revealing a faint carving etched into the floorboards.'
                  'The symbols of the Sun, Moon, and Star are arranged in a triangular pattern.'
                  'Below them, an inscription reads: '
                  '"The heavens must align to reveal the way."'
                  )
    choices = [
        "Place the Sigils",
        "Go back looking around the room",
        "Look in inventory",
        "Display character"
        ]

    selected_option = display_menu(story_text, choices)

    if selected_option == 0:
        tower_entry(character, previous_function)
    elif selected_option == 1:
        look_libarary(character, previous_function)  
    elif selected_option == 2:
        inventory_menu(lambda: examine_rug_library(character))  
    elif selected_option == 3:
        display_character(character, lambda: examine_rug_library(character))  
    else:
        print("\nSomething went wrong!")



def tower_entry(character, previous_function):
    required_sigils = {"Sun Sigil", "Moon Sigil", "Star Sigil"}
    player_sigils = set(item for item in inventory.keys() if "Sigil" in item)

    if required_sigils.issubset(player_sigils):
        print("\nThe three Sigils glow brightly as you place them into the tower door's indentations.")
        print("With a deep rumble, the door opens, revealing a staircase leading upward into the tower.")
        story_text = ("")

        choices = [
            "Enter tower",
            "Go back"
        ]
        selected_option = display_menu(story_text, choices)

        if selected_option == 0:
            tower_path(character, previous_function)
        elif selected_option == 1:
            look_libarary(character, previous_function)
    else:
        missing_sigils = required_sigils - player_sigils
        print("\nThe door remains shut. You need the following Sigils to proceed:")
        for sigil in missing_sigils:
            print(f"- {sigil}")
    look_libarary(character, previous_function)
    

# dungeon path
def dungeon_path(character, previous_function):
    story_text = ("You descend into the dungeon, the air growing colder and damper with each step."
                  "The stone walls are slick, and the faint sound of dripping water echoes through the darkness."
                  "The dim light from above fades, leaving only a faint flicker from torches mounted on the walls.")

    choices = [
        "Look around the room",
        "Go back to the entryway",
        "Look in inventory",
        "Display character"
        ]
    selected_option = display_menu(story_text, choices) 
    
    if selected_option == 0:
        look_dungen(character, lambda: look_dungeon(character, previous_function))
    elif selected_option == 1:
        entryway_path(character, previous_function)
    elif selected_option == 2:
        inventory_menu(lambda: look_dungeon(character, previous_function))
    elif selected_option == 3:
        display_character(character, lambda: look_dungeon(character, previous_function))
    else:
        print("\nSomething went wrong!")

# look around dungeon
def look_dungen(character, previous_function):
    story_text = ("You take a closer look at your surroundings."
                  "The dungeon is oppressive, its cold stone walls bearing the weight of forgotten history."
                  "Iron-barred cells line the far walls, some with broken doors, others sealed shut by rust."
                  "Scattered across the floor are remnants of discarded tools and old, tattered cloths."
                  "In the far corner, a small weapon rack leans against the wall, its contents long abandoned "
                  "and rusted."
                  "Your eyes fall on a small chest in the center of the room, half-buried beneath rubble.")
    choices = [
        "Investigate the cells",
        "Examine the weapon rack",
        "Examine the chest",
        "Go back to the entryway",
        "Look in inventory",
        "Display character"
        ]
    selected_option = display_menu(story_text, choices)

    if selected_option == 0:
        examine_cells_dungen(character, lambda: look_dungeon(character, previous_function))
    elif selected_option == 1:
        examine_rack_dungen(character, lambda: look_dungeon(character, previous_function))
    elif selected_option == 2:
        examine_chest_dungen(character, lambda: look_dungeon(character, previous_function))
    elif selected_option == 3:
        entryway_path(character, previous_function)
    elif selected_option == 4:
        inventory_menu(lambda: look_dungeon(character, previous_function))
    elif selected_option == 5:
        display_character(character, lambda: look_dungeon(character, previous_function))
    else:
        print("\nSomething went wrong!")

def examine_cells_dungen(character, previous_function):
    
    print("\n".join(textwrap.wrap("You walk past the rows of cells, peering inside.")))
    if "Moon Sigil" not in inventory:  # Check if the moon has already been taken
        print("\n In one of them, beneath a pile of straw, you find a Moon Sigil."
              "Its metallic surface feels warm to the touch.")
        pick_up = input("Do you want to pick it up? (yes/no): ").lower()
        if pick_up == "yes":
            add_item("Moon Sigil", "")
    else:
        print("\n You already took the Moon Sigil.")
        time.sleep(2)
    look_dungen(character, previous_function)

def examine_rack_dungen(character, previous_function):
    story_text = ("You approach the weapon rack near the wall, half-collapsed under years of neglect."
                  "Several rusted swords, maces, and shields hang in a disorganized manner, coated in grime and decay.")
    print("\n".join(textwrap.wrap(story_text, width=70)))
    if "Weapon" not in inventory:  # Check if the weapon has already been taken
        print('\n The dagger is odd, the blade thin but etched with intricate runes that pulse with a faint '
              'magical glow. It feels unnaturally light in your hand, as though it has been designed to be '
              'wielded by someone of your stature.'
              'A closer inspection reveals the words "Blade of the Forgotten" etched into the metal.')
        pick_up = input("Do you want to pick it up? (yes/no): ").lower()
        if pick_up == "yes":
            add_item("Weapon", '"Blade of the Forgotten" is etched into the metal')
    else:
        print("\n You already took the Dagger.")
        time.sleep(2)
    look_dungen(character, previous_function)

def examine_chest_dungen(character, previous_function):
    print("\n".join(textwrap.wrap("The chest sits before you, its wood darkened and worn by time."
                  "You see the number 3: 8 is scratched into the side of the chest.")))
    if "Protective Gear" not in inventory:
        print("\n".join(textwrap.wrap('The lock is old and rusted, but as you study it, you notice something.'
              'The lock has four rotating dials, each etched with glowing runes that shift and shimmer.'
              'An inscription glows faintly along the top of the chest: '
              '"The numbers are hidden in the echoes of those who came before. Gather them, align them, and '
              'claim your prize."'
             )))
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            num3 = int(input("Enter the third number: "))
            num4 = int(input("Enter the fourth number: "))
        
            if [num1, num2, num3, num4] == [6, 3, 8, 3]:
                print("The lock clicks open! You have successfully unlocked the chest.")
                print("Inside, you find: Protective Gear!")
                pick_up = input("Do you want to pick it up? (yes/no): ").lower()
                if pick_up == "yes":
                    add_item("Protective Gear", "")
                else:
                    print("\nYou decided not to take the Protective Gear.")
            else:
                print("The combination is incorrect. The lock remains shut.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")
    else:
        "The chest lays open and emptey"
    look_dungen(character, previous_function)

def tower_path(character, previous_function):
    print("\n" + "\n".join(textwrap.wrap("You ascend the winding stairs of the tower, the creaking of each step echoing in the oppressive silence. "
        "The air grows colder with every step, and an overwhelming sense of purpose wells up within you. "
        "Whatever you've been searching for, you know it's near. At the top of the stairs, a massive, ornately carved door looms before you. "
        "The door is etched with runes that pulse faintly, as if alive, and at its center is an emblem that mirrors the sigils you've found. "
        "You press your hand to the door, and it swings open with a low groan, revealing the chamber beyond.")))
    story_text = ("The chamber is vast, its walls lined with decayed tapestries and towering shelves filled with crumbling tomes. "
                "In the center of the room stands a pedestal, bathed in an otherworldly glow. On the pedestal rests an object that seems to defy description—a swirling, pulsating artifact that draws your gaze like a moth to a flame. "
                "But between you and the artifact stands a figure cloaked in shadow, its form shifting and unnatural. "
                "The figure speaks, its voice a low growl that seems to echo from the depths of the void: "
                "'You’ve come far, but your journey ends here. The artifact is mine, and I will not allow you to take it.'")
    choices = [
        "Enter battle"
        ]
    selected_option = display_menu(story_text, choices)

    if selected_option == 0:
        combat_final_boss(character, previous_function)



def combat_final_boss(character, previous_function):
    print("\n" + "\n".join(textwrap.wrap(
        "You ascend the winding staircase to the tower's apex. The room is shrouded in shadows, but an ominous figure steps forward. "
        "The air feels heavy with power and malice. 'You dare challenge me for the artifact?' the final boss hisses, "
        "its form shifting between monstrous and human-like. Prepare yourself for the ultimate battle!"
    )))

    # Initialize boss and minions in a unified list
    enemies = [
        {"name": "Final Boss", "health": 100, "attack": (15, 25), "phase": 1}
    ]

    character["health"]
    base_damage = 5  # Base player damage
    weapon_bonus = 15 if "Weapon" in inventory else 0

    # Check if the owl is an ally
    owl_ally = character.get("has_owl_ally", False)

    # Combat loop
    while character["health"] > 0 and any(enemy["health"] > 0 for enemy in enemies):
        # Display player's health and enemies' statuses
        print(f'\nYour health: {character["health"]}')
        for i, enemy in enumerate(enemies):
            status = f"{enemy['health']} HP" if enemy["health"] > 0 else "Defeated"
            phase = f" (Phase {enemy['phase']})" if "phase" in enemy else ""
            print(f"{i + 1}. {enemy['name']}{phase}: {status}")

        # Player's turn
        print("\nChoose your action:")
        print("1. Attack an enemy")
        print("2. Use an item from inventory")


        choice = input("\nEnter the number of your choice: ")

        if choice == "1":
            # Attack an enemy
            target_index = None
            while target_index is None:
                try:
                    target_index = int(input("Choose an enemy to attack (enter the number): ")) - 1
                    if not (0 <= target_index < len(enemies)) or enemies[target_index]["health"] <= 0:
                        print("Invalid choice. Choose a living enemy.")
                        target_index = None
                except ValueError:
                    print("Invalid input. Enter a number.")
            damage = random.randint(base_damage, base_damage + 5) + weapon_bonus
            enemies[target_index]["health"] -= damage
            print(f"You attack {enemies[target_index]['name']} for {damage} damage!")
            check_FBoss_heath(character, previous_function, enemies)

        elif choice == "2":
            # Use an item
            inventory_menu(character, lambda: None, combat_mode=True, boss_combat=True, enemies=enemies)
            check_FBoss_heath(character, previous_function, enemies)

        else:
            print("Invalid action. Choose a valid option.")

        # Owl's help if it's an ally
        if owl_ally:
            print("\nThe owl swoops down to assist you in battle!")
            owl_damage = random.randint(15, 25)
            target_index = random.choice([i for i in range(len(enemies)) if enemies[i]["health"] > 0])
            enemies[target_index]["health"] -= owl_damage
            print(f"The owl attacks {enemies[target_index]['name']} for {owl_damage} damage!")
            check_FBoss_heath(character, previous_function, enemies)

        # Check if boss advances phases
        boss = enemies[0]  # Assume the boss is always the first enemy
        if boss["health"] <= 50 and boss["phase"] == 1:
            boss["phase"] = 2
            print("\nThe boss snarls and summons shadowy figures to aid it!")
            enemies.extend([
                {"name": "Shadow Minion", "health": 20, "attack": (5, 10)},
                {"name": "Shadow Minion", "health": 20, "attack": (5, 10)}
            ])
        elif boss["health"] <= 20 and boss["phase"] == 2:
            boss["phase"] = 3
            print("\nThe boss grows desperate and unleashes a wave of chaos, testing your sanity!")
            character["sanity"] -= 20
            check_status(character)

        # Enemies' turn
        for enemy in enemies:
            if enemy["health"] > 0:
                damage = random.randint(*enemy["attack"])
                character["health"] -= damage
                print(f"{enemy['name']} attacks you for {damage} damage!")

        # Check player's status
        character["health"] 
        check_status(character)

    # End of combat
    if enemies[0]["health"] <= 0:
        print("\n" + "\n".join(textwrap.wrap(
            "With a final strike, the shadow figure lets out an ear-piercing wail and collapses into a pool of darkness, which evaporates into the air. "
            "The chamber brightens slightly, and the oppressive weight in the air begins to lift. "
            "You step forward toward the artifact, your heart pounding in your chest."
        )))
        ending_path(character)
    else:
        print("\n" + "\n".join(textwrap.wrap(
            "The shadow figure overpowers you, its form enveloping you completely. "
            "As your vision fades, the last thing you see is the artifact pulsing with an eerie, mocking glow."
        )))

def check_FBoss_heath(character, previous_function, enemies):
    # Check if all enemies are defeated
    for i, enemy in enumerate(enemies):
        if enemy["health"] <= 0:
            if enemy["name"] == "Final Boss":
                print("\n" + "\n".join(textwrap.wrap(
                    "With a final strike, the shadow figure lets out an ear-piercing wail and collapses into a pool of darkness, which evaporates into the air. "
                    "The chamber brightens slightly, and the oppressive weight in the air begins to lift. "
                    "You step forward toward the artifact, your heart pounding in your chest."
                )))
                ending_path(character)
            else:
                print(f"\nThe {enemy['name']} has been defeated and crumbles into nothingness!")
                # Remove defeated minions from the list
                enemies[i]["health"] = 0  # Ensure health is 0 for defeated enemies

    # Check if there are still active enemies
    if all(enemy["health"] <= 0 for enemy in enemies):
        print("\nAll enemies have been defeated! The room falls silent.")
        ending_path(character)



def ending_path(character):
    print("\n" + "\n".join(textwrap.wrap("The artifact radiates a strange warmth as you approach. Its surface seems to shift and swirl, and as you reach out to touch it, visions flood your mind. "
        "The house, the sigils, the battles—all of it was leading to this moment. You feel a surge of power coursing through you, but also a creeping unease. "
        "You grasp the artifact, and your fate is sealed.")))
    if character["sanity"] >= 50:  # High sanity ending
        print("\n" + "\n".join(textwrap.wrap(
            "As the artifact's power flows through you, clarity washes over your mind. "
            "Memories of your life outside the house return, and you suddenly remember who you are and why you came here. "
            "The yearning that drove you fades, replaced by a sense of purpose. "
            "You find your way out of the house, the artifact no longer a mystery but a tool to guide you home."
        )))
    else:  # Low sanity ending
        print("\n" + "\n".join(textwrap.wrap(
            "As the artifact's power floods your mind, your thoughts fragment and spiral into chaos. "
            "The yearning is all that remains, consuming you entirely. "
            "You feel yourself drawn deeper into the house, becoming one with its darkness. "
            "You have become the new guardian of the artifact, your identity lost to its power."
        )))
    print("\nTHE END")
    exit()  # End the game

    

# Main function
def main():
    print("Game is starting....")
    print()
    char1 = create_character()
    print("---"*7)
    story_text = (
        "You wake up in an unfamiliar place. Getting to your feet you seem to be in an entryway of an "
        "old house. With paint peeling from the walls and the floorboard warped. You think back to "
        "how you got here. Remembering nothing except for a feeling of yearning for something."
        "You look around the decrepit house and know that whatever you want is in this house."
        "There are three doors ahead of you and one behind.")

    choices = [
        "Go to the kitchen",
        "Go to the library",
        "Go to the dungeon",
        "Go to the front door",
        "Look around the entryway",
        "Look in inventory",
        "Display character"
    ]

    # Display the menu and handle the choice
    selected_option = display_menu(story_text, choices)

    if selected_option == 0:
        kitchen_path(char1, lambda: main())
    elif selected_option == 1:
        library_path(char1, lambda: main())
    elif selected_option == 2:
        dungeon_path(char1, lambda: main())
    elif selected_option == 3:
        front_door_path(char1, lambda: main())
    elif selected_option == 4:
        look_entryway(char1, lambda: main())
    elif selected_option == 5:
        inventory_menu(lambda: main())
    elif selected_option == 6:
        display_character(char1, lambda: main())
    else:
        raise GameError("Invalid menu selection")

    
    
if __name__ == "__main__":
    main()


