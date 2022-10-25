# 开发人员：leo
# 开发时间：2022/10/21 16:55

# Linear Convection - 2D
# the problem to be solved: du/dt + c*du/dx +c*du/dy = 0
"""
本质是物理量u，在二维速度场(c, c)中的移动，理论上u的形状与大小不会发生变化，但是数值格式问题总会有数值耗散
"""

import numpy
from matplotlib import pyplot, cm
from datetime import datetime
# 在 3.2.0 版更改：在 Matplotlib 3.2.0 之前，有必要显式导入 mpl_toolkits.mplot3d模块以使 '3d' 投影到 Figure.add_subplot
# from mpl_toolkits.mplot3d import axes3d, Axes3D  ##New Library required for projected 3d plots


# Control parameters
Lx = 2  # spatial domain size
Ly = 2
nx = 81  # the number of grid points
ny = 81
dx = Lx / (nx - 1)  # the distance between any pair of adjacent grid points
dy = Ly / (ny - 1)
nt = 100  # Total time steps we want to calculate
c = 1  # wavespeed of c = 1
sigma = .2  # CFL number
dt = dx * sigma  #  time step (delta t)
# print("dx =", dx)  # 仅用于debug
print("dt =", dt)

# Assign initial conditions and meshes
x = numpy.linspace(0, Lx, nx)
y = numpy.linspace(0, Ly, ny)
u = numpy.ones((ny, nx))  # ny是行数，nx是列数
un = numpy.ones((ny, nx))
print(id(u) is id(un))  # False
u[int(.5 / dy):int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2  # 数组切片后没有生成新的数组，因为切片是右开区间，所以要加上1， # index = x/dx
# Plot initial conditions
fig = pyplot.figure(figsize=(11, 7), dpi=100)  # initializing a figure window,  specify the size and resolution
# ax = fig.gca(projection='3d')  # 为绘图窗口指定轴标签“ax”，并指定它将是三维投影绘图。老版本用法
ax = fig.add_subplot(projection='3d')  # 为绘图窗口指定轴标签“ax”，并指定它将是三维投影绘图
X, Y = numpy.meshgrid(x, y)
ax.plot_surface(X, Y, u[:], cmap=cm.viridis)
# ax.plot_surface(X, Y, u[:], cmap='rainbow', linewidth=0, antialiased=False)
ax.set_zlim(1,2.5)
ax.set_xlim(0,2)
ax.set_ylim(0,2)
ax.set_xlabel("X Label")
ax.set_ylabel("Y Label")
pyplot.show()

pyplot.figure()
pyplot.contourf(X, Y, u[:], cmap="rainbow")
pyplot.colorbar()
pyplot.show()

# Numerical solution - FDM
# nested for loops, time-consuming, 取消注释使用
"""
time1 = datetime.now()
for n in range(nt+1):  # 可不可以不+1
    un = u.copy()
    row, col = u.shape
    for j in range(1, row): # 最后一层网格也求解了，是否可以不用求解，即到row-1，是否会影响结果？ 不影响，因为每次更新边界条件时都会把对最后一层网格的求解更新为边界条件
        for i in range(1, col):
            u[j, i] = un[j,i] - c * dt / dx * (un[j, i] - un[j , i-1]) - \
                                c * dt / dy * (un[j, i] - un[j-1, i])
    # 更新边界条件
    u[0, :] = 1  # 第0行，列是[:]
    u[-1, :] = 1
    u[:, 0] = 1
    u[:, -1] = 1
print("嵌套循环时间：", datetime.now() - time1)
"""
# 采用矩阵操作代替嵌套循环
time2 = datetime.now()
for n in range(nt+1):  # 可不可以不+1
    un = u.copy()
    u[1:, 1:] = un[1:, 1:] - c * dt / dx * (un[1:, 1:] - un[1:, :-1]) - \
                              c * dt / dy * (un[1:, 1:] - un[:-1, 1:])
    # 更新边界条件
    u[0, :] = 1  # 第0行，列是[:]
    u[-1, :] = 1
    u[:, 0] = 1
    u[:, -1] = 1
print("矩阵操作时间：", datetime.now() - time2)

# postProcessing
fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, u[:], cmap=cm.viridis)
pyplot.xlabel('X')
pyplot.ylabel('Y')
pyplot.title('2D Linear Convection')
pyplot.show()


pyplot.figure()
pyplot.contourf(X, Y, u[:], cmap="rainbow")
pyplot.colorbar()
pyplot.show()

print(u[int(1. / dy), int(1. / dx)])
print(u[int(1.25 / dy), int(1.25 / dx)])
print(u[int(1.75 / dy), int(1.75 / dx)])

print("加速倍数：", 0.543773 / 0.003015)

