#wap to find sum of numbers between m and n
m=int(input("m: "))
n=int(input("n: "))
s=0
for i in range(m,n+1):
    s+=i
print("sum of number between",m,"to",n,"is:",s)