import sys
print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/Users/Ming/Documents/CodingNomads/2019_crashcourse/week2/miercoles'])

import printing_functions as x

"""
import module_name
from module_name import function_name
from module_name import function_name as fn import module_name as mn
from module_name import *
"""

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
x.print_models(unprinted_designs, completed_models)
x.show_completed_models(completed_models)
