a=int(input("Enter a number:"))
b=a
sum=0
while(a>0):
    d=a%10
    sum+=(d*d*d)
    a//=10
if (sum==b):
    print(b,"is an armstrong number")
else:
    print(b,"a is not an armstrong number")