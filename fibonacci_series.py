# 0 1 1 2 3 5 8 13
n=int(input("Enter number of terms:"))
a=0
b=1
for i in range(1,n+1):
    print(a)
    c=(a+b)
    a=b
    b=c


