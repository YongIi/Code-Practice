# 开发人员：leo
# 开发时间：2022/11/1 9:17

import numpy as np
import matplotlib.pyplot as plt

a = 1.0  # advection speed

m = 1000  # number of cells
dx = 1. / m  # Size of 1 grid cell
x = np.arange(-dx / 2, 1. + dx / 2, dx)  # Cell centers, including ghost cells # 注意arange是右开区间，故最右边只到最后一个网格中心，即最右边没有ghost cell
print(x)  # 注意arange是右开区间，故最右边只到最后一个网格中心，即最右边没有ghost cell，如需在最右端设置ghost cell，需要给1. + dx / 2乘以2
print(len(x))  # 统计包含ghost cells的网格数量
"""
Notice how we set up a grid that contains an extra cell at each end, outside of the problem domain[0, 1]. 
These are called ghost cells and are often useful in handling the solution at the grid boundaries.
"""

t = 0.  # Initial time
T = 0.5  # Final time
dt = 0.8 * dx / a  # Time step  # 0.8是CFL数

Q = np.exp(-200 * (x - 0.2) ** 2)  # Initial data
Qnew = np.empty(Q.shape)

while t < T:
    # Extrapolation at boundaries: 边界外推，向ghost cells网格中给入值
    Qnew[0] = Q[1]
    Qnew[-1] = Q[-2]  # 右边不是没有ghost cells网格吗？
    """
    The technique we have used to set the ghost cell values above, by copying the last value 
    inside the grid to the ghost cells, is known as zero-order extrapolation. It is useful for 
    allowing waves to pass out of the domain (so-called non-reflecting boundaries). Note that 
    we don't actually need the ghost cell at the right end for the upwind method, but for other methods we will.
    """

    """
    for i in range(1, len(x)):
        Qnew[i] = Q[i] - a * dt / dx * (Q[i] - Q[i - 1])
    """

    Qnew[1:] = Q[1:] - a * dt / dx * (Q[1:] - Q[0: -1])

    Q = Qnew.copy()
    t = t + dt

plt.plot(x, Q, linewidth=2)
# plt.title('t = ' + str(t))
plt.title('t = ' + '%.3fs' % (t))
plt.show()
