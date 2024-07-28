import random

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"

def clear_screen():
    print(CLEAR, end="")
    print(CLEAR_AND_RETURN, end="")

def colored_text(text, color_code):
    return f"{color_code}{text}{RESET}"

def game_over(message):
    print(colored_text(message, RED))
    print("Game Over!")
    exit()

def start_adventure():
    health = 100
    inventory = []
    
    name = input("Enter your name: ")
    print(f"Welcome {BOLD}{name}{RESET} to this {GREEN}ADVENTURE{RESET}!!")

    answer = input(
        "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

    if answer == "left":
        answer = input(
            "You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ").lower()

        if answer == "swim":
            game_over("You swam across and were eaten by an alligator.")
        elif answer == "walk":
            print("You walked for many miles and found a village.")
            if "key" in inventory:
                print("You used the key to open a chest and found gold. You WIN!")
            else:
                print("You found a key on the ground.")
                inventory.append("key")
        else:
            game_over("Not a valid option. You lose.")
    elif answer == "right":
        answer = input(
            "You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()

        if answer == "back":
            game_over("You go back and lose.")
        elif answer == "cross":
            answer = input(
                "You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ").lower()

            if answer == "yes":
                print("You talk to the stranger and they give you a potion. You gained 20 HP.")
                health += 20
            elif answer == "no":
                game_over("You ignore the stranger and they are offended and you lose.")
            else:
                game_over("Not a valid option. You lose.")
        else:
            game_over("Not a valid option. You lose.")
    else:
        game_over("Not a valid option. You lose.")

    print("End of the adventure. Thank you for playing!")

clear_screen()
start_adventure()

#more to complete
