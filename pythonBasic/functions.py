a=4
b=6
c=sum((a,b)) #Built in function
def function1(a, b):
    print("hello you are a function", a+b)
print(function1(5, 7))
print(c)

def function2(d,e):
    """This is a ffunction which calculate average of two numbers"""
    average=(d+e)/2
    print(average)
    return average
v= function2(5,6)
print(v)
print(function2.__doc__)