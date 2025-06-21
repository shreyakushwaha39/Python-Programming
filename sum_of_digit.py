# 1. Write a program to find the sum of digits of a number.
a=int(input("Enter a number:"))
m=a
s=0
while(a>0):
    d=a%10
    s+=d
    a//=10
print("sum of digit :",s)