# Write a program to check whether a number is palindrome or not using functions.
def palindrome(n):
    rev=0
    while(n>0):
        d=n%10
        rev=rev*10+d
        n//=10
    return rev
n=int(input("Enter a number:"))
ans=palindrome(n)
if(ans==n):
    print("palindrome")
else:
    print("not a palindrome")