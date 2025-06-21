##Write a Python program to replace the last value of tuples in a list.
##Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
##Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
l=[(45,56),(67,78),(90,91)]
L=[]
L.append(l[0:-1])
print(L)
