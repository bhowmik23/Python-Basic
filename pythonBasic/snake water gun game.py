import random
n=1
draw =0
userWin = 0
comWin= 0

while(n<=10):
    n+=1
    list = ["Snake", "Water", "Gun"]
    choose2 = random.choice(list)
    choose1 = input("Enter 'snake', 'Water' or 'Gun':\n")
    if choose1 == "snake" or choose1 == "Snake":
        if choose2 == "Snake":
            print("Choice are same")
            draw += 1
        elif choose2 == "Water":
            print("You win the round")
            userWin += 1
        else:
            print("computer Win the Round")
            comWin += 1
    elif choose1 == "water" or choose1 == "Water":
        if choose2 == "Snake":
            print("You win the round")
            userWin += 1
        elif choose2 == "Water":
            print("Choice are same")
            draw += 1
        else:
            print("computer Win the Round")
            comWin += 1
    elif choose1 == "gun" or choose1 == "Gun":
        if choose2 == "Snake":
            print("computer Win the Round ")
            comWin += 1
        elif choose2 == "Water":
            print("You win the round")
            userWin += 1
        else:
            print("Choice are same")
        draw += 1
print(f"Total Draws are {draw}")
print(f"You win {userWin} times")
print(f"Computer win {comWin} times")
if userWin < comWin:
    print("so computer is win this game")
else:
    print("So you win the game")


