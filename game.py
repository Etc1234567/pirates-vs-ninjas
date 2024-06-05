from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()

print("Welcome to Pirates vs Ninjas! Choose your character: \n")

numPlayer= 0

while numPlayer == 0:
    numPlayers = input("How many players? 1 or 2: \n")
    if (numPlayers == 1):
        print("You have one player. Time to create your character! \n")
    
    elif (numPlayers == 2):
        print("Multiplayer: Time to create your characters! \n")

    else:
        print("Invalid number of players.\n")

character_type = ""
character_name = ""

while character_type != "p" and character_type != "n":
    character_type = input("Press 'p' for pirate and 'n' for ninja: \n")
    if (character_type == "p"):
        print(f"You are playing as a pirate, arrr!\n")

    elif (character_type == "n"):
        print(f"You are playing as a ninja. Shhh!\n")

    else: 
        print ("Not a valid choice. Try again!\n")

while character_name == "":
    if (character_type == "p"):
        character_name = input("What is your pirate's name?: \n")
        print(f"Your pirate's name is {character_name}\n")
        character = Pirate(character_name)
    
    else:
        character_name = input("What is your ninja's name?: \n")
        print(f"Your ninja's name is {character_name}\n")
        character = Ninja(character_name)

character.show_stats()

# Two player system:


# Maybe Randomize character

# Alternate turns -- LOOP
while character.health > 0:
    pass

