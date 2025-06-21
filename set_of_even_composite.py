a={x for x in range(1,21) if x%2==0}
print('even number:',a)
c={x for x in range(2,21)}
b={x for x in range(2,21) if all(x%i!=0 for i in range(2,x))}
print('composite number:',c-b)
print('is superset',a.issuperset(b))
print('sum of composite number:',sum(c-b))
print('len of set:',len(b))