import random

computers_points = 0
user_poits = 0

print('This is the game "Rock, Scissors, Paper". Enjoy!')
user_name = input("What is your name? ")
print(f"OK, {user_name}. The game is up to 3 wins.")
while True:
    print()
    user_choice = input("Choose [r] for Rock, [s] for Scissors, [p] for Paper: ").lower()
    if user_choice == "r":
        user_choice = "Rock"
    elif user_choice == "s":
        user_choice = "Scissors"
    elif user_choice == "p":
        user_choice = "Paper"

    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    print(f"{user_name} -> {user_choice} : {computer_choice} <- Computer")
    print()

    if user_choice == "Rock":
        if computer_choice == "Rock":
            print("Draw!")
        elif computer_choice == "Paper":
            print("Computer won a point")
            computers_points +=1
        elif computer_choice == "Scissors":
            print(f"{user_name} won a point")
            user_poits += 1
    elif user_choice == "Paper":
        if computer_choice == "Rock":
            print(f"{user_name} won a point")
            user_poits += 1
        elif computer_choice == "Paper":
            print("It's Draw")
        elif computer_choice == "Scissors":
            print("Computer won a point")
            computers_points += 1
    elif user_choice == "Scissors":
        if computer_choice == "Rock":
            print("Computer won a point")
            computers_points += 1
        elif computer_choice == "Paper":
            print(f"{user_name} won a point")
            user_poits += 1
        elif computer_choice == "Scissors":
            print("It's a Draw")
    else:
        print("Invalid Guess! Try again!")
        print(f"The result is still {user_poits}:{computers_points}")
        continue

    print(f"({user_name}) {user_poits}:{computers_points} (Computer)")

    if computers_points == 3:
        print("Computer Win")
        print()
        command = input("Do you wonna another game? [yes] or [no]")
        if command == "yes":
            user_poits = 0
            computers_points = 0
        elif command == "no":
            break
        else:
            print('I will accept this for "no" ')
            break
    elif user_poits == 3:
        print("User Win")
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


