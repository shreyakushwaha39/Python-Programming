#Write a Python program to remove an empty tuple(s) from a list of tuples.
#Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
#Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
l=[(56,56),(),(45,43,67,89),(9,23,90,88),()]
for i in l:
    if i!=():
        print(i,end='')
