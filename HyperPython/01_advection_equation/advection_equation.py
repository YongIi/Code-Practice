# 开发人员：leo
# 开发时间：2022/10/31 20:18

# 对流方程（单波方程）及特征值

"""
dq/dt+u*dq/dx = 0
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
# from clawpack.visclaw.JSAnimation import IPython_display

# set up a grid and the initial condition
x = np.linspace(0,1,1000)  # Spatial grid
t = np.linspace(0,1)       # Temporal grid  默认总网格点是50个
a = 1.0                    # Advection speed

def q_0(x):                # Initial condition
    return np.exp(-200.*(x-0.2)**2)

# 解析解及绘图工具
def plot_q(t):
    line.set_data(x, q_0(x - a * t))  # Replace the line plot with the solution at time t
    time_text.set_text(time_template%(t))  # 在动图中添加对时间的显示，%(a, b)可以添加多个参数
    return line, time_text  # 该行貌似可以省略

# postProcessing
fig = plt.figure(figsize=(8, 4))  # Create an empty figure
ax = plt.axes()
ax.grid()  # 显示背景网格
line, = ax.plot([], [], color='r', linewidth=2)  # Create an empty line plot
plt.axis((0, 1, -0.1, 1.1))  # Set the bounds of the plot
time_template = 'time = %.2fs'  # 显示时间的字符串模板
time_text = ax.text(0.03, 0.86, '', transform=ax.transAxes)  # 指定显示时间的位置

anim = animation.FuncAnimation(fig, plot_q, frames=t)  # Animate the solution
anim.save('advection.gif', fps=100)
plt.show()


# characteristics 特征线
"""
These lines are called characteristics; they are the trajectories along which 
solution information is transmitted. The value  is referred to as the characteristic velocity. 
The code below plots some of these characteristics.

When we learn about more complicated conservation laws, we'll see that information still 
travels along characteristics, but those characteristics aren't necessarily straight lines.
"""
fig = plt.figure(figsize=(8,4))
ax  = plt.axes()

for x_0 in np.linspace(0,1,10):  # 画9条特征线
    ax.plot(x,(x-x_0)/a,'-k')
plt.ylim(0,1)
plt.show()