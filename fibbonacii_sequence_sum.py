#wap to genrate a fibbonacii sequence and store it in a list and then find the sum of even element of the list
l=[0,1]
n=int(input("Enter a number:"))
for i in range(1,n):
    c=(l[-1]+l[-2])
    l.append(c)
print(l)
a=filter(lambda x:x%2==0,l)
print(list(a))
b=sum(a)
print(b)
