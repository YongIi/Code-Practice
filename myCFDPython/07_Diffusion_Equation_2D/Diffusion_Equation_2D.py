# 开发人员：leo
# 开发时间：2022/10/25 10:53

# Nonlinear Convection 2D
"""
the problem to be solved: du/dt = nu*(ddu/(dx**2)) + nu*(ddu/(dy)**2)

# the expected phenomena is that the velocities will tend to spread
# from the high values to the low values; this can be best seen in the plots
"""

import numpy
from matplotlib import pyplot, cm

# Control parameters
Lx = 2  # spatial domain size
Ly = 2
nx = 31  # the number of grid points
ny = 31
dx = Lx / (nx - 1)  # the distance between any pair of adjacent grid points
dy = Ly / (ny - 1)
nt = 17  # Total time steps we want to calculate
nu = 0.05
sigma = .25  # CFL number
dt = sigma * dx * dy / nu  #  time step (delta t)
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
fig = pyplot.figure()  # initializing a figure window,  specify the size and resolution
# ax = fig.gca(projection='3d')  # 为绘图窗口指定轴标签“ax”，并指定它将是三维投影绘图。老版本用法
ax = fig.add_subplot(projection='3d')  # 为绘图窗口指定轴标签“ax”，并指定它将是三维投影绘图
X, Y = numpy.meshgrid(x, y)
ax.plot_surface(X, Y, u, cmap=cm.viridis, rstride=1, cstride=1, linewidth=0, antialiased=False)  # rstride x方向条纹数=网格数grids/2。值越大图片越粗糙，默认值为1
# ax.plot_surface(X, Y, u[:], cmap='rainbow', linewidth=0, antialiased=False)
pyplot.title('2D Diffusion Equation - IC')
ax.set_zlim(1,2.5)
ax.set_xlim(0,2)
ax.set_ylim(0,2)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
pyplot.show()

pyplot.figure()
pyplot.contourf(X, Y, u[:], cmap="rainbow")
pyplot.title('2D Diffusion Contour - IC')
pyplot.colorbar()
pyplot.show()


# Numerical solution - FDM
def diffuse(nt):
    u[int(.5 / dy):int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2
    for n in range(nt + 1):  # 可不可以不+1
        un = u.copy()
        u[1:-1, 1:-1] = un[1:-1, 1:-1] + nu * dt / dx**2 * (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, 0:-2]) \
                                       + nu * dt / dy**2 * (un[2:, 1:-1] - 2 * un[1:-1, 1:-1] + un[0:-2, 1:-1])
        # 更新边界条件
        u[0, :] = 1  # 第0行，列是[:]
        u[-1, :] = 1
        u[:, 0] = 1
        u[:, -1] = 1

    # postProcessing
    fig = pyplot.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(X, Y, u[:], rstride=1, cstride=1, cmap=cm.viridis,
                    linewidth=0, antialiased=True)
    ax.set_zlim(1, 2.5)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    pyplot.title('2D Diffusion Equation - nt ={0}'.format(nt))
    pyplot.show()

    pyplot.figure()
    pyplot.contourf(X, Y, u[:], cmap="rainbow")
    pyplot.title('2D Diffusion Contour - nt ={0}'.format(nt))
    pyplot.colorbar()
    pyplot.show()


diffuse(10)
diffuse(14)
diffuse(50)







