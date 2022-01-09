#Rock, paper, scissors game in Python
from random import randint
choices=["rock", "paper", "scissors"]
playGame=True

while playGame == True:
    computer=choices[randint(0,2)]
    player= input("rock, paper, or scissors?").lower()

    if player ==computer:
        print("It's a tie!")

    elif player=="rock":
        if computer =="scissors":
            print("You win! Rock smashes scissors.")
        else:
            print("You Lose!Paper covers rock.")

    elif player=="paper":
        if computer =="Rock":
            print("You win! Paper covers Rock.")
        else:
            print("You Lose!Scissors cut paper.")

    elif player=="scissors":
        if computer =="Paper":
            print("You win! scissors cut paper.")
        else:
            print("You Lose!Rock smashes scissors.")

    else:
            print("Not a valid play. Try again")
            continue

    keepPlaying=input("Play again?").lower()
    if keepPlaying=="yes":
        playGame=True
        print("Lets Play!")
        
    elif keepPlaying=="no":
        playGame=False
        print("Thanks for Playing!") 
else:
        print("Not valid. Please type 'yes' or'no'.")


        
        
