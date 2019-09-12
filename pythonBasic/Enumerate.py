list1 = ["Bhindi", "Alo", "chowmein", "chopsticks"]

i=1
# for item in list1:
#     if i%2 is not 0:
#         print(f" jarvis please buy {item}")
#     i +=1

for index, item in enumerate(list1):
    if index%2==0:
        print(f" jarvis please buy {item}")