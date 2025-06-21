#Write a Pytho program to remove an item from a tuple.
t=(34,56.78,345,455)
item=float(input("Enter an element:"))
a=list(t)
if item in a:
    a.remove(item)
    print(tuple(a))
else:
    print("Element is not present in the tuple")
