import random

def play():
    choices = ["rock", "paper", "scissors"]
    user = input("Choose rock, paper, or scissors:  ").lower()
    if user not in choices:
        print("Invalid choice. Try again")
        return
    
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
