# 开发人员：liyong
# 开发时间：2022/12/01 11:04

import math
import numpy as np
import myplot
import interface_propagation as propagation
import re_init as re

# Control parameters
xmin = 0
xmax = 1
ymin = 0
ymax = 1
m = 100  # number of cells in every direction
dx = (xmax - xmin) / m  # Size of 1 grid cell
dy = (ymax - ymin) / m
t = 0.  # Initial time
T = 4.0 # Final time
CFL = 0.01  # CFL数
dt = CFL * dx  # Time step
print("dt=", dt)
count = 0  # 统计迭代次数
interval = 200  # re-init间隔的时间步
nt = 5  # re-init时迭代步数
t1 = 2.0  # 速度反号时间2.0
# savet = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]  # 指定需要保存图片的时间
# savet = [0.5, 1.0, 1.5, 2.0]

# Assign initial conditions
# x = np.arange(xmin - dx / 2, xmax + dx / 2 * 3, dx)  # 边界外1个ghost cells
# y = np.arange(ymin - dy / 2, ymax + dy / 2 * 3, dy)
x = np.arange(xmin-3*dx/2, xmax+5*dx/2, dx)  # 边界外2个ghost cells
y = np.arange(ymin-3*dy/2, ymax+5*dy/2, dy)
print('包含ghost cells的网格数量：', len(x))  # 统计包含ghost cells的网格数量
u = np.zeros((len(y), len(x)))  # len(y)是行数，len(x)列数 在速度发生变化的流场中采用
v = np.zeros((len(y), len(x)))
phi = np.zeros((len(y), len(x)))
# define the circle
R = 0.25
x_center, y_center = 0.5, 0.3
for j in range(0, len(y)):
    for i in range(0, len(x)):
        # 初始化符号距离函数phi
        phi[j, i] = math.sqrt((x[i] - x_center) ** 2 + (y[j] - y_center) ** 2) - R
        # 初始化速度
        u[j, i] = -2 * math.pi * math.cos(math.pi * (x[i] - 0.5)) * math.sin(math.pi * (y[j] - 0.5))
        # u[j, i] = 1.0
        v[j, i] = 2 * math.pi * math.sin(math.pi * (x[i] - 0.5)) * math.cos(math.pi * (y[j] - 0.5))
        # v[j, i] = 1.0

# Plot initial conditions
# myplot.plotC(x, y, phi)
# myplot.plotContour(x, y, phi)
# myplot.plotU(x, y, u, v)
# myplot.plotu(x, y, u, v)
# myplot.plotv(x, y, u, v)

while t < T:
    # Modify the code so that the last step is adjusted to exactly reach T
    if t + dt > T:
        dt = T - t

    if count == int(t1/dt+1):
        print("速度反号，反号时间：{0}，反号前迭代了：{1}".format(t,count))
        u = -1*u
        v = -1*v

    # 界面推进
    phi = propagation.calcPhi(x,y,dx,dy,dt,u,v,phi)

    # Re-init
    if (count+1) % interval == 0:
        print("开始Re-init，此时迭代步为：{0}".format(count))
        phi = re.reinit(x, y, dx, dy, dt, nt, phi)

    count += 1
    t = t + dt
    print("总时间{0}，目前时间{1}".format(T, t))

    # 选择合适的图片保存方式，方式一：指定时间保存
    # for i in range(len(savet)):  # 在savet指定的时间下保存图片
    #     if count == int(savet[i]/dt):
    #         myplot.saveC(x, y, t, phi)

    # 选择合适的图片保存方式，方式二：间隔保存图片，方便制成动图
    if count % 100 == 0:
        myplot.saveC(x, y, t, phi)
        # myplot.saveContour(x, y, t, phi)

print("总共迭代了：{0}次".format(count))
# 后处理
myplot.plotC(x, y, phi)
myplot.plotContour(x, y, phi)
#myplot.plotU(x, y, u, v)  # 查看反向后的速度
#myplot.plotu(x, y, u, v)
#myplot.plotv(x, y, u, v)
