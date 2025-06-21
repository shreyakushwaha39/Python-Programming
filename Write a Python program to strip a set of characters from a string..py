#Write a Python program to strip a set of characters from a string.
s=input("Enter a string:")
ch={',','!','o'}
result=' '.join(char for char in s if char not in ch)
print(result)

