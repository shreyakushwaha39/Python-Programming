#Write a Python program to find the index of an item in a tuple.
t=(34,55.67,347,890)
item=float(input("Enter an element:"))
for i in t:
    if item in t:
        print("Item is present in a tuple",item)
        break
    else:
        print("Item is not present in a tuple")
    
    
    
