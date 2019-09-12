f= open("Biddut.txt", "rt")
content= f.read()
print(content)
for line in f:
    print(line, end="")
content= f.read(56)
print(f.read(3))

print(f.readline())
print(f.readline())
print(f.readline())

print(f.readlines())


f.close()