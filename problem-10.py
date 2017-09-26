"""
Problem #10

Linear function is defined by an equation:

y(x) = ax + b

Where a and b are some constants.
For example, with a=3, b=2 function will yield values y = 2, 5, 8, 11...
for x = 0, 1, 2, 3...

Your task is to determine a and b by two points, belonging to the function.
I.e. you are told two pairs of values (x1, y1), (x2, y2) which satisfy the function equation
and you should restore the equation itself.

Input data have the number of test-cases in the first line
and then test-cases themselves in separate lines.
Each case contains 4 integers (x1 y1 x2 y2).
Answers should be integer too and you are to write them in line,
separating with spaces and enclosing each pair in parenthesis, for example:

input data:
2
0 0 1 1
1 0 0 1

answer:
(1 0) (-1 1)
"""

from random import randint

# Keeping amount of test cases small
test_cases = randint(1,5)
print("Test cases: %s" % test_cases)

points_list = []
for i in range(test_cases):
    # Variable definition for better readability
    # Using values greater than zero to avoid error handling
    # and focus more on logic
    x1 = randint(1,5)
    x2 = randint(1,5)
    y1 = randint(1,5)
    y2 = randint(1,5)
    points_list.append([x1,y1,x2,y2])

print("Points list:")
print(points_list)

# Not truly sure if this is correct...
def find_slope(points):
    # Variable definition for better readability
    x1 = points[0]
    x2 = points[2]
    y1 = points[1]
    y2 = points[3]
    # Needs division by zero handling
    a = (y2-y1) / (x2-x1)
    # Using (x1, y1)
    b = y1 - (a*x1)
    pair = (a,b)
    return pair

pair_list = []
for i in range(len(points_list)):
    pair_list.append(find_slope(points_list[i]))

print("Pair list:")
print(pair_list)
