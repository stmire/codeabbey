"""
Problem #11

As any number greater than 9 is represented by several digits, we can calculate the sum of these digits.

For example, for numbers 1492 and 1776 we get:
1 + 4 + 9 + 2 = 16
1 + 7 + 7 + 6 = 21

In this task you will be given several numbers and asked to calculate their sums of digits.

Important: while many programming languages have built-in functions to convert numbers to strings
(from which digits could be extracted), you should not use this.

Instead you need to implement algorithm with repetitive division by 10 (base of numeral system)
and summing up the remainders.

input data:
3
11 9 1
14 90 232
111 15 111

answer:
1 16 21

Here the first case requires to calculate 11*9+1 = 100 and its sum of digits is 1+0+0 = 1.
"""

from random import randint

process_values = randint(1,9)
#print("Values to process: %s" % process_values)

digits_list = []
for i in range(process_values):
    a = randint(0,100)
    b = randint(0,100)
    c = randint(0,100)
    digits_list.append([a,b,c])
print("Digits list:")
print(digits_list)

values_list = []
for digits in digits_list:
    a = digits[0]
    b = digits[1]
    c = digits[2]
    base = (a*b+c)
    num = 0
    while (base > 0):
        num += base % 10
        base = base / 10
    values_list.append(num)
print("Values list:")
print(values_list)
