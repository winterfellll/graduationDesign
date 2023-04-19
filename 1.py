import random

num = 31
while num >= 2:
    x = random.randint(1, 4)
    yi = x
    jia = 5 - x
    num -= yi
    num -= jia
print(num)
