import random
from time import sleep


def countdown():
    print(3)
    sleep(0.6)
    print(2)
    sleep(0.6)
    print(1)
    sleep(0.6)


pieces = ["rock", "paper", "scissors"]
print("Play?\n")
play = input("[Y]\n[N]\n").upper()
sleep(0.5)
if play != "Y":
    print('exit')
while play == "Y":
    playerChoice = input("rock paper scissors\n").lower()
    gameChoice = random.choice(pieces)
    if playerChoice == gameChoice:
        countdown()
        print(playerChoice, ' x ', gameChoice, '\nDraw!')

    elif playerChoice == 'rock' and gameChoice == 'scissors':
        countdown()
        print(playerChoice, ' x ', gameChoice, '\nYou Win!')

    elif playerChoice == 'rock' and gameChoice == 'paper':
        countdown()
        print(playerChoice, ' x ', gameChoice, '\nYou Lose!')

    elif playerChoice == 'scissors' and gameChoice == 'paper':
        countdown()
        print(playerChoice, ' x ', gameChoice, '\nYou Win!')

    elif playerChoice == 'scissors' and gameChoice == 'rock':
        countdown()
        print(playerChoice, ' x ', gameChoice, '\nYou Lose!')

    elif playerChoice == 'paper' and gameChoice == 'rock':
        countdown()
        print(playerChoice, ' x ', gameChoice, '\nYou Win!')

    elif playerChoice == 'paper' and gameChoice == 'scissors':
        countdown()
        print(playerChoice, ' x ', gameChoice, '\nYou Lose!')

    else:
        print('Your choice was Invalid!')

    print("Play again?\n")
    play = input("[Y]\n[N]\n").capitalize()