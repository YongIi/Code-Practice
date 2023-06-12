# 开发人员：leo
# 开发时间：2023/4/7 10:35

import matplotlib.pyplot as plt
import numpy as np

hl = np.linspace(0.1, 10.1)
ul = np.linspace(-1.0, 1.0)
HL, UL = np.meshgrid(hl, ul)
XIL = UL - np.sqrt(HL)
xi_min = np.min(XIL)
xi_max = np.max(XIL)
h_min = np.min(hl)
h_max = np.max(hl)
u_min = np.min(ul)
u_max = np.max(ul)
xi = np.linspace(xi_min, xi_max)


def plot_sw_rarefaction(hl, ul):
    "Plot the rarefaction curve through the state (hl, ul)"

    xil = ul - np.sqrt(hl)
    h = ((xil - xi) / 3.0 + np.sqrt(hl)) ** 2
    u = 2.0 * (xi - xil) / 3.0 + ul

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111)
    ax.plot(hl, ul, 'rx', markersize=16, markeredgewidth=3)
    ax.plot(h, u, 'k--', linewidth=2)
    ax.set_xlabel(r"$h$")
    ax.set_ylabel(r"$u$")
    dh = h_max - h_min
    du = u_max - u_min
    ax.set_xbound(h_min - 0.1 * dh, h_max + 0.1 * dh)
    ax.set_ybound(u_min - 0.1 * du, u_max + 0.1 * du)
    fig.tight_layout()
    plt.show()

plot_sw_rarefaction(5.0, 1.0)