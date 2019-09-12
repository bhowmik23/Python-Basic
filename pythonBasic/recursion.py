# n! = n * n-1 * n-2 *n-3....
# n! = n * (n-1)!
def factorial_iterative(n):
    fact=1
    for i in range(n): # start from i and ends with n-1
        fact= fact*(i+1)
    return fact

num= int(input("Enter a number:\n"))
print(factorial_iterative(num))

def factorial_recursivee(n):
    if n==1:
        return 1
    else:
        return n* factorial_iterative(n-1)
num1=int(input("Enter a number:\n"))
print(factorial_recursivee(num1))