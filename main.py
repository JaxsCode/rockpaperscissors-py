# THIS ROCK PAPER AND SCISSORS GAME IS MADE By github.com/Jaxscode


import random #Importing random module for selecting the choice of computer randomly.
items = ['ROCK','PAPER','SCISSORS'] #Items for computer to choose
computer_choice = random.choice(items) # Variable for computer to choose

def logic(computer_choice):
        # Prompt the player to enter their choice
    while True:
        player_choice = input("ENTER YOUR CHOICE [ROCK,PAPERS,SCISSORS]: ")
        player_choice = player_choice.upper()
        if player_choice not in items:
            print("CHOOSE VALID ITEM!")
        else:
            break

    
    # Print the computer's choice
    print(computer_choice)

    #CONDITIONS FOR DECIDING THE WINNER OF THE GAME
    # TIE IF BOTH PLAYER AND COMPUTER CHOOSE SAME ITEM
    # SCISSORS WIN OVER PAPER
    # PAPER WINS OVER ROCK
    # ROCK WINS OVER SCISSORS

    if player_choice == computer_choice:
        print("TIE")
    elif player_choice == "ROCK" and computer_choice == "SCISSORS":
        print("ROCK BREAKS SCISSORS! PLAYER WINS")
    elif player_choice == "SCISSORS" and computer_choice == "PAPER":
        print("SCISSORS CUTS PAPER! PLAYER WINS")
    elif player_choice == "PAPER" and computer_choice == "ROCK":
        print("PAPER BLOCKS ROCK! PLAYER WINS")
    elif player_choice == "PAPER" and computer_choice == "SCISSORS":
        print("SCISSORS CUT PAPER! COMPUTER WINS")
    elif player_choice == "SCISSORS"and computer_choice =="ROCK":
        print("ROCK BREAKS SCISSORS! COMPUTER WINS")
    else:
        print("PAPER BLOCKS SCISSOR! COMPUTER WINS")

print("ROCK PAPER SCISSORS!")       # Starting of Program
while True: #This while loop runs infinitely till player does not tell to quit the game.

    choice = int(input("ENTER [0] TO QUIT OR [1] TO PLAY WITH COMPUTER: "))

    if choice == 0:
        break
    elif choice == 1:
        logic(computer_choice)
    else:
        print("CHOOSE VALID OPTION!")
