from sympy import *

x = symbols('x')
init_printing()

pprint(Integral(4 * x / sqrt(pow(x, 2) + 1), x), use_unicode=False)
