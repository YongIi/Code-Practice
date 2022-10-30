# 开发人员：leo
# 开发时间：2022/10/27 16:46

# 2D Poisson equation

"""
this is very similar to the Laplace eq, but this time we a have a non-homgenous（非齐次项-源项）
eq, which has a free term that is a source term
this will be expressed as two pressure spikes (one positive and one negative)
the iterations will advance in pseudo-time to relax the spikes

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

# Control parameters
nx = 50
ny = 50
nt  = 100  # pseudo-time，设置迭代次数
xmin = 0
xmax = 2
ymin = 0
ymax = 1
dx = (xmax - xmin) / (nx - 1)
dy = (ymax - ymin) / (ny - 1)

# Assign initial conditions and meshes
p  = numpy.zeros((ny, nx))
pn = numpy.zeros((ny, nx))
b  = numpy.zeros((ny, nx))
x  = numpy.linspace(xmin, xmax, nx)
y  = numpy.linspace(ymin, ymax, ny)

# Source
b[int(ny / 4), int(nx / 4)]  = 100  # index求法一：index = x/dx x是实际坐标  求法二：index = ny / 4   1/4总网格点处
b[int(3 * ny / 4), int(3 * nx / 4)] = -100

# Plot initial conditions
plot3D(x, y, b)
plot2D(x, y, b)

# Numerical solution - FDM
for n in range(nt):
    pn = p.copy()
    # 在Python中，对于坐标(i, j)，指标j写在前面，i写在后面
    p[1:-1, 1:-1] = ((pn[1:-1, 2:] + pn[1:-1, 0:-2])* dy**2 + (pn[2:, 1:-1] + pn[0:-2, 1:-1]) * dx**2 \
                     - b[1:-1, 1:-1] * dx**2 * dy**2) / (2 * (dx**2 + dy** 2))

    # 更新边界条件
    p[0, :] = 0
    # p[ny - 1, :] = 0
    p[-1, :] = 0
    p[:, 0] = 0
    # p[:, nx - 1] = 0
    p[:, -1] = 0

# postProcessing
plot3D(x, y, p)
plot2D(x, y, p)
