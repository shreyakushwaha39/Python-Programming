#Write a Python program to split a multi-line string into a list of lines.
##Sample Output:
##Original string: This
##is a
##multiline
##string.
##Split the said multiline string into a list of lines:
##['This', 'is a', 'multiline', 'string.', '']
import sys
s=sys.stdin.read()
print(s)
a=s.split()
print("Split the said multiline string into a list of lines:")
print(a)
