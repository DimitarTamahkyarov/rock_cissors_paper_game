import random
from colorama import Fore

user_poits = 0
computers_points = 0

print()
print('This is the game "Rock, Scissors, Paper". Enjoy!')
user_name = input("What is your name? ")
print(f"OK, {user_name}. The game is up to 3 wins.")

while True:
    print()
    user_choice = input(Fore.RESET + "Choose [r] for Rock, [s] for Scissors, [p] for Paper: ").lower()
    if user_choice == "r":
        user_choice = "Rock"
    elif user_choice == "s":
        user_choice = "Scissors"
    elif user_choice == "p":
        user_choice = "Paper"

    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    print(f"({user_name}) {user_choice} : {computer_choice} (Computer)")

    if user_choice == computer_choice:
        print(Fore.LIGHTYELLOW_EX + "It's Draw")
    elif user_choice == "Rock":
        if computer_choice == "Paper":
            print(Fore.RED + "Computer won a point")
            computers_points +=1
        elif computer_choice == "Scissors":
            print(Fore.GREEN + f"{user_name} won a point")
            user_poits += 1
    elif user_choice == "Paper":
        if computer_choice == "Rock":
            print(Fore.GREEN + f"{user_name} won a point")
            user_poits += 1
        elif computer_choice == "Scissors":
            print(Fore.RED + "Computer won a point")
            computers_points += 1
    elif user_choice == "Scissors":
        if computer_choice == "Rock":
            print(Fore.RED + "Computer won a point")
            computers_points += 1
        elif computer_choice == "Paper":
            print(Fore.GREEN + f"{user_name} won a point")
            user_poits += 1
    else:
        print("Invalid Guess! Try again!")
        print(f"The result is still {user_poits}:{computers_points}")
        continue

    print(f"({user_name}) {user_poits}:{computers_points} (Computer)")

    if computers_points == 3:
        print(Fore.RESET + "Computer Win The Game")
        print()
        command = input("Do you wonna another game? [yes] or [no] -> ")
        if command == "yes":
            user_poits = 0
            computers_points = 0
        elif command == "no":
            break
        else:
            print('I will accept this for "no" ')
            break
    elif user_poits == 3:
        print(f"{user_name} Win The Game")
        print()
        command = input("Do you wonna another game? [yes] or [no] -> ")
        if command == "yes":
            user_poits = 0
            computers_points = 0
        elif command == "no":
            break
        else:
            print('I will accept this for "no" ')
            break


