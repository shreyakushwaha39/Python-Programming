#wap to find permutation of n and r using function
def fact(n):
        if n==0:
            return 1
        else:
            return n*fact(n-1)
def permutation(n,r):
    if n<r:
        return "Invalid input"
    else:
        return fact(n)/fact(n-r)
n=int(input("Enter a number:"))
r=int(input("Enter the value of r:"))
print("The permutation of",n,"and",r,"is:",permutation(n,r))

