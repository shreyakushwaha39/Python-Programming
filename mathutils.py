def fac(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True