#wap to call all function from my custom module
from mathpack import arithmatic,geometry
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
print(arithmatic.add(a,b))
print(arithmatic.sub(a,b))
print(arithmatic.mul(a,b))
print(arithmatic.div(a,b))
#for area of rectangle
l=float(input("Enter length of rectangle:"))
b=float(input("Enter breadth of rectangle:"))
print("area of rectangle:",geometry.area_of_rectangle(l,b))
#for area of circle
r=float(input("enter radius:"))
print("area of circle:",geometry.area_of_circle(r))