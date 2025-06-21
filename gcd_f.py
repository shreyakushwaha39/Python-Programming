#wap to find gcd of two numbers by using function
def gcd(m,n):
    g=1
    a=min(m,n)
    for i in range(1,a+1):
        if(m%i==0 and n%i==0):
            if i>g:
                g=i
    return g
m=int(input("m: "))
n=int(input("n: "))
ans=gcd(m,n)
print("gcd of",m,"and",n,"is",ans)
    