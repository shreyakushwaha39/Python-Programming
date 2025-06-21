#wap that create a list of numbers from 1-20 that are either divisible by 2 or 4 without using filter function
l=[x for x in range(1,20) if((x%2==0)or(x%4==0))]
print(l)