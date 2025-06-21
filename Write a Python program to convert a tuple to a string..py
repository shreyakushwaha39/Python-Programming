#Write a Python program to convert a tuple to a string.
t=(34,56.67,'True',444)
a=','.join(map(str,t))
print(a)
