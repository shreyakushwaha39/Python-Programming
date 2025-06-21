#wap to create a list of 10 random number,then create two list even and odd list which have all even odd number seperately
import random
l=[random.randint(1,11) for x in range(1,11) ]
print(l)
even=[x for x in l if(x%2==0)]
odd=[x for x in l if(x%2!=0)]
print(even)
print(odd)