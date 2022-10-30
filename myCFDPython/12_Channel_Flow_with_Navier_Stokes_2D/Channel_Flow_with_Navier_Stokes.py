# 开发人员：leo
# 开发时间：2022/10/30 14:29

# Channel Flow with Navier Stokes

import numpy
from matplotlib import pyplot, cm

"""
画等高线参考代码
plt.contour(x1, x2, z, colors=list('kbrbk'), linestyles=['--', '--', '-', '--', '--'],
                    linewidths=[1, 0.5, 1.5, 0.5, 1], levels=[-1, -0.5, 0, 0.5, 1])
以上是画5条等值线，并指定每条轮廓线的颜色、线型、线宽和值，当只需要一个值时(例如画Levl set的0等值线)，[]只需要取一个值即可

"""

def plotP(x, y, p, u, v):
    pyplot.figure(figsize=(11, 7), dpi=100)
    X, Y = numpy.meshgrid(x, y)
    # plotting the pressure field as a contour, contourf是画云图。contour()是绘制轮廓线，contourf()会填充轮廓
    pyplot.contourf(X, Y, p, alpha=0.8, cmap="rainbow")  # alpha混合值，介于0（透明）和1（不透明）之间
    pyplot.colorbar()
    pyplot.title("p distribution")
    # plotting the pressure field outlines, contour是画等值线
    #pyplot.contour(X, Y, p, colors='k')
    # plotting velocity field
    pyplot.quiver(X[::3, ::3], Y[::3, ::3], u[::3, ::3], v[::3, ::3])  # quiver画速度矢量图，箭头长度与速度模量成正比
    # 符号::2表示每隔2个网格点取一个值，不然依据网格点画的速度矢量图太密集了
    pyplot.xlabel('X')
    pyplot.ylabel('Y')
    pyplot.show()


def plotU(x, y, u, v):
    pyplot.figure(figsize=(11, 7), dpi=100)
    X, Y = numpy.meshgrid(x, y)
    pyplot.contourf(X, Y, u, alpha=0.9, cmap="rainbow")
    pyplot.colorbar()
    #pyplot.streamplot(X, Y, u, v, color="k", linewidth=1)  # 流线
    pyplot.title("u contour with streamline")
    pyplot.xlabel('X')
    pyplot.ylabel('Y')
    pyplot.show()


def plotV(x, y, u, v):
    pyplot.figure(figsize=(11, 7), dpi=100)
    X, Y = numpy.meshgrid(x, y)
    pyplot.contourf(X, Y, v, alpha=0.9, cmap="rainbow")
    pyplot.colorbar()
    #pyplot.streamplot(X, Y, u, v, color="k", linewidth=1)  # 流线
    pyplot.title("v contour with streamline")
    pyplot.xlabel('X')
    pyplot.ylabel('Y')
    pyplot.show()

"""
One thing to note is that we have periodic boundary conditions throughout this grid, 
so we need to explicitly calculate the values at the leading and trailing edge of our u vector.
"""

def build_up_b(b, rho, dt, u, v, dx, dy):  # 压力泊松方程的源项
    b[1:-1, 1:-1] = rho * (
            1 / dt * ((u[1:-1, 2:] - u[1:-1, 0:-2]) / (2 * dx) + (v[2:, 1:-1] - v[0:-2, 1:-1]) / (2 * dy)) \
            - ((u[1:-1, 2:] - u[1:-1, 0:-2]) / (2 * dx)) ** 2 \
            - 2 * (u[2:, 1:-1] - u[0:-2, 1:-1]) / (2 * dy) * (v[1:-1, 2:] - v[1:-1, 0:-2]) / (2 * dx) \
            - ((v[2:, 1:-1] - v[0:-2, 1:-1]) / (2 * dy)) ** 2)

    # 更新边界条件（计算周期性边界上的b值）
    # Periodic BC Pressure @ x = 2
    b[1:-1, -1] = rho * (
            1 / dt * ((u[1:-1, 0] - u[1:-1, -2]) / (2 * dx) + (v[2:, -1] - v[0:-2, -1]) / (2 * dy)) \
            - ((u[1:-1, 0] - u[1:-1, -2]) / (2 * dx)) ** 2 \
            - 2 * (u[2:, -1] - u[0:-2, -1]) / (2 * dy) * (v[1:-1, 0] - v[1:-1, -2]) / (2 * dx) \
            - ((v[2:, -1] - v[0:-2, -1]) / (2 * dy)) ** 2)

    # Periodic BC Pressure @ x = 0
    b[1:-1, 0] = rho * (
            1 / dt * ((u[1:-1, 1] - u[1:-1, -1]) / (2 * dx) + (v[2:, 0] - v[0:-2, 0]) / (2 * dy)) \
            - ((u[1:-1, 1] - u[1:-1, -1]) / (2 * dx)) ** 2 \
            - 2 * (u[2:, 0] - u[0:-2, 0]) / (2 * dy) * (v[1:-1, 1] - v[1:-1, -1]) / (2 * dx) \
            - ((v[2:, 0] - v[0:-2, 0]) / (2 * dy)) ** 2)

    return b


