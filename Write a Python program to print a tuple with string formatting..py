##Write a Python program to print a tuple with string formatting.
##Sample tuple : (100, 200, 300)
##Output : This is a tuple (100, 200, 300)
s=input("Enter a string:")
a=s.split(',')
for i in a:
    print((i,))
