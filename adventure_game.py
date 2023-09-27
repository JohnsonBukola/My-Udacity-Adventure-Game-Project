import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro(weapon, obstacle):
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.\n")
    print_pause("Rumor has it that a " + obstacle + " is somewhere around here, and has been terrifying the nearby village.\n")
    print_pause("In front of you is a house.\n")
    print_pause("To your right is a dark cave.\n")
    print_pause("In your hand you hold your trusty (but not very effective) dagger.\n")

    
def fight(weapon, obstacle):
    # Things that happen when the player fights
    if "sword" not in weapon:
        print_pause("You do your best...\n")
        print_pause("but your dagger is no match for the " + obstacle + ".\n")
        print_pause("You have been defeated!")
    else:
        print_pause("As the " + obstacle + " moves to attack, you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.\n")
        print_pause("But the " + obstacle + " takes one look at your shiny new toy and runs away!\n")
        print_pause("You have rid the town of the " + obstacle + ". You are victorious!")
    play_again()

    
def cave(weapon, obstacle):
    # Things that happen to the player goes in the cave
     if "sword" in weapon:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all")
        print_pause("the good stuff. It's just an empty cave now.")
        print_pause("You walk back to the field.")
     else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a "
                    "rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take "
                    "the sword with you.")
        weapon.append("sword")
     field(weapon, obstacle)
    
     
def field(weapon, obstacle):
    # Things that happen when the player runs back to the field
     if "sword" not in weapon:
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the " + obstacle + ".")
        print_pause("You have been defeated!")         
        play_again()
     else:
           print_pause("You run back into the field. Luckily, you don't seem to have been followed.")
           get_started(weapon, obstacle)
   

def house(weapon, obstacle):
    # Things that happen to the player in the house
    if "sword" not in weapon:
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock when the door opens and out steps a " + obstacle + ".\n"
                    "Eep! This is the " + obstacle + "'s house!\n")
        print_pause("The " + obstacle + " attacks you!\n"
                    "You feel a bit under-prepared for this, what with only having a tiny dagger.")
        valid_input(weapon, obstacle)
    else:
        print_pause("As the " + obstacle + " moves to attack, "
                    "you unsheath your new sword.")
        print_pause("\nThe Sword of Ogoroth shines brightly in "
                    "your hand as you brace yourself for the "
                    "attack.")
        print_pause("But the " + obstacle + "takes one look at "
                    "your shiny new toy and runs away!")
        print_pause("You have rid the town of the " + obstacle + ". You are victorious!")
    play_again()


def valid_input(weapon, obstacle):
    answer = input("Would you like to (1) fight or (2) run away?")
    if answer == '1':
        fight(weapon, obstacle)
    else:# response == '2':
        field(weapon, obstacle)


def get_started(weapon, obstacle):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    response = input("(Please enter 1 or 2.)")
    if response == '1':
        house(weapon, obstacle)
    else:# response == '2':
        cave(weapon, obstacle)


def play_again():
    print_pause("Would you like to play again? ")
    decision = input("Please say 'yes' or 'no'.\n")
    if decision == "no":
        print_pause("Thanks for playing! See you next time.")
        exit(0)
    else:# response == "yes":
        print_pause("Excellent. Restarting the game.")
        play_game()
    

def play_game():
    weapon = []
    obstacle = random.choice(["wicked fairie", "pirate", "dragon", "troll", "gorgon"])
    intro(weapon, obstacle)
    get_started(weapon, obstacle)
    valid_input(weapon, obstacle)
    

play_game()