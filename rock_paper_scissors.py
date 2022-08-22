import random

print("**************************ROCK PAPER SCISSORS******************************\n \n")

ai = random.randint(1,3)
count = 0
player = 0
comp = 0
while count < 6:
    choice = int(input("Enter 1 for Rock, 2 for Paper, or 3 for Scissors :"))
    ai = random.randint(1,3)
    if choice == 1:
        if ai == 1:
            print("Player : " + str(player) + "       |       " + "Computer : " + str(comp))
            print("Player : Rock       |          Computer : Rock")
            print("TIE")
            count += 1
        elif ai == 2:
            print("Player : " + str(player) + "       |       " + "Computer : " + str(comp))
            print("Player : Rock       |          Computer : Paper")
            print("Paper beats Rock, You Lose!")
            count += 1
            comp += 1
        else:
            print("Player : " + str(player) + "       |       " + "Computer : " + str(comp))
            print("Player : Rock       |          Computer : Scissors")
            print("Rock beats Scissors, you Win!")
            count += 1
            player += 1
    elif choice == 2:
        if ai == 1:
            print("Player : " + str(player) + "       |       " + "Computer : " + str(comp))
            print("Player : Paper       |          Computer : Rock")
            print("Paper beats Rock, You Win!")
            count += 1
            player += 1
        elif ai == 2:
            print("Player : " + str(player) + "       |       " + "Computer : " + str(comp))
            print("Player : Paper       |          Computer : Paper")
            print("TIE!")
            count += 1
        else:
            print("Player : " + str(player) + "       |       " + "Computer : " + str(comp))
            print("Player : Paper       |          Computer : Scissors")
            print("Scissors beats Paper, you Lose!")
            count += 1
            comp += 1
    elif choice == 3:
        if ai == 1:
            print("Player : " + str(player) + "      |       " + "Computer : " + str(comp))
            print("Player : Scissors       |          Computer : Rock")
            print("Rock beats Scissors, you Lose")
            count += 1
            comp += 1
        elif ai == 2:
            print("Player : " + str(player) + "       |       " + "Computer : " + str(comp))
            print("Player : Scissors       |          Computer : Paper")
            print("Scissors beats Paper, you Win")
            count += 1
            player += 1
        else:
            print("Player : " + str(player) + "       |       " + "Computer : " + str(comp))
            print("Player : Scissors       |          Computer : Scissors")
            print("Tie")
            count += 1