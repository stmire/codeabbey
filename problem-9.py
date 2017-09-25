"""Look at http://www.mathwarehouse.com/geometry/triangles/triangle-formulas.php
For Triangle Inequality Theorem"""

"""
Problem #9: Triangles

You are given several triplets of values representing lengths of the sides of triangles.
You should tell from which triplets it is possible to build triangle and for which it is not.

Notes:

data:
2
3 4 5
1 2 4

answer:
1 0
"""

from random import randint

# Using the Triangle Inequality Theorem
def is_tri_equal(triangle = []):
    a = triangle[0]
    b = triangle[1]
    c = triangle[2]
    if a == b and b == c: return 1
    equality_flag = 0
    if (a+b)>c and (b+c)>a and (a+c)>b:
        equality_flag = 1
    return equality_flag

tri_amount = randint(1, 5)
print("Amount of triangles: %s\n" % tri_amount)

tri_list = []
for i in range(tri_amount):
    a = randint(1,3)
    b = randint(1,3)
    c = randint(1,3)
    triangle = [a,b,c]
    tri_list.append(triangle)

equal_list = []
print("Triangle list:")
for triangle in tri_list:
        print(triangle)
        is_equal = is_tri_equal(triangle)
        equal_list.append(is_equal)
print("")

print("Equality list:")
print(equal_list)
