"""
Problem #5: Minimum of Three

Several triplets of numbers are given to you.
Your task is to select minimum among each of triplets.

Note:
This must be run with Python 3

data:
3
7 3 5
15 20 40
300 550 137

answer:
3 15 137
"""

from random import randint

pair_amount = randint(1, 5)
print("Amount of pairs: %s\n" % pair_amount)

pair_list = []
for i in range(pair_amount):
        a = randint(0, 1000)
        b = randint(0, 1000)
        c = randint(0, 1000)
        pair = [a,b,c]
        pair_list.append(pair)

print("Pair list:")
for pair in pair_list:
        print(pair)
print("")

min_list = []
min_num = 0
for pair in pair_list:
    min_num = pair[0]
    for i in pair:
        if i <= min_num:
            min_num = i
    min_list.append(min_num)


print("Minimum list:", end=" ")
print(min_list)
