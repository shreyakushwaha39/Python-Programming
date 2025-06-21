#wap to create a dictionary of cubes of odd numbers in the range 1 to 10
a={x:x**3 for x in range(1,11) if x%2!=0}
print(a)
