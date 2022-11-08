import random

choices = ["Rock", "Paper", "Cissors"]

computers_points = 0
user_poits = 0

print("Best of 5 Games")

while True:
    print()
    user_guess = input("Choose [r] for Rock, [p] for paper, [s] for cissors: ").lower()
    computer_guess = random.choice(choices)

    if user_guess == "r":
        if computer_guess == "Rock":
            print("User Guess: Rock")
            print("Computer Guess: Rock")
            print("It's a Draw")
            print(f"Result is {user_poits}:{computers_points}")
        elif computer_guess == "Paper":
            print("User Guess: Rock")
            print("Computer Guess: Paper")
            print("Computer beat this turn")
            computers_points +=1
            print(f"Result is {user_poits}:{computers_points}")
        elif computer_guess == "Cissors":
            print("User Guess: Rock")
            print("Computer Guess: Cissors")
            print("User beat this turn")
            user_poits +=1
            print(f"Result is {user_poits}:{computers_points}")
    elif user_guess == "p":
        if computer_guess == "Rock":
            print("User Guess: Paper")
            print("Computer Guess: Rock")
            print("User beat this turn")
            user_poits += 1
            print(f"Result is {user_poits}:{computers_points}")
        elif computer_guess == "Paper":
            print("User Guess: Paper")
            print("Computer Guess: Paper")
            print("It's Draw")
            print(f"Result is {user_poits}:{computers_points}")
        elif computer_guess == "Cissors":
            print("User Guess: Paper")
            print("Computer Guess: Cissors")
            print("Computer beat this turn")
            computers_points += 1
            print(f"Result is {user_poits}:{computers_points}")
    elif user_guess == "s":
        if computer_guess == "Rock":
            print("User Guess: Cissors")
            print("Computer Guess: Rock")
            print("Computer beat this turn")
            computers_points += 1
            print(f"Result is {user_poits}:{computers_points}")
        elif computer_guess == "Paper":
            print("User Guess: Cissors")
            print("Computer Guess: Paper")
            print("User beat this turn")
            user_poits += 1
            print(f"Result is {user_poits}:{computers_points}")
        elif computer_guess == "Cissors":
            print("User Guess: Cissors")
            print("Computer Guess: Cissors")
            print("It's a Draw")
            print(f"Result is {user_poits}:{computers_points}")
    else:
        print("Invalid Guess! Try again!")
        print(f"The result is still {user_poits}:{computers_points}")
        continue

    if computers_points == 3:
        print("Computer Win")
        break
    elif user_poits == 3:
        print("User Win")
        break