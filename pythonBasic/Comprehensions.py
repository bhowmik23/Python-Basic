'''
ls = []
for i in range(100):
    if i%3==0:
        ls.append(i)
print(ls)
'''

# list comprehension
'''
ls = [i for i in range(100) if i%3==0]
print(ls)
'''

# dict Comprehension
'''
# dict1 = {i:f"item{i}" for i in range(100) if i%4==0}
dict1 = {i:f"item{i}" for i in range(5)}
dict1 = {value:key for key,value in dict1.items()}
print(dict1)
'''
# set Comprehension
'''
dresses = {dress for dress in ["dress1", "dress2",  "dress2", "dress1"]}
print(dresses)

even = (i for i in range(100) if i%2==0)
# print(even.__next__())
# print(even.__next__())
# print(even.__next__())
# print(even.__next__())
for item in even:
    print(item)
'''

n = int(input("How many input :\n"))
input_string = input()
list = input_string.split()
choose = int(input("1. List\n 2. Dictionary\n 3. Set\n"))
if choose==1:
    ls = [i for i in list]
    print(ls)
elif choose==2:
    dict = {f"item{i}":i for i in list}
    print(dict)
elif choose==3:
    set = {i for i in list}
    print(set)
else:
    print("You enter wrong input")