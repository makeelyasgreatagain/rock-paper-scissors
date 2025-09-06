import random

def play():
    choices = ["rock", "paper", "scissors"]
    print("\n--- It's your turn. Choose from this menu (1-3): ---")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    user_choice = input("Which one do you choose? (enter the number)  ")

    if user_choice == "1":
        user = "rock"
    elif user_choice == "2":
        user = "paper"
    elif user_choice == "3":
        user = "scissors"
    else:
        print("Invalid selection.")
    
    computer = random.choice(choices)
    print(f"Computer choice: {computer}")
    
    if user == computer:
        print("It's a tie!")
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        print("You win!")
    else:
        print("You lose!")


while (True):
    play()
    again = input("Play again? (y/n)")
    if again != "y":
        print("goodbye!")
        break
