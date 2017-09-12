"""
Problem #3: Sum in Loops

Input data will contain the total count of pairs to process in the first line.
The following lines will contain pairs themselves- one pair at each line.
Answer should contain the results separated by spaces.

Example:

data:
3
100 8
15 245
1945 54

answer:
108 260 1999
"""

from random import randint

list_count = randint(1, 9)
print("Amount of pairs: %s" % list_count)

pair_list = []
for i in range(list_count):
        a = randint(0, 1000)
        b = randint(0, 1000)
        pair = [a,b]
        pair_list.append(pair)
print

print("Pair list:")
for pair in pair_list:
        print(pair)
print

sum_string = ""
for pair in pair_list:
        num = pair[0] + pair[1]
        sum_string += str(num) + " "

print("Sum list: %s" % sum_string)
