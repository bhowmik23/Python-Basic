# Map function
# numbers = ["3", "4", "5", "7"]
# numbers= list(map(int, numbers))
# for i in range(len(numbers)):
#     numbers[i]=int(numbers[i])
# numbers[2]=numbers[2]+1
# print(numbers[2])
#
# def sq(a):
#     return a*a
#
# num = [2,3,1,4,5,6,8,0]
# square = list(map(sq, num))
# print(square)

# num = [2,3,1,4,5,6,8,0]
# square = list(map(lambda x: x*x, num))
# print(square)


# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a
# func= [square, cube]
# num = [2,3,1,4,5,6,8,0]
# for i in range(5):
#     val= list(map(lambda x:x(i), func))
#     print(val)

# filter function

num = [2,3,1,4,5,6,8,0]
def is_grater_5(num):
    return num>5
gr_than_5=list(filter(is_grater_5,num))
print(gr_than_5)

# reduce function
from functools import reduce
list = [2, 2, 4, 5, 5, 7]
num =reduce(lambda x,y:x+y, list)
# num=0
# for i in list:
#     num= num + i
print(num)

