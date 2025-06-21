# Write a function that takes an integer as input and returns True if the number is even and False if the number is odd.
def even_odd(n):
    if n%2==0:
        return True
    else:
        return False
n=int(input("Enter a number:"))
if even_odd(n):
    print(n,"is an even number")
else:
    print(n,"is an odd number")