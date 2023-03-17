# 开发人员：leo
# 开发时间：2023/2/13 22:32

# 绘制Burger方程稀疏波的特征线，需要给出黎曼问题的左右值
# 其实可以根据不同的激波速度s，求不同的激波

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def plot_rarefaction_burgers(ql, qr):
    """Plot the characteristic lines for the rarefaction solution to Burger's equation."""

    assert (ql < qr)

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

    slope_l = ql
    slope_r = qr

    left_edge = np.min([-1.0, -1.0 - slope_l])
    right_edge = np.max([1.0, 1.0 - slope_r])
    x_start_points_l = np.linspace(left_edge, 0.0, 20)
    x_start_points_r = np.linspace(0.0, right_edge, 20)
    x_end_points_l = x_start_points_l + slope_l
    x_end_points_r = x_start_points_r + slope_r

    # Rarefaction wave
    xi_l = ql
    xi_r = qr
    xi = np.linspace(xi_l, xi_r, 7)
    x_end_rarefaction = xi

    for xs, xe in zip(x_start_points_l, x_end_points_l):
        ax2.plot([xs, xe], [0.0, 1.0], 'b-')
    for xs, xe in zip(x_start_points_r, x_end_points_r):
        ax2.plot([xs, xe], [0.0, 1.0], 'g-')
    for xe in x_end_rarefaction:
        ax2.plot([0.0, xe], [0.0, 1.0], 'r--')

    ax2.set_xbound(-1.0, 1.0)
    ax2.set_ybound(0.0, 1.0)
    ax2.set_xlabel(r"$x$")
    ax2.set_ylabel(r"$t$")

    fig.tight_layout()
    plt.show()


plot_rarefaction_burgers(-0.5, 0.5)
