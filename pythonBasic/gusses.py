num=90
i=0
while(True):
    inp= int(input())
    i=i+1
    if i<5:
        if inp<num:
            print("increase")
            continue
        elif inp>num:
            print("Decrease")
            continue
        elif inp==num:
            print("You won")
            print("You gussess ", i ,"times")
            break
    else:
        print("Game Over")
        break
