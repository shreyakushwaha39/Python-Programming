#wap to find gcd of two numbers
m=int(input("m: "))
n=int(input("n: "))
a=min(m,n)
gcd=1
for i in range(1,a+1):
    if(m%i==0 and n%i==0):
        if i>gcd:
            gcd=i
print("gcd of",m,"and",n,"is",gcd)