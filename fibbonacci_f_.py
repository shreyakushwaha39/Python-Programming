#0 1 1 2 3 5 8 13 21 34...
def fibbonacci(n):
    a=0
    b=1
    for i in range(1,n):
        print(a)
        c=(a+b)
        a=b
        b=c
    return a
n=int(input("Enter a number:"))
f=fibbonacci(n)
print("nth fibbonaccii number is",f)

    

