# Write a program that converts a binary number to a decimal number.
# The program should take an input from the user and display the corresponding decimal number.
n=float(input("Enter a number:"))
a=n//1
dr=n-a
de=int(((str(dr))[2:6])[::-1])
p=-1
m=0
s=0
while(a>0):
    d=a%10
    s+=d*2**m
    m+=1
    a//=10
while(de>0):
    d=de%10
    s+=d*2**p
    p-=1
    de//=10
print("In binary :",s)