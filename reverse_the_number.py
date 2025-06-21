a=int(input("Enter a number:"))
m=a
s=0
while(a>0):
    d=a%10
    s=s*10+d
    a//=10
print("sum of digit :",s)