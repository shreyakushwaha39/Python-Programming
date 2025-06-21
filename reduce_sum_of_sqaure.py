#wap to write a function to reduce the sum of square of the list
from functools import reduce
l=[2,3,4,5,6,7,8,9,10]
sum=reduce(lambda x,y: x+y,[x**2 for x in l])
print(sum)
