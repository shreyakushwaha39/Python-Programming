a=float(input("Enter a side1:"))
b=float(input("Enter a side2:"))
c=float(input("Enter a side3:"))
peri=a+b+c
s=peri/2
a=(s*(s-a)*(s-b)*(s-c))*0.5
print("Perimeter of triangle :",peri )
print("Area of triangle : ",a )


