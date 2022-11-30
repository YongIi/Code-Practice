# 开发人员：liyong
# 开发时间：2022/11/16 10:04

import numpy as np
# from matplotlib import pyplot as plt
import myplot
import calc_normal_vecter as nxy
import interface_reconstruction as reconstruction
import interface_propagation as propagation


# Control parameters
xmin = 0
xmax = 1
ymin = 0
ymax = 1
m = 100  # number of cells in every direction
dx = (xmax - xmin) / m  # Size of 1 grid cell
dy = (ymax - ymin) / m
t = 0.  # Initial time
T = 2.0  # Final time
CFL = 0.5  # CFL数
dt = CFL * dx  # Time step

# Assign initial conditions
x = np.arange(xmin - dx / 2, xmax + dx / 2 * 3, dx)  # 边界外1个ghost cells
y = np.arange(ymin - dy / 2, ymax + dy / 2 * 3, dy)
# x = np.arange(xmin-3*dx/2, xmax+5*dx/2, dx)  # 边界外2个ghost cells
# y = np.arange(ymin-3*dy/2, ymax+5*dy/2, dy)
print('包含ghost cells的网格数量：', len(x))  # 统计包含ghost cells的网格数量
# u = np.zeros((len(y), len(x)))  # len(y)是行数，len(x)列数 在速度发生变化的流场中采用
# v = np.zeros((len(y), len(x)))
u = 1.0
v = -0.5
C = np.zeros((len(y), len(x)))
# 数组切片后没有生成新的数组，因为切片是右开区间，所以要加上1， # index = (x+dx/2)/dx
C[int((0.55 + dy / 2) / dy):int((0.95 + dy / 2) / dy + 1), int((0.05 + dx / 2) / dx):int((0.45 + dx / 2) / dx + 1)] = 1
C[int((0.65 + dy / 2) / dy):int((0.85 + dy / 2) / dy + 1), int((0.15 + dx / 2) / dx):int((0.35 + dx / 2) / dx + 1)] = 0

# Plot initial conditions
# myplot.plotC(x, y, C)
myplot.plotContour(x,y,C)

while t < T:
    # Modify the code so that the last step is adjusted to exactly reach T
    if t + dt > T:
        dt = T - t

    # 计算界面的法向量nx与ny
    nx, ny = nxy.calcnxy(dx, dy, C)
    #print(len(C), len(nx))  # 测试后删除
    #myplot.plotValue(x,y,nx)

    # interface reconstruction 求出alhpa
    alpha = reconstruction.calcAlpha(x, y, dx, dy, C, nx, ny)
    #print("alpha的尺度是", len(alpha))
    #myplot.plotValue(x,y,alpha)

    # interface propagation 求出下一时刻的C
    # 沿x方向求出Cstar
    nx, ny = nxy.calcnxy(dx, dy, C)
    #Cstar = propagation.calcCstar(nx, ny, u, v, dt, dx, dy, alpha, x, y, C)
    # myplot.plotValue(x,y,Cstar)
    #myplot.plotContour(x,y,Cstar)

    # 沿y方向求出下一时刻C
    #nx, ny = nxy.calcnxy(dx, dy, Cstar)
    #nx, ny = nxy.calcnxy(dx, dy, C)
    #alpha = reconstruction.calcAlpha(x, y, dx, dy, Cstar, nx, ny) # 注释拿掉
    #nx, ny = nxy.calcnxy(dx, dy, C)
    C_nplus1 = propagation.calcC_nplus1(nx, ny, u, v, dt, dx, dy, alpha, x, y, C) #Cstar改为C

    C = C_nplus1.copy()
    #C = Cstar.copy()  # 用于测试
    t = t + dt

# 后处理
myplot.plotContour(x,y,C)
#myplot.plotC(x,y,C)












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
