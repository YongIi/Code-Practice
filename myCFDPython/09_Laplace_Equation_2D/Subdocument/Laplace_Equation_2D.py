# 开发人员：leo
# 开发时间：2022/10/27 14:19

# Laplace Equation 2D

import numpy
# from matplotlib import pyplot, cm
# import laplace2d
from laplace2d import laplace2d
#from plot import plot as plt  # 第一个plot是软件包（目录），第二个plot是模块，来自plot.py文件
import plot.plot as plt  # 同上

# Control parameters
Lx = 2  # spatial domain size
Ly = 1
nx = 31  # the number of grid points
ny = 31
dx = 2 / (nx - 1)  # the distance between any pair of adjacent grid points
dy = 2 / (ny - 1)  # 即使y方向与x方向距离不一样，但是网格数量是一样的
l1norm_target = 1e-4  # l1norm_target: tolerance -> required error
"""  没有时间相关的参数
nt = 120  # Total time steps we want to calculate
sigma = .0009  # CFL number
nu = 0.01  # Viscosity coefficient
dt = sigma * dx * dy / nu  #  time step (delta t)
print("dx =", dx)  # 仅用于debug
print("dt =", dt)
"""

# Assign initial conditions and meshes
p = numpy.zeros((ny, nx))
x = numpy.linspace(0, Lx, nx)
y = numpy.linspace(0, Ly, ny)


# Boundary Conditions
p[:, 0] = 0  # p = 0 @ x = 0
p[:, -1] = y  # p = y @ x = 2
p[0, :] = p[1, :]  # dp/dy = 0 @ y = 0
p[-1, :] = p[-2, :]  # dp/dy = 0 @ y = 1

# Plot initial conditions
plt.plot3D(x, y, p)
plt.plot2D(x, y, p)

# Numerical solution - FDM
laplace2d(p, y, dx, dy, l1norm_target)

# postProcessing
plt.plot3D(x, y, p)
plt.plot2D(x, y, p)





