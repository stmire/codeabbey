"""
Problem #2: Sum in Loop

Let us find the sum of several numbers (more than two).
It will be useful to do this in a loop.
You can create variable sum and add every value from the list to it.

Example:

input data:
8
10 20 30 40 5 6 7 8

answer:
126
"""

from random import randint

elements = randint(0, 9)
nums = []
numsString = ''

for i in range(elements):
    rand = randint(0, 99)
    nums.append(rand)
    numsString += "%s " % rand

acc = 0
for num in nums:
    acc += num

print("Amount of elements: %s" % elements)
print("Elements in list: %s" % numsString)
print("Sum of elements: %s" % acc)
