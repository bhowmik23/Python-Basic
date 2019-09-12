with open("Biddut.txt") as f:
    a= f.readlines()
    print(a)
f= open("Biddut.txt")
print(f.readlines())
print(f.readline())
f.close()