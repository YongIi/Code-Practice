# 开发人员：liyong
# 开发时间：2022/11/16 14:47

import numpy as np
from matplotlib import pyplot as plt

"""
画等高线参考代码
plt.contour(x1, x2, z, colors=list('kbrbk'), linestyles=['--', '--', '-', '--', '--'],
                    linewidths=[1, 0.5, 1.5, 0.5, 1], levels=[-1, -0.5, 0, 0.5, 1])
以上是画5条等值线，并指定每条轮廓线的颜色、线型、线宽和值，当只需要一个值时(例如画Levl set的0等值线)，[]只需要取一个值即可

"""


def plotC(x, y, C):
    plt.figure(figsize=(5, 5), dpi=100)
    X, Y = np.meshgrid(x, y)
    # plt.contourf(X, Y, C[:], cmap="rainbow")
    plt.contour(X, Y, C[:], colors='k', linewidths=[2.0], levels=[0.0])
    plt.title("two-phase interface")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.show()


def plotContour(x, y, C):
    plt.figure(figsize=(6, 5), dpi=100)
    X, Y = np.meshgrid(x, y)
    plt.contourf(X, Y, C[:], cmap="rainbow")
    # plt.grid()
    plt.colorbar()
    # plt.title("volume fraction contour")
    plt.title("signed distance")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.show()

def saveContour(x, y, t, C):
    plt.figure(figsize=(5, 5), dpi=100)
    X, Y = np.meshgrid(x, y)
    plt.contourf(X, Y, C[:], cmap="rainbow_r", levels=[-100.0, 0.0, 100.0])
    # plt.grid()
    # plt.colorbar()
    # plt.title("volume fraction contour")
    plt.title("signed distance")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.savefig('C%.2fs.png' % t)
    plt.close()


# 以下代码用于二维流场中，速度u和v变化时
def plotU(x, y, u, v):
    plt.figure(figsize=(5, 5), dpi=100)
    X, Y = np.meshgrid(x, y)
    # plt.contourf(X, Y, u, alpha=0.9, cmap="rainbow")
    # plt.colorbar()
    # plt.streamplot(X, Y, u, v, color="k", linewidth=1.5)  # 流线
    # plt.title("u contour with streamline")
    interval = 11
    plt.quiver(X[::interval, ::interval], Y[::interval, ::interval], u[::interval, ::interval],
               v[::interval, ::interval])
    plt.title("velocity vector")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.show()


def plotu(x, y, u, v):
    plt.figure(figsize=(6, 5), dpi=100)
    X, Y = np.meshgrid(x, y)
    plt.contourf(X, Y, u, alpha=0.9, cmap="rainbow")
    plt.colorbar()
    plt.streamplot(X, Y, u, v, color="k", linewidth=1.5)  # 流线
    plt.title("u contour with streamline")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.show()


def plotv(x, y, u, v):
    plt.figure(figsize=(6, 5), dpi=100)
    X, Y = np.meshgrid(x, y)
    plt.contourf(X, Y, v, alpha=0.9, cmap="rainbow")
    plt.colorbar()
    plt.streamplot(X, Y, u, v, color="k", linewidth=1.5)  # 流线
    plt.title("v contour with streamline")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.show()


def plotValue(x, y, Value):
    plt.figure(figsize=(5, 5), dpi=100)
    X, Y = np.meshgrid(x, y)
    # plt.contourf(X, Y, C[:], cmap="rainbow")
    plt.contour(X, Y, Value, colors='k', linewidths=[2.0])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.show()


def saveC(x, y, t, C):
    plt.figure(figsize=(5, 5), dpi=100)
    X, Y = np.meshgrid(x, y)
    # plt.contourf(X, Y, C[:], cmap="rainbow")
    plt.contour(X, Y, C[:], colors='k', linewidths=[2.0], levels=[0.0])
    plt.title("two-phase interface")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.savefig('%.2fs.png' % t)
    plt.close()
