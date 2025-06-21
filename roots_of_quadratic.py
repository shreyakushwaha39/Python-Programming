#wap to find the roots of a quadratic equation
a=float(input("Enter the coefficient of x^2:"))
b=float(input("Enter the coefficient of x:"))
c=float(input("Enter the coefficient of c:"))
d=((b**2)-4*a*c)
if(d>0):
    root1=(-b+((d)**0.5))/(2*a)
    root2=(-b-((d)**0.5))/(2*a)
    print("real roots:",root1,root2)
elif(d==0):
    root1=-b/(2*a)
    print("Equal roots are ",root1,root1)
elif(d<0):
    real_part = -b / (2 * a)
    imaginary_part = ((-d)**0.5) / (2 * a)
    print(f"Imaginary roots are: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")
else:
    print("error")
   
    
    




