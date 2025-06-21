a=int(input("enter a number:"))
m=a
s=0
p=len(str(a))
while(a>0):
    d=a%10
    s+=d**p
    a//=10
if(m==s):
    print("given number is an armstrong number")
else:
    print("given number is not an armstrong number")
