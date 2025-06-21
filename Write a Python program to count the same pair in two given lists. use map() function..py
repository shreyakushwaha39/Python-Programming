##Write a Python program to count the same pair in two given lists. use
##map() function.
l1 = [6, 7, 8, 9, 3, 4, 5]
l2 = [6, -8, -6, -7, -9, 4, 5]
same_pairs = list(map(lambda x: x[0] == x[1], zip(l1, l2)))
count = same_pairs.count(True)
print("Number of same pairs:", count)
