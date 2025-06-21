##Write a Python program to split a string on the last occurrence of the
##delimiter.
s=input("Enter a string:")
d=input("Enter a delimiter:")
a=s.rsplit(d,1)
if len(a)>1:
    print(a)
else:
    print(s)

