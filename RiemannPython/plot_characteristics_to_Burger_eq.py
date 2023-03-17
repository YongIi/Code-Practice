# 开发人员：leo
# 开发时间：2023/2/13 22:32

# 绘制Burger方程的特征线图，根据左右初值给的不同，得到不同的激波或是稀疏波

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def plot_solution_burgers(ql, qr):
    """Plot the characteristic lines for the full solution to Burger's equation."""

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

    if (ql <= qr):
        # Rarefaction case

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

    else:
        # Shock case
        s = 0.5 * (qr + ql)
        ax2.plot([0.0, s], [0.0, 1.0], 'k-', linewidth=3)

        left_edge = np.min([-1.0, -1.0 - slope_l])
        right_edge = np.max([1.0, 1.0 - slope_r])
        x_start_points_l = np.linspace(left_edge, 0.0, 20)
        x_start_points_r = np.linspace(0.0, right_edge, 20)
        t_end_points_l = np.ones_like(x_start_points_l)
        t_end_points_r = np.ones_like(x_start_points_r)

        # Look for intersections
        t_end_points_l = np.minimum(t_end_points_l, x_start_points_l / (s - slope_l))
        t_end_points_r = np.minimum(t_end_points_r, x_start_points_r / (s - slope_r))
        x_end_points_l = x_start_points_l + slope_l * t_end_points_l
        x_end_points_r = x_start_points_r + slope_r * t_end_points_r

        for xs, xe, te in zip(x_start_points_l, x_end_points_l, t_end_points_l):
            ax2.plot([xs, xe], [0.0, te], 'b-')
        for xs, xe, te in zip(x_start_points_r, x_end_points_r, t_end_points_r):
            ax2.plot([xs, xe], [0.0, te], 'g-')

    ax2.set_xbound(-1.0, 1.0)
    ax2.set_ybound(0.0, 1.0)
    ax2.set_xlabel(r"$x$")
    ax2.set_ylabel(r"$t$")

    fig.tight_layout()

    plt.show()


plot_solution_burgers(-0.5, 1.5)
