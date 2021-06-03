from sympy.interactive import printing
printing.init_printing(use_latex=True)
from sympy import *
import sympy as sy
x = symbols('x')
f  = sy.Function('f')(x)
print(f)
diffeq = Eq(f.diff(x,x)-20*f-36,0)
print(diffeq)
solution = dsolve(diffeq,f)
print(solution)
