# i=0
# while(i<45):
#     print(i)
#     i=i+1

n=0
while(n<10):
    try:
        num = int(input("Enter a number:\n"))
        print(num * num)
    except Exception as e:
        print("please enter a number")

    n+=1

