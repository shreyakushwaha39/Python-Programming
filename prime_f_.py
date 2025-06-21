# Write a program to check whether a number is prime or not.
def prime(n):
    if (n<=1) :
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input("Enter a number:"))
if prime(n):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")