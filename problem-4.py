"""
Problem #4: Minimum of Two

Of two numbers, select one with minimum value.

Note:
This must be run with Python 3

Example:

data:
3
5 3
2 8
100 15

answer:
3 2 15
"""

from random import randint

pair_amount = randint(1, 5)
print("Amount of pairs: %s\n" % pair_amount)

num_list1 = []
num_list2 = []

for i in range(pair_amount):
    num_list1.append(randint(0, 100))
    num_list2.append(randint(0, 100))

print("A =", end=" ")
print(num_list1)

print("B =", end=" ")
print(num_list2)

print()

min_list = []
for i in range(len(num_list1)):
    if num_list1[i] < num_list2[i]:
        min_list.append(num_list1[i])
    else:
        min_list.append(num_list2[i])

print("C =", end=" ")
print(min_list)
