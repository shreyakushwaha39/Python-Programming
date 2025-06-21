#Wap that calculate fib(n) using a dictionary
l=[0,1]
n=int(input("Enter a number:"))
for i in range(1,n+1):
    c=(l[-1]+l[-2])
    l.append(c)
k=[x for x in range(1,n+1)]
dic=dict(zip(k,l))
print(sorted(dic.items()))