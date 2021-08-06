#https://www.w3schools.com/python/numpy/numpy_random.asp

from numpy import random

# x = random.randint(100)
# print(x)

x=random.randint(100, size=(5, 2))
print(x)