#wap to use reduce function to find product of all elements of the list
from functools import reduce
l=[2,3,4,5,6,7,8,9,10]
product=reduce(lambda x,y: x*y,l)
print(product)
