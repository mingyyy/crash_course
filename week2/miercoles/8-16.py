'''
8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file .
Import the function into your main program file, and call the function using each of these approaches:

import module_name
from module_name import function_name
from module_name import function_name as fn import module_name as mn
from module_name import *
'''

l = [1,3,[234,[34,345]],[23,43,[0,789,[3]]]]

# import flattening
# print(flattening.unpack_list(l))


# from flattening import unpack_list as ul
# print(ul(l))

from flattening import *
print(unpack_list(l))




