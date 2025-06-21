# Write a Python program to find the factorial of a number provided by the user.
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Enter a number:"))
print("Factorial of",n,"is",factorial(n))