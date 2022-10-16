# 开发人员：leo
# 开发时间：2022/10/11 14:50

# 1-D Linear Convection

import numpy  # a library that provides a bunch of useful matrix operations
from matplotlib import pyplot  # 2D plotting library
# import time, sys  # provide basic timing functions that we'll use to slow down animations for viewing

# nx = 81  # the number of grid points

def linearConv(nx):
    # Control parameters
    Lx = 2  # spatial domain that is 2 units of length wide
    dx = Lx / (nx - 1)  # grid size
    nt = 20  # Total time steps we want to calculate
    # dt = 0.025  # time step (delta t)
    c = 1  # wavespeed of c = 1
    # print("dx =", dx)
    CFL = 0.5
    dt = CFL * dx / c

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
        for i in range(1,nx):  # 根据上一步的结果un，计算出这一步的u
            u[i] = un[i] - c*dt/dx*(un[i]-un[i-1])

    pyplot.plot(numpy.linspace(0, Lx, nx), u)
    pyplot.show()  # 将绘图在IDE中显示出来

linearConv(41)
# linearConv(61)
# linearConv(71)
# linearConv(81)
linearConv(91)
linearConv(101)
linearConv(121)
linearConv(201)