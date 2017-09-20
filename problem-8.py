"""
Problem #8: Arithmetic Progression

Arithmetic sequence is completely defined by
the first member (A) and the increment value - step size - (B).
First few members could be expressed as
[A + (A + B) + (A + 2B) + (A + 3B) + ...]
You are to calculate the sum of first members of arithmetic sequence.

Notes:
This must be run with Python 3

data:
2
5 2 3
3 0 10

answer:
21 30
"""

from random import randint

trip_amount = randint(1, 5)
print("Amount of pairs: %s\n" % trip_amount)

#trip_list = [[5,2,3],[3,0,10]]
trip_list = []
for i in range(trip_amount):
    a = randint(0, 20)
    b = randint(0,10)
    c = randint(0,10)
    triplet = [a,b,c]
    trip_list.append(triplet)

print("Triplet list:")
for triplet in trip_list:
        print(triplet)
print("")

sum_list = []
for triplet in trip_list:
    a = triplet[0]
    b = triplet[1]
    c = triplet[2]
    acc = 0
    for i in range(c):
        acc += (a + (b*i))
    sum_list.append(acc)

print("Sum list:")
print(sum_list)
