# rock_paper_scissors.py

import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

print("=== ROCK, PAPER, SCISSORS ===")

while True:
    user_choice = input("Choose (rock/paper/scissors or q to quit): ").lower()

    if user_choice == 'q':
        print("Thanks for playing!")
        break

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Try again.")
        continue

    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = get_winner(user_choice, computer_choice)
    print("Result:", result)
