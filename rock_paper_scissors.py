import random

print("Welcome to my computer quiz")

player_wins = 0
computer_wins = 0

choices = ["rock", "paper", "scissors"]

while True:
    player_input = input("Insert Rock/Paper/Scissors or Q to quit: ").lower()
    if player_input == "q":
        break

    if player_input not in choices:
        continue

    random_number = random.randint(0,2)

    computer_chose = choices[random_number]
    print("Computer picked", computer_chose + ".")

    if player_input == "rock" and computer_chose == "scissors":
        print("You won")
        player_wins += 1
    
    elif player_input == "paper" and computer_chose == "rock":
        print("You won")
        player_wins += 1

    elif player_input == "scissors" and computer_chose == "paper":
        print("You won")
        player_wins += 1

    else:
        print("You lost!")
        computer_wins += 1 

print("You won", player_wins, "times!")
print("The computer won", computer_wins, "times!")
print("Thank you for joining the game. Goodbye!")