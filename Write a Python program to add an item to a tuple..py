#Write a Python program to add an item to a tuple.
t=(23,'ddcd',56.67,'True')
print(t)
a=list(t)
a.extend([456,56.66,'True'])
t1=tuple(a)
print(t1)
