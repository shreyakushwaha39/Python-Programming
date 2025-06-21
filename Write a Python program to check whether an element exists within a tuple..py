#Write a Python program to check whether an element exists within a tuple.
t=(45,67,89,90,23,12)
num=int(input("Enter an element:"))
if num in t:
    print("Element is present in the tuple")
else:
    print("Element is not present in the tuple")
