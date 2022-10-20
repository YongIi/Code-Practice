# 开发人员：leo
# 开发时间：2022/10/12 17:55

# 1-D Convection Diffusion Equation -- Burgers’ equation

import numpy  # a library that provides a bunch of useful matrix operations
from matplotlib import pyplot as plt # 2D plotting library
import sympy  # the symbolic math library for Python 例如可以用来帮忙给函数求导
# 以下两行其实可以省略，只是为了显示好看点
from sympy import init_printing  # 渲染sympy计算的结果，例如使用LATEX显示
init_printing(use_latex=True)  # tell SymPy that we want all of its output to be rendered using LATEX
# lambdify函数可以将SymPy symbolic equation and turns it into a callable function
from sympy.utilities.lambdify import lambdify
# import time, sys  # provide basic timing functions that we'll use to slow down animations for viewing

# Control parameters
Lx = 2*numpy.pi  # spatial domain size
nx = 101  # the number of grid points
dx = Lx / (nx - 1)  # the distance between any pair of adjacent grid points
nt = 100  # Total time steps we want to calculate
nu = 0.03  #the value of viscosity
# sigma = .2  # CFL number
dt = dx * nu  #  time step (delta t)
# print("dx =", dx)  # 仅用于debug
print("dt =", dt)

# Initial Conditions
x, nu, t = sympy.symbols('x nu t')  # setting up symbolic variables for the three variables in our initial condition
phi = (sympy.exp(-(x - 4 * t)**2 / (4 * nu * (t + 1))) +
       sympy.exp(-(x - 4 * t - 2 * sympy.pi)**2 / (4 * nu * (t + 1))))
print("phi =", phi)
phiprime = phi.diff(x)
print("phiprime =", phiprime)
u = -2 * nu * (phiprime / phi) + 4
print("u =", u)
print(type(u))
"""
# 测试sympy的求导功能
y2 = sympy.sin(5*x**2)
print(y2)
print(y2.diff(x))
# print(dir(sympy))  # 查看sympy可用的函数
"""
# u已经是一个SymPy symbolic equation，lambdify将其转化为一个可调用的函数，并指定t, x, nu是自变量，u是待求变量
ufunc = lambdify((t, x, nu), u)
print(ufunc)
print(ufunc(1, 4, 3))
x = numpy.linspace(0, Lx, nx)
un = numpy.empty(nx)
t = 0
nu = 0.03  # 从symbolic variables转回来
u = numpy.asarray([ufunc(t, x0, nu) for x0 in x])
"""
# 展示初始条件
# print(u)
plt.figure(figsize=(11, 7), dpi=100)
plt.plot(x, u, marker='o', lw=2)
plt.title("saw-tooth function")
plt.xlim([0, Lx])
plt.ylim([0, 10]);
plt.show()
"""

# Numerical solution - FDM
for n in range(nt):  # 时间推进
    un=u.copy()  # 将上一时间步的结果复制给un
    # 改写：采用矩阵操作，省略循环操作
    u[1:-1] = un[1:-1] - un[1:-1] * dt / dx * (un[1:-1] - un[0:-2]) + nu * dt / (dx ** 2) * (un[2:] - 2 * un[1:-1] + un[0:-2])
    """
    for i in range(1,nx-1):  # 根据上一步的结果un，计算出这一步的u
        u[i] = un[i] - un[i]*dt/dx*(un[i]-un[i-1]) + nu*dt/(dx**2)*(un[i+1]-2*un[i]+un[i-1])  # 注意要控制CFL数，否则容易发散
    """
    # 处理完内部网格后再处理边界网格，先求入口边界网格的值(由于u[-1] = u[0]，un[i-1]取un[-2])，再拷贝给出口网格
    u[0] = un[0] - un[0] * dt / dx * (un[0] - un[-2]) + nu * dt / (dx ** 2) * (un[1] - 2 * un[0] + un[-2])
    u[-1] = u[0]  # 周期性边界条件



# analytical solution
u_analytical = numpy.asarray([ufunc(nt * dt, xi, nu) for xi in x])


# postProcessing
plt.figure(figsize=(11, 7), dpi=100)
u0 = numpy.asarray([ufunc(0, x0, nu) for x0 in x])
plt.plot(x, u0, marker='*', lw=2, label='IC')
plt.plot(x,u, marker='o', lw=2, label='Computational')
plt.plot(x, u_analytical, label='Analytical')
plt.xlim([0, Lx])
plt.ylim([0, 10])
plt.legend();
plt.show()  # 将绘图在IDE中显示出来
