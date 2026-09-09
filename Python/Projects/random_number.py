import random
Target = random.randint(1,100)

while True:
    userChoice = input("guess the target or quit(Q): ")
    if (userChoice == "Q"):
        break
    
    userChoice = int(userChoice)
    if (userChoice == Target):
        print("congratulations you guess the correct number")
        break
    elif (userChoice< Target):
        print("your number is small then target guess once again: ")
    else:
        print("your number is bigger then target guess once again: ")

print("---GAME OVER ---")
