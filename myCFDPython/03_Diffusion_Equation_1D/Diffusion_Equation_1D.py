# 开发人员：leo
# 开发时间：2022/10/12 17:55

# 1-D Diffusion Equation

import numpy  # a library that provides a bunch of useful matrix operations
from matplotlib import pyplot  # 2D plotting library
# import time, sys  # provide basic timing functions that we'll use to slow down animations for viewing

# Control parameters
Lx = 2  # spatial domain that is 2 units of length wide
nx = 81  # the number of grid points
dx = Lx / (nx - 1)  # the distance between any pair of adjacent grid points
nt = 80  # Total time steps we want to calculate
nu = 0.3  #the value of viscosity
sigma = .2  # CFL number
dt = sigma * (dx ** 2) / nu  #  time step (delta t)
# print("dx =", dx)  # 仅用于debug
print("dt =", dt)

# Initial Conditions
# setting u = 2 between 0.5 and 1, and u=1 everywhere else in (0,2)
u = numpy.ones(nx)  # nx elements long with every value equal to 1.
u[int(.5 / dx):int(1 / dx + 1)] = 2  # 数组切片后没有生成新的数组，因为切片是右开区间，所以要加上1， # index = x/dx
# print(u)
pyplot.plot(numpy.linspace(0, Lx, nx), u)
pyplot.show()  # 将绘图在IDE中显示出来

# Numerical solution - FDM
un = numpy.ones(nx)  # initialize a temporary array, to hold the values we calculate for the n+1 timestep
for n in range(nt):  # 时间推进
    un=u.copy()  # 将上一时间步的结果复制给un
    for i in range(1,nx-1):  # 根据上一步的结果un，计算出这一步的u
        u[i] = un[i] + nu*dt/(dx**2)*(un[i+1]-2*un[i]+un[i-1])  # 注意要控制CFL数，否则容易发散

# print(u)  # 仅用于debug

# postProcessing
pyplot.plot(numpy.linspace(0, Lx, nx), u)
pyplot.show()  # 将绘图在IDE中显示出来