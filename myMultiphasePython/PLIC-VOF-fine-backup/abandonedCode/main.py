# 开发人员：liyong
# 开发时间：2022/11/16 10:04

import numpy as np
# from matplotlib import pyplot as plt
import myplot
import calc_normal_vecter as nxy  # 测试完成后放进重构模块中去

# Control parameters
xmin = 0
xmax = 1
ymin = 0
ymax = 1
m = 100  # number of cells in every direction
dx = (xmax - xmin) / m  # Size of 1 grid cell
dy = (ymax - ymin) / m
t = 0.  # Initial time
T = 0.5  # Final time
dt = 0.8 * dx  # Time step, 0.8是CFL数

# Assign initial conditions
x = np.arange(xmin - dx / 2, xmax + dx / 2 * 3, dx)  # 边界外1个ghost cells
y = np.arange(ymin - dy / 2, ymax + dy / 2 * 3, dy)
# x = np.arange(xmin-3*dx/2, xmax+5*dx/2, dx)  # 边界外2个ghost cells
# y = np.arange(ymin-3*dy/2, ymax+5*dy/2, dy)
print('包含ghost cells的网格数量：', len(x))  # 统计包含ghost cells的网格数量
u = np.zeros((len(y), len(x)))  # len(y)是行数，len(x)列数
v = np.zeros((len(y), len(x)))
C = np.zeros((len(y), len(x)))
# define the circle
R = 0.4
x_center, y_center = 0.5, 0.5
for j in range(0, len(y)):
    for i in range(0, len(x)):
        # 初始化体积分数C
        if (x[i] - x_center) ** 2 + (y[j] - y_center) ** 2 < R ** 2:
            C[j, i] = 1.
        if 0.4 < x[i] < 0.6 and y[j] < 0.7:  # 矩形的左右端点分别是(0.4,0.7)和(0.6,0.7)
            C[j, i] = 0.
        # 初始化速度
        u[j, i] = -2 * np.pi * (y[j] - 0.5)
        v[j, i] = 2 * np.pi * (x[i] - 0.5)


# Plot initial conditions
"""
myplot.plotC(x, y, C)
myplot.plotContour(x,y,C)
myplot.plotU(x, y, u, v)
myplot.plotu(x, y, u, v)
myplot.plotv(x, y, u, v)
"""

# 计算界面的法向量nx与ny  # 测试完成后放进重构模块中去
nx, ny = nxy.calcnxy(dx, dy, C)
print(len(C), len(nx))


"---------以下代码仅用于debug-----------"
"""
# 测试法向矢量的计算
myplot.plotContour(x, y, nx)
myplot.plotContour(x, y, ny)
myplot.plotC(x, y, nx)
myplot.plotC(x, y, ny)
a = np.zeros_like(C)
a[1:-1, 1:-1] = nx[1:-1, 1:-1] ** 2 + ny[1:-1, 1:-1] ** 2
myplot.plotContour(x, y, a)
myplot.plotC(x, y, a)
"""






