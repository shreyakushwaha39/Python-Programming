#wap to use the random module to generate 10 random numbers between 1 and 100  and 2. stimulate the rolling of a dice
import random
print('10 random numbers between 1 and 100:')
for i in range(10):
    print(random.randint(1,100))
print('Rolling a dice:')
print(random.randint(1,6))