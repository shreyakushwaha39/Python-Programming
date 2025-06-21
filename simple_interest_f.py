#write a program to calculate simple interest suppose the customer is a senior citizen then the rate of interest is 12% otherwise the rate of interest is 10%
def si(p,t,age):
    if age>=60:
        r=12
    else:
        r=10
    return p*t*r/100
p=int(input("Enter the principal amount: "))
t=int(input("Enter the time period: "))
age=int(input("Enter the age of the customer: "))
print("The simple interest is: ",si(p,t,age))