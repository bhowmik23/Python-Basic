# def fun1():
#     print("hello")
# fun2=fun1
# del fun1
# fun2()

# def fucreutrn(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
# a = fucreutrn(0)
# print(a)

# def executer(func):
#     func("this")
# executer(print)

def dec1(func1):
    def nowexecute():
        print("Executing now")
        func1()
        print("Executed")
    return nowexecute
@dec1
def who_is_biddut():
    print("Biddut is a good boy")
# who_is_biddut= dec1(who_is_biddut)
who_is_biddut()