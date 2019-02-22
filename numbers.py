'''
float, integer


after the class or function:
the first line use """ which is the docstring
'''

# float
f = 1.434
# integer
i = 2

print(type(f), type(i))

# implicit type conversion
print(int(f * i))
print(round(f * i, 3))


def add_two(self, a, b):
        """
        add the two numbers
        :param a: first variable
        :param b: second variable
        """

