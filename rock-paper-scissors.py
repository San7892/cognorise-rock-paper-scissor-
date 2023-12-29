import random

def get_user_choice():
    choice = input("Choose rock, paper, or scissors: ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()
    return choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def play_again():
    choice = input("Would you like to play again? (yes/no): ").lower()
    while choice not in ['yes', 'no']:
        choice = input("Invalid choice. Please choose yes or no: ").lower()
    return choice == 'yes'

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}. The computer chose {computer_choice}.")
    print(determine_winner(user_choice, computer_choice))
    if not play_again():
        break

user_score = 0
computer_score = 0

while True:
    # ... (previous code)
    result = determine_winner(user_choice, computer_choice)
    print(result)

    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1

    print(f"User score: {user_score}. Computer score: {computer_score}.")

    if not play_again():
        break
