# 开发人员：leo
# 开发时间：2022/11/4 16:30

"""
以往我自己设置的ghost cells坐标x是存在问题的

激波前后不应该有凹陷和突起（激烈的震荡），为此需要构造非线性格式
"""

import sys
import numpy as np
sys.path.append('../util')
from myianimate import ianimate


def f(q):  # 定义通量
    return q * (1.0 - q)

# Control parameters
m = 100     # number of points
dx = 1./m   # Size of 1 grid cell
x = np.arange(-3*dx/2, 1.+5*dx/2, dx)  # Cell centers, including ghost cells # 注意arange是右开区间，一个step是dx，故最右边比最左边多2*dx/2
print(len(x))  # 统计包含ghost cells的网格数量
t = 0. # Initial time
T = 0.5 # Final time
dt = 0.9 * dx  # Time step


# Assign initial conditions
Q = 0.9*np.exp(-100*(x-0.5)**2)
# Qnew = np.empty(Q.shape)
Qnew = np.zeros(Q.shape)
Qstar = np.zeros(Q.shape)
sigma = np.zeros(Q.shape)   #  the slope using centered approximation
F = np.zeros(Q.shape)  # 数值通量
lst_anim = [Q]  # 创建一个列表用来存储所有时间的解

# Numerical solution - FVM
while t < T:
    # Modify the code so that the last step is adjusted to exactly reach T
    if t + dt > T:
        dt = T - t

    sigma[1:-1] = (Q[2:] - Q[:-2]) / (2.0 * dx)
    qplus = Q[1:-1] - sigma[1:-1] * dx / 2.0  # q^+_{i-1/2}
    qminus = Q[:-2] + sigma[:-2] * dx / 2.0  # q^-_{i-1/2}
    F[1:-1] = 0.5 * (f(qplus) + f(qminus) - dx / dt * (qplus - qminus))  # F_{i-1/2}

    Qstar[2:-2] = Q[2:-2] - dt / dx * (F[3:-1] - F[2:-2])
    Qstar[0:2] = Qstar[2]
    Qstar[-2:] = Qstar[-3]

    sigma[1:-1] = (Qstar[2:] - Qstar[:-2]) / (2.0 * dx)
    qplus = Qstar[1:-1] - sigma[1:-1] * dx / 2.0  # q^+_{i-1/2}
    qminus = Qstar[:-2] + sigma[:-2] * dx / 2.0  # q^-_{i-1/2}
    F[1:-1] = 0.5 * (f(qplus) + f(qminus) - dx / dt * (qplus - qminus))  # F_{i-1/2}

    Qnew[2:-2] = 0.5 * Q[2:-2] + 0.5 * (Qstar[2:-2] - dt / dx * (F[3:-1] - F[2:-2]))

    Q = Qnew.copy()
    Q[0:2] = Q[2]
    Q[-2:] = Q[-3]
    t = t + dt
    lst_anim.append(Q)

print(len(sigma))
# postProcessing
ianimate(x, lst_anim)






