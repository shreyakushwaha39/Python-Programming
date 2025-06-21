#wap to find the sum of the series 1/1!+2/2!+3/3!+4/4!+...n/n!
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
def taylor(n):
    sum=0
    s=''
    for i in range(1,n+1):
        num=i**i
        den=fact(i)
        s+=str(i**i)+'/'+str(i)+"!"+'+'
        sum+=num/den
    return sum,s
n=int(input("Enter a number:"))
s,series=taylor(n)
print("The series is:",series[:-1],"=",s)



    