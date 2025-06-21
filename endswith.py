a=input("Enter a string:")
b=input("Enter a start substring :")
c=input("Enter a end substring :")
if a.endswith(b):
    print("Yes,string ends with",b)
else:
    print("No")
if a.startswith(c):
    print("Yes,string starts with",c)
else:
    print("No")