def pressure_poisson_periodic(p, dx, dy, b):
    pn = numpy.zeros_like(p)
    for q in range(nit):
        pn = p.copy()
        p[1:-1, 1:-1] = ((pn[1:-1, 2:] + pn[1:-1, 0:-2]) * dy ** 2 + (pn[2:, 1:-1] + pn[0:-2, 1:-1]) * dx ** 2 \
                         - b[1:-1, 1:-1] * dx ** 2 * dy ** 2) / (2 * (dx ** 2 + dy ** 2))

        # 更新边界条件
        # Periodic BC Pressure @ x = 2
        p[1:-1, -1] = ((pn[1:-1, 0] + pn[1:-1, -2]) * dy ** 2 + (pn[2:, -1] + pn[0:-2, -1]) * dx ** 2 \
                         - b[1:-1, -1] * dx ** 2 * dy ** 2) / (2 * (dx ** 2 + dy ** 2))

        # Periodic BC Pressure @ x = 0
        p[1:-1, 0] = ((pn[1:-1, 1] + pn[1:-1, -1]) * dy ** 2 + (pn[2:, 0] + pn[0:-2, 0]) * dx ** 2 \
                         - b[1:-1, 0] * dx ** 2 * dy ** 2) / (2 * (dx ** 2 + dy ** 2))

        # Wall boundary conditions, pressure
        p[-1, :] = p[-2, :]  # dp/dy = 0 at y = 2
        p[0, :] = p[1, :]  # dp/dy = 0 at y = 0

    return p


def channel_flow(u, v, dt, dx, dy, p, rho, nu, tolerance):
    # 定义中间变量
    un = numpy.empty_like(u)
    vn = numpy.empty_like(v)
    b = numpy.zeros((ny, nx))  # b是压力泊松方程的源项，其值与速度有关

    # 首次修正压强
    b = build_up_b(b, rho, dt, u, v, dx, dy)
    p = pressure_poisson_periodic(p, dx, dy, b)

    # 指定error并进入循环
    error = 1
    stepcount = 0  # 统计迭代次数

    # Numerical solution - FDM
    while error > tolerance:
        un = u.copy()
        vn = v.copy()

        # 速度推进
        u[1: -1, 1: -1] = un[1: -1, 1: -1] - un[1: -1, 1: -1] * dt / dx * (un[1: -1, 1: -1] - un[1: -1, 0: -2]) \
                          - vn[1: -1, 1: -1] * dt / dy * (un[1: -1, 1: -1] - un[0: -2, 1: -1]) \
                          - dt / (2 * rho * dx) * (p[1: -1, 2:] - p[1: -1, 0: -2]) \
                          + nu * (dt / dx ** 2 * (un[1: -1, 2:] - 2 * un[1: -1, 1: -1] + un[1: -1, 0: -2]) \
                                  + dt / dy ** 2 * (un[2:, 1: -1] - 2 * un[1: -1, 1: -1] + un[0: -2, 1: -1])) + dt * F

        v[1: -1, 1: -1] = vn[1: -1, 1: -1] - un[1: -1, 1: -1] * dt / dx * (vn[1: -1, 1: -1] - vn[1: -1, 0: -2]) \
                          - vn[1: -1, 1: -1] * dt / dy * (vn[1: -1, 1: -1] - vn[0: -2, 1: -1]) \
                          - dt / (2 * rho * dy) * (p[2:, 1: -1] - p[0: -2, 1: -1]) \
                          + nu * (dt / dx ** 2 * (vn[1: -1, 2:] - 2 * vn[1: -1, 1: -1] + vn[1: -1, 0: -2]) \
                                  + dt / dy ** 2 * (vn[2:, 1: -1] - 2 * vn[1: -1, 1: -1] + vn[0: -2, 1: -1]))

        # 更新边界条件
        # Periodic BC u @ x = 2
        u[1: -1, -1] = un[1: -1, -1] - un[1: -1, -1] * dt / dx * (un[1: -1, -1] - un[1: -1, -2]) \
                          - vn[1: -1, -1] * dt / dy * (un[1: -1, -1] - un[0: -2, -1]) \
                          - dt / (2 * rho * dx) * (p[1: -1, 0] - p[1: -1, -2]) \
                          + nu * (dt / dx ** 2 * (un[1: -1, 0] - 2 * un[1: -1, -1] + un[1: -1, -2]) \
                                  + dt / dy ** 2 * (un[2:, -1] - 2 * un[1: -1, -1] + un[0: -2, -1])) + dt * F

        # Periodic BC u @ x = 0
        u[1: -1, 0] = un[1: -1, 0] - un[1: -1, 0] * dt / dx * (un[1: -1, 0] - un[1: -1, -1]) \
                          - vn[1: -1, 0] * dt / dy * (un[1: -1, 0] - un[0: -2, 0]) \
                          - dt / (2 * rho * dx) * (p[1: -1, 1] - p[1: -1, -1]) \
                          + nu * (dt / dx ** 2 * (un[1: -1, 1] - 2 * un[1: -1, 0] + un[1: -1, -1]) \
                                  + dt / dy ** 2 * (un[2:, 0] - 2 * un[1: -1, 0] + un[0: -2, 0])) + dt * F

        # Periodic BC v @ x = 2
        v[1: -1, -1] = vn[1: -1, -1] - un[1: -1, -1] * dt / dx * (vn[1: -1, -1] - vn[1: -1, -2]) \
                          - vn[1: -1, -1] * dt / dy * (vn[1: -1, -1] - vn[0: -2, -1]) \
                          - dt / (2 * rho * dy) * (p[2:, -1] - p[0: -2, -1]) \
                          + nu * (dt / dx ** 2 * (vn[1: -1, 0] - 2 * vn[1: -1, -1] + vn[1: -1, -2]) \
                                  + dt / dy ** 2 * (vn[2:, -1] - 2 * vn[1: -1, -1] + vn[0: -2, -1]))

        # Periodic BC v @ x = 0
        v[1: -1, 0] = vn[1: -1, 0] - un[1: -1, 0] * dt / dx * (vn[1: -1, 0] - vn[1: -1, -1]) \
                          - vn[1: -1, 0] * dt / dy * (vn[1: -1, 0] - vn[0: -2, 0]) \
                          - dt / (2 * rho * dy) * (p[2:, 0] - p[0: -2, 0]) \
                          + nu * (dt / dx ** 2 * (vn[1: -1, 1] - 2 * vn[1: -1, 0] + vn[1: -1, -1]) \
                                  + dt / dy ** 2 * (vn[2:, 0] - 2 * vn[1: -1, 0] + vn[0: -2, 0]))

        # Wall BC: u,v = 0 @ y = 0,2
        u[0, :] = 0
        u[-1, :] = 0
        v[0, :] = 0
        v[-1, :] = 0

        # 修正压强  # 此处与原代码在顺序上有些区别，将压强的修正放在了速度推进的后面，旨在最后一次迭代求出速度后，还需最后一次修正压强
        b = build_up_b(b, rho, dt, u, v, dx, dy)
        p = pressure_poisson_periodic(p, dx, dy, b)

        # 统计残差
        error = (numpy.sum(numpy.abs(u) - numpy.abs(un)) /
                  numpy.sum(numpy.abs(u)))
        # error1 = (numpy.sum(u) - numpy.sum(un)) / numpy.sum(u)
        # print(error1 == error)

        # 统计迭代次数
        stepcount += 1

    return u, v, p, stepcount


