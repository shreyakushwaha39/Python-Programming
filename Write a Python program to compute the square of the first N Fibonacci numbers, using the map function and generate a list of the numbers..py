##Write a Python program to compute the square of the first N Fibonacci
##numbers, using the map function and generate a list of the numbers.
n=[0,1,1,2,3,5,7]
square=list(map(lambda x: x**2,n))
print(square)
