#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10

if number < 0:
    ld = -ld

if ld > 5:
    s = 'greater than 5'
elif ld < 6 and ld != 0:
    s = 'less than 6 and not 0'
else:
    s = '0'
print(f'Last digit of {number} is {ld} and is {s}')
