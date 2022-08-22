import random

ai = random.randint(1,10)
tries = 1
pick = 0
while pick != ai:
    pick = int(input("Enter number between 1 and 10 : "))
    if pick > ai:
        print("lower     tries = " + str(tries))
        tries += 1
    else:
        print("higher    tries = " + str(tries))
        tries += 1
print("GAME OVER")