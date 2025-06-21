#wap that  genrate the set of prime number and another set of odd number
a={x for x in range(1,21) if x%2!=0}
print('odd number:',a)
b={x for x in range(2,21) if all(x%i!=0 for i in range(2,x))}
print('prime number:',b)
print('union of these sets',a.union(b))
print('intersection of these sets:',a.intersection(b))
print('symmetric difference of these sets:',a.difference(b))
