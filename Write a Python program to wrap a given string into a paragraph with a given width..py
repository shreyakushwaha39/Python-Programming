##Write a Python program to wrap a given string into a paragraph with a
##given width.
##Sample Output:
##Input a string: The quick brown fox.
##Input the width of the paragraph: 10
##Result:
##The quick
##brown fox.
s=input("Input a string:")
width=input("Input the width of the paragraph")
a=s.split()
print(' '.join(a[0:2]))
print(' '.join(a[2:len(a)]))
