##Write a Python program to convert a given string list to a tuple.
##Original string: python 3.0
##<class 'str'>
##Convert the said string to a tuple:
##('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
##<class 'tuple'>
s=input("Original string:")
print(type(s))
l=[]
print("Convert the said string to a tuple:")
for i in s:
    if i!=" ":
        l.append(i)
t=tuple(l)
print(t)
print(type(t))
