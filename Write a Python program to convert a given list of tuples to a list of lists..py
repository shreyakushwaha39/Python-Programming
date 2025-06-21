##Write a Python program to convert a given list of tuples to a list of lists.
##Original list of tuples: [(1, 2), (2, 3), (3, 4)]
##Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
##Original list of tuples: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
##Convert the said list of tuples to a list of lists: [[1, 2], [2, 3, 5], [3, 4],[2, 3, 4, 2]]
l=[(1, 2), (2, 3), (3, 4)]
print("Original list of tuples:",l)
L=[]
for i in l:
    a=list(i)
    L.append(a)
print("Convert the said list of tuples to a list of lists:",L)
    

