# Program to find factorial

def factorial(x):
    f = 1
    for i in range(1, x+1):
        f *= i
    return f

x = 5
print(factorial(x))