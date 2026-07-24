# Rock, paper and scissors game
import random

moves = ("rock", "paper", "scissors")
player_choice = None
device_choice = random.choice(moves)
running = True

while running:
    player_choice = None
    device_choice = random.choice(moves)


    while player_choice not in moves:
        player_choice = input("Enter your move (rock, paper, scissors) : ")
    
    print(f"Player's choice : {player_choice}")
    print(f"Computer's choice : {device_choice}")
    
    if player_choice == device_choice:
        print("TIED")
    elif player_choice == "rock" and device_choice == "scissors":
        print("Player wins!")
    elif player_choice == "paper" and device_choice == "rock":
        print("Player wins!")
    elif player_choice == "scissors" and device_choice == "paper":
        print("Player wins!")
    else:
        print("Computer wins!")


    play_again = input("Do you want to play again (y/n) : ")
    if play_again == "n":
        running == False
        
