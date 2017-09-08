"""
Problem #1: Sum "A+B"

We need to sum two numbers and tell the result.
Though you can do it manually, try to write a simple program
in any language you know, or like, or want to learn.

Example:

input data:
3 5

answer:
8
"""

from random import randint

a = randint(0, 9)
b = randint(0, 9)
c = a + b

print("A is %s" % a)
print("B is %s" % b)
print("A+B is %s" % c)
