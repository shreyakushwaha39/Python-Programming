#wap to create a set of square and cube of numbers from 1 to 20 and perform the following operations on it
#1. update the set
#2. remove an element from the set
#3. remove a specified element from the set
#4. add an element to the set
#5. clear the set
#6. pop an element from the set
a={x**2 for x in range(1,21)}
b={x**3 for x in range(1,21)}
print('square:',a)
print('cube:',b)
print('update:',a.update(b))
#pop() method removes a random element from the set
print('pop:',a.pop())
print('set after pop:',a)
#remove() method removes the specified element from the set
print('remove:',a.remove(8))
print('set after remove:',a)
#add() method adds an element to the set
print('add:',a.add(8))
print('set after add:',a)
#clear() method removes all the elements from the set
print('clear:',a.clear())
print('set after clear:',a)

