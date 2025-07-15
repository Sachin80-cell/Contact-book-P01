import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

user_score = 0
computer_score = 0

while True:
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid input! Try again.")
        continue

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

    if "You win" in result:
        user_score += 1
    elif "Computer wins" in result:
        computer_score += 1

    print(f"Score => You: {user_score} | Computer: {computer_score}")
    
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != 'yes':
        break