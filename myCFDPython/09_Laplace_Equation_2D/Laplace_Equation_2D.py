# 开发人员：leo
# 开发时间：2022/10/27 14:19

# Laplace Equation 2D

"""
the equation to be solved: ddp/dx**2 + ddp/dy**2 = 0
Dirichlet boundary（第一类边界条件）—在端点，待求变量的值被指定。
Neumann boundary（第二类边界条件）—待求变量边界外法线的方向导数被指定。
"""

import numpy
from matplotlib import pyplot, cm


def plot3D(x, y, p):  # 3个参数，x-vector, a y-vector and our p matrix
    fig = pyplot.figure(figsize=(11, 7), dpi=100)  # initializing a figure window,  specify the size and resolution
    ax = fig.add_subplot(projection='3d')  # 为绘图窗口指定轴标签“ax”，并指定它将是三维投影绘图
    X, Y = numpy.meshgrid(x, y)
    ax.plot_surface(X, Y, p[:], cmap=cm.viridis, rstride=1, cstride=1, linewidth=0,
                    antialiased=False)  # rstride x方向条纹数=网格数grids/2。值越大图片越粗糙，默认值为1
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 1)
    ax.view_init(30, 225)  # 视角转换
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    pyplot.show()


def plot2D(x, y, p):
    pyplot.figure()
    X, Y = numpy.meshgrid(x, y)
    pyplot.contourf(X, Y, p[:], cmap="rainbow")
    pyplot.colorbar()
    pyplot.show()

def laplace2d(p, y, dx, dy, l1norm_target):  # l1norm_target: tolerance -> required error
    l1norm = 1
    pn = numpy.empty_like(p)  # 返回一个与给定数组相同形状和类型的新数组。其值是任意的

    # solve the discretized form of governing equations
    while l1norm > l1norm_target:
        pn = p.copy()
        p[1:-1, 1:-1] = (dy**2 * (pn[1:-1, 2:] + pn[1:-1, 0:-2]) \
                       + dx**2 * (pn[2:, 1:-1] + pn[0:-2, 1:-1])) / (2 * (dx**2 + dy**2))
        # 更新边界条件
        p[:, 0] = 0  # p = 0 @ x = 0  # Dirichlet boundary
        p[:, -1] = y  # p = y @ x = 2
        p[0, :] = p[1, :]  # dp/dy = 0 @ y = 0  # Neumann boundary
        p[-1, :] = p[-2, :]  # dp/dy = 0 @ y = 1

        # calulation of error magnitude
        l1norm = (numpy.sum(numpy.abs(p[:]) - numpy.abs(pn[:])) /
                  numpy.sum(numpy.abs(pn[:])))

        l1norm2 = numpy.sum(numpy.abs(p[:] - pn[:])) / numpy.sum(numpy.abs(pn[:]))

        # print(l1norm == l1norm2)  # always True this case

        # TO DO
        # 添加对迭代次数的计算

    return p


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
plot3D(x, y, p)
plot2D(x, y, p)

# Numerical solution - FDM
laplace2d(p, y, dx, dy, l1norm_target)

# postProcessing
plot3D(x, y, p)
plot2D(x, y, p)





