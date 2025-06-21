#wap to reduce maximum element from the list using reduce function
from functools import reduce
l=[2,3,4,5,6,7,8,9,10]
max=reduce(lambda x,y: x if x>y else y,l)
print(max)