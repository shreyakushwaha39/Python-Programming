#compute nth fibbonaccii number by recurrsion
def fibbo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibbo(n-1)+fibbo(n-2)
n=int(input("Enter the number:"))
print(fibbo(n))
