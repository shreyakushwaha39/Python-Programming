# Write a function that takes a number as input and returns the sum of digits of the number.
def sum_of_digit(n):
    s=0
    while(n>0):
        d=n%10
        s+=d
        n//=10
    return s
n=int(input("Enter a number:"))
ans=sum_of_digit(n)
print("sum of digit is",ans)
