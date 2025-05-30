#Python program to implement pseudo random number generator.

import random
a=int(input("Enter the seed value: "))
random.seed(a)
b=int(input("Enter the range: "))
for i in range(b):
    print(random.randint(0,900))
