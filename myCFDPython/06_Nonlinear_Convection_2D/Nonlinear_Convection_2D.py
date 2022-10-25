# 开发人员：leo
# 开发时间：2022/10/22 17:25

# Nonlinear Convection 2D
"""
the problem to be solved: du/dt + u*du/dx +v*du/dy = 0
                          dv/dt + u*dv/dx +v*dv/dy = 0

非线性对流方程越来越像NS方程了（忽略粘性项、耗散项等等），在二维问题中，要分别在x方向求u的分量，在y方向上求v的分量

"""


import numpy
from matplotlib import pyplot, cm

# Control parameters
Lx = 2  # spatial domain size
Ly = 2
nx = 101  # the number of grid points
ny = 101
dx = Lx / (nx - 1)  # the distance between any pair of adjacent grid points
dy = Ly / (ny - 1)
nt = 80  # Total time steps we want to calculate
sigma = .2  # CFL number
dt = dx * sigma  #  time step (delta t)
# print("dx =", dx)  # 仅用于debug
print("dt =", dt)


# Assign initial conditions and meshes
x = numpy.linspace(0, Lx, nx)
y = numpy.linspace(0, Ly, ny)
u = numpy.ones((ny, nx))  # ny是行数，nx是列数
v = numpy.ones((ny, nx))  # ny是行数，nx是列数
un = numpy.ones((ny, nx))
vn = numpy.ones((ny, nx))
print(id(u) is id(un))  # False
u[int(.5 / dy):int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2  # 数组切片后没有生成新的数组，因为切片是右开区间，所以要加上1， # index = x/dx
v[int(.5 / dy):int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2
# Plot initial conditions
fig = pyplot.figure(figsize=(11, 7), dpi=100)  # initializing a figure window,  specify the size and resolution
# ax = fig.gca(projection='3d')  # 为绘图窗口指定轴标签“ax”，并指定它将是三维投影绘图。老版本用法
ax = fig.add_subplot(projection='3d')  # 为绘图窗口指定轴标签“ax”，并指定它将是三维投影绘图
X, Y = numpy.meshgrid(x, y)
ax.plot_surface(X, Y, u, cmap=cm.viridis, rstride=2, cstride=2)  # rstride x方向条纹数=网格数grids/2。值越大图片越粗糙，默认值为1
# ax.plot_surface(X, Y, u[:], cmap='rainbow', linewidth=0, antialiased=False)
ax.set_zlim(0.5,2.5)
ax.set_xlim(0,2)
ax.set_ylim(0,2)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
pyplot.show()

pyplot.figure()
pyplot.contourf(X, Y, u[:], cmap="rainbow")
pyplot.colorbar()
pyplot.show()


# Numerical solution - FDM
for n in range(nt+1):  # 可不可以不+1
    un = u.copy()
    vn = v.copy()
    # 在Python中，对于坐标(i, j)，指标j写在前面，i写在后面
    u[1:, 1:] = un[1:, 1:] - un[1:, 1:] * dt / dx * (un[1:, 1:] - un[1:, :-1]) \
                           - vn[1:, 1:] * dt / dy * (un[1:, 1:] - un[:-1, 1:])

    v[1:, 1:] = vn[1:, 1:] - un[1:, 1:] * dt / dx * (vn[1:, 1:] - vn[1:, :-1]) \
                           - vn[1:, 1:] * dt / dy * (vn[1:, 1:] - vn[:-1, 1:])

    # 更新边界条件
    u[0, :] = 1  # 第0行，列是[:]
    u[-1, :] = 1
    u[:, 0] = 1
    u[:, -1] = 1

    v[0, :] = 1  # 第0行，列是[:]
    v[-1, :] = 1
    v[:, 0] = 1
    v[:, -1] = 1

# postProcessing
fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.add_subplot(projection='3d')
# X, Y = numpy.meshgrid(x, y)  # IC中已经定义过了
ax.plot_surface(X, Y, u, cmap=cm.viridis, rstride=2, cstride=2)
ax.set_zlim(0.5,2.5)
ax.set_xlim(0,2)
ax.set_ylim(0,2)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
pyplot.title('2D Nonlinear Convection - x velocity')
pyplot.show()

fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.add_subplot(projection='3d')
# X, Y = numpy.meshgrid(x, y)  # IC中已经定义过了
ax.plot_surface(X, Y, v, cmap=cm.viridis, rstride=2, cstride=2)
ax.set_zlim(0.5,2.5)
ax.set_xlim(0,2)
ax.set_ylim(0,2)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
pyplot.title('2D Nonlinear Convection - y velocity')
pyplot.show()


pyplot.figure()
pyplot.contourf(X, Y, u, cmap="rainbow")
pyplot.title("u contour")
pyplot.colorbar()
pyplot.show()

pyplot.figure()
pyplot.contourf(X, Y, v, cmap="rainbow")
pyplot.title("v contour")
pyplot.colorbar()
pyplot.show()