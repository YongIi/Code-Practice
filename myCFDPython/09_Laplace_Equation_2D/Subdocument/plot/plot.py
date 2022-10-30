
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
