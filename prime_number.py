#wap to check whether a given number is a prime number or not
n=int(input("enter a program:"))
flag=0
for i in range(2,n):
    if(n%i==0):
        flag=1
if(flag==1):
    print("not a prime number")
else:
    print("prime number")