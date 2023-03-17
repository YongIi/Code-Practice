# 开发人员：leo
# 开发时间：2023/2/13 22:32

# 绘制黎曼问题的特征线，需要给出黎曼问题的左右值以及在df_burgers中给出df/dq

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def df_burgers(q):
    """The derivative of the flux function, here defined for Burger's equation."""

    # return 1.0-2*q
    return q  # 通量计算出来恰好是q


def plot_characteristics(df, ql, qr):
    """Plot the characteristic lines for the initial data of a scalar Riemann problem."""

    fig = plt.figure(figsize=(12, 6))
    ax1 = fig.add_subplot(121)

    dq = np.max([abs(qr - ql), 0.1])
    qmin = np.min([ql, qr])
    qmax = np.max([ql, qr])
    ax1.plot([-1.0, 0.0], [ql, ql], 'b-')
    ax1.plot([0.0, 1.0], [qr, qr], 'g-')
    ax1.set_xbound(-1.0, 1.0)
    ax1.set_ybound(qmin - 0.1 * dq, qmax + 0.1 * dq)
    ax1.set_xlabel(r"$x$")
    ax1.set_ylabel(r"$q(x, t=0)$")

    ax2 = fig.add_subplot(122)

    slope_l = df(ql)
    slope_r = df(qr)
    left_edge = np.min([-1.0, -1.0 - slope_l])
    right_edge = np.max([1.0, 1.0 - slope_r])
    x_start_points_l = np.linspace(left_edge, 0.0, 20)
    x_start_points_r = np.linspace(0.0, right_edge, 20)
    x_end_points_l = x_start_points_l + slope_l
    x_end_points_r = x_start_points_r + slope_r

    for xs, xe in zip(x_start_points_l, x_end_points_l):
        ax2.plot([xs, xe], [0.0, 1.0], 'b-')
    for xs, xe in zip(x_start_points_r, x_end_points_r):
        ax2.plot([xs, xe], [0.0, 1.0], 'g-')

    x_fill = [x_end_points_l[-1], x_start_points_l[-1], x_end_points_r[0]]
    t_fill = [1.0, 0.0, 1.0]
    ax2.fill_between(x_fill, t_fill, 1.0, facecolor='red', alpha=0.5)

    ax2.set_xbound(-1.0, 1.0)
    ax2.set_ybound(0.0, 1.0)
    ax2.set_xlabel(r"$x$")
    ax2.set_ylabel(r"$t$")

    fig.tight_layout()
    plt.show()

plot_characteristics(df_burgers, 0.1, -0.2)  # 根据左右值的不同，特征线交叉出现激波
plot_characteristics(df_burgers, -0.1, 0.2)  # 根据左右值的不同，特征线分散出现稀疏波

"""以下模块包安装不上
from ipywidgets import interactive, FloatSlider
def interactive_characteristics(ql, qr):
    return plot_characteristics(df_burgers, ql, qr)
interactive(interactive_characteristics,
            ql = FloatSlider(min=-2.0, max=2.0, step=0.1, value=-0.1),
            qr = FloatSlider(min=-2.0, max=2.0, step=0.1, value=0.2))
"""

