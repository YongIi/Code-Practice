# 开发人员：leo
# 开发时间：2022/11/1 9:17

# traffic flow

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


m = 500  # number of cells
dx = 1. / m  # Size of 1 grid cell
x = np.arange(-dx / 2, 1. + dx / 2 * 2, dx)  # Cell centers, including ghost cells # 注意arange是右开区间，故最右边只到最后一个网格中心，即最右边没有ghost cell
print(x)  # 注意arange是右开区间，故最右边只到最后一个网格中心，即最右边没有ghost cell，如需在最右端设置ghost cell，需要给1. + dx / 2乘以2
print(len(x))  # 统计包含ghost cells的网格数量
"""
Notice how we set up a grid that contains an extra cell at each end, outside of the problem domain[0, 1]. 
These are called ghost cells and are often useful in handling the solution at the grid boundaries.
"""

t = 0.  # Initial time
T = 2  # Final time
# CFL = 0.8
dt = 0.9 * dx  # Time step  # 0.8是CFL数



Q = 0.9*np.exp(-100*(x-0.5)**2)  # Initial data
Qnew = np.empty(Q.shape)
lst_anim = [Q]  # 创建一个列表用来存储所有时间的解

# FVM -  the Lax-Friedrichs method
while t < T:
    # Modify the code so that the last step is adjusted to exactly reach T
    if t + dt > T:
        dt = T - t

    Qnew[1:-1] = 0.5 * (Q[:-2] + Q[2:]) - 0.5 * dt / dx * (Q[2:] * (1 - Q[2:]) - Q[:-2] * (1 - Q[:-2]))

    # 更新边界条件
    # 周期性边界条件
    Qnew[0] = Qnew[-2]
    Qnew[-1] = Qnew[1]
    """
    The technique we have used to set the ghost cell values above.
    """

    Q = Qnew.copy()
    lst_anim.append(Q)  # accumulate frames of the solution in a list
    t = t + dt  # 本次迭代完后得到的实际时间
    #print("t =", t)


# postProcessing
# plt.plot(x, Qexact,label="exact solution", linestyle='-', color='k', linewidth=2)
plt.plot(x, Q, label="The Lax-Friedrichs method with {0} grids".format(m), linestyle='-', color='r', linewidth=2)
plt.title('t = ' + str(t))
#plt.title('t = ' + '%.3fs' % (t))
plt.legend()
plt.show()

# animation
fig = plt.figure(figsize=(8, 4))  # Create an empty figure
ax = plt.axes()
ax.grid()  # 显示背景网格
line, = ax.plot([], [], color='r', linewidth=2)  # Create an empty line plot
plt.axis((0, 1, -0.1, 1.1))  # Set the bounds of the plot
time_template = 'time = %.2fs'  # 显示时间的字符串模板
time_text = ax.text(0.03, 0.86, '', transform=ax.transAxes)  # 指定显示时间的位置

def plot_q(i):
    line.set_data(x, lst_anim[i])  # Replace the line plot with the solution at time t
    time_text.set_text(time_template % (i*dt))  # 在动图中添加对时间的显示，%(a, b)可以添加多个参数

anim = animation.FuncAnimation(fig, plot_q, frames=range(0,len(lst_anim),10))  # frames是帧数，数量太多了需要间隔来取，但因为是右开区间，最后一些帧数可能没包含进来
anim.save('traffic flow with Lax-Friedrichs method.gif', fps=100)
plt.show()

