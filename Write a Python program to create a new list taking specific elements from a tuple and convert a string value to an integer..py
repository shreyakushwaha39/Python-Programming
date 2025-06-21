##Write a Python program to create a new list taking specific elements from
##a tuple and convert a string value to an integer.
# Given tuple
tup = ('10', '20', '30', 'forty', '50', '60')
selected_elements = tup[0:6:2]
new_list = list(map(lambda x: int(x), selected_elements))
print(new_list)

