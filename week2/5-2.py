'''
5-2. More Conditional Tests: You don’t have to limit the number of tests you create to 10 .
If you want to try more comparisons, write more tests and add them to conditional_tests.py .
Have at least one True and one False result for each of the following:

• Tests for equality and inequality with strings
• Tests using the lower() function
• Numerical tests involving equality and inequality, greater than and less than, greater than or equal to,
and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
'''
import math
# Tests for equality and inequality with strings
a = "string"
b = "string "
print(a == b)
print(a == b.strip())

# Tests using the lower() function
a = "StRing"
b = "string"
print(a == b)
print(a.lower() == b)

# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to,
# and less than or equal to
print(1 == 1.00)
print(1 == -1.00)

print(10 >= 9.99)
print(10 <= 10.01)

print(2.71828 > math.e)
print(math.e < 2.7182)

# Tests using the and keyword and the or keyword
print(True or False)
print(True and False)

print(1 or 2 or 0  or -1) # print the first?
print(3 and 4 and -3 and 2) # print the last?

# • Test whether an item is in a list
# • Test whether an item is not in a list

l = [1, 3, 5, 10]
if 2 in l:
    print(True)
else:
    print(False)

