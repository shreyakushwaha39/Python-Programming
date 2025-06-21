#Write a Python script that takes input from the user and displays that
#input back in upper and lower cases.
s=input("Enter a python script:")
for i in s:
    if i.isupper():
        print(i.lower(),end='')
    else:
        print(i.upper(),end='')
