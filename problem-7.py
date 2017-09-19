"""
Problem #7: Fahrenheit to Celsius

There are two widespread systems of measuring temperature - Celsius and Fahrenheit.
First is quite popular in Europe and second is well in use in United States for example.
You are to write a program to convert degrees of Fahrenheit to Celsius.

Notes:
This must be run with Python 3

data:
495 353 168 -39 22
answer:
257 178 76 -39 -6
"""

from random import randint
import math

far_amount = randint(1, 10)
print("Amount of temps to convert: %s\n" % far_amount)

far_list = []
for i in range(far_amount):
        far_temp = randint(0, 999)
        far_list.append(far_temp)

print("Fahrenheit list:")
print(far_list)

def round_num(c):
    decimal_num = c - math.floor(c)
    if decimal_num >= 0.5:
        c = math.ceil(c)
    else:
        c = math.floor(c)
    return c

cel_list = []
far_length = len(far_list)
div = 5 / float(9)
for i in range(far_length):
    cel = far_list[i] * div
    cel = round_num(cel)
    cel_list.append(int(cel))

print("Celsius list:")
print(cel_list)
