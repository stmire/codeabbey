"""
Problem #6: Rounding

There are several pairs of numbers.
For each pair you are to divide first by second
and return the result, rounded to the nearest integer.

Note:
This must be run with Python 3

input data:
3
12 8
11 -3
400 5

answer:
2 -4 80
"""

from random import randint
import math

pair_amount = randint(1, 5)
print("Amount of pairs: %s\n" % pair_amount)

pair_list = []
for i in range(pair_amount):
        # Forcing higher numerator to avoid error handling
        a = randint(10, 100)
        b = randint(-10, 10)
        if b == 0: b = randint(-10, 10) # In case 0 is assigned
        pair = [a,b]
        pair_list.append(pair)

print("Pair list:")
for pair in pair_list:
        print(pair)
print("")

def round_num(c):
    decimal_num = c - math.floor(c)
    print(decimal_num) # For debugging
    if c > 0:
        if decimal_num >= 0.5:
            c = math.ceil(c)
        else:
            c = math.floor(c)
        return c
    elif c < 0:
        if decimal_num <= (0.5):
            c = math.floor(c)
        else:
            c = math.ceil(c)
        return c


rounded_list = []
for pair in pair_list:
    if pair[0] % pair[1] == 0:
        c = pair[0] / pair[1]
        rounded_list.append(int(c))
        continue
    else:
        c = pair[0] / pair[1]
        c = round_num(c)
        rounded_list.append(int(c))

print("Rounded list:")
print(rounded_list)
