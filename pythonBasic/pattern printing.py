# Pattern Printing
num= int(input("Enter no of rows: "))

for i in range(0,num+1):
    print("*"*i)

print()
for i in range(num,0,-1):
    print("*"*i)
print()

i=1
while(i<=num):
    print("*"*i)
    i+=1
print()
while(num>0):
    print("*"*num)
    num-=1