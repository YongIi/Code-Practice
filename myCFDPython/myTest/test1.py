import numpy  # a library that provides a bunch of useful matrix operations
from matplotlib import pyplot as plt # 2D plotting library
import sympy  # the symbolic math library for Python 例如可以用来帮忙给函数求导
# lambdify函数可以将SymPy symbolic equation and turns it into a callable function
from sympy.utilities.lambdify import lambdify
# import time, sys  # provide basic timing functions that we'll use to slow down animations for viewing


x = sympy.symbols('x')
phi = 5*(x+1)**3
print("phi =", phi)
phiprime = phi.diff(x)
print("phiprime =", phiprime)
u = -2 * (phiprime / phi) + 4
print("u =", u)
print(type(u))
ufunc = lambdify((x), u)
x = numpy.linspace(0, 10, 10)
u = numpy.asarray([ufunc(x0) for x0 in x])

# postProcessing
plt.figure(figsize=(11, 7), dpi=100)
plt.plot(x,u, marker='o', lw=2, label='Computational')
#plt.xlim([0, 10])
#plt.ylim([0, 10])
plt.legend();
plt.show()  # 将绘图在IDE中显示出来
