p=float(input("Enter the principal amount: "))
r=float(input("Enter the rate of interest: "))
t=float(input("Enter the time period in years: "))
d=p*(1+r/100)**t
print("The compound interest is: ",d-p)