# Control parameters
xmin = 0
xmax = 2
ymin = 0
ymax = 2
nx = 41  # the number of grid points
ny = 41
# nt = 10  # Total time steps we want to calculate
nit = 50  # pseudo-time，设置泊松方程迭代次数
dx = (xmax - xmin) / (nx - 1)
dy = (ymax - ymin) / (ny - 1)
rho = 1
nu = .1  # Viscosity coefficient
F = 1
dt = .01
tolerance = 0.001  # tolerance -> required error
# 计算下CFL数

# Assign initial conditions and meshes
x = numpy.linspace(xmin, xmax, nx)
y = numpy.linspace(ymin, ymax, ny)
# X, Y = numpy.meshgrid(x, y)  # 该定义挪到了plot相关的函数中
u = numpy.zeros((ny, nx))  # ny是行数，nx是列数
v = numpy.zeros((ny, nx))
p = numpy.zeros((ny, nx))
# b = numpy.zeros((ny, nx))  # b是压力泊松方程的源项  # 在cavity flow里面重复定义了，可以删除

# Boundary Conditions 仅仅是初始时刻的边界条件
u[0, :] = 0
u[:, 0] = 0
u[:, -1] = 0
u[-1, :] = 0
v[0, :] = 0
v[-1, :] = 0
v[:, 0] = 0
v[:, -1] = 0
p[:, -1] = 0  # dp/dx = 0 at x = 2
p[:, 0] = 0  # dp/dx = 0 at x = 0
p[-1, :] = p[-2, :]  # dp/dy = 0 at y = 2
p[0, :] = p[1, :]  # dp/dy = 0 at y = 0

# Plot initial conditions
# plotP(x, y, p, u, v)
# plotU(x, y, u, v)

# Numerical solution for cavity flow- FDM
u, v, p, stepcount=channel_flow(u, v, dt, dx, dy, p, rho, nu, tolerance)
print("共迭代了{0}次，达到残差{1}".format(stepcount, tolerance))


# postProcessing
plotP(x, y, p, u, v)
plotU(x, y, u, v)
# plotV(x, y, u, v)
