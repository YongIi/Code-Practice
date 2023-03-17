# 开发人员：leo
# 开发时间：2023/2/13 22:32

# 绘制Buckley-Leverett problem的复合波，需要给出黎曼问题的左右值

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def flux_buckley_leverett(q):
    return q ** 2 / (q ** 2 + a * (1.0 - q) ** 2)


def df_buckley_leverett(q):
    return 2.0 * a * q * (1.0 - q) / (q ** 2 + a * (1.0 - q) ** 2)


fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)

a = 0.5
ql = 1.0
qr = 0.0
qs = np.sqrt(a / (1.0 + a))
s = df_buckley_leverett(qs)  # Shock speed matches characteristic speed on left!

slope_l = df_buckley_leverett(ql)
slope_r = df_buckley_leverett(qr)

left_edge = np.min([-1.0, -1.0 - slope_l])
right_edge = np.max([1.0, 1.0 - slope_r])
x_start_points_l = np.linspace(left_edge, 0.0, 20)
x_start_points_r = np.linspace(0.0, right_edge, 20)
x_end_points_l = x_start_points_l + slope_l
x_end_points_r = x_start_points_r + slope_r

# Rarefaction wave
xi_l = df_buckley_leverett(ql)
xi_r = df_buckley_leverett(qs)
xi = np.linspace(xi_l, xi_r, 7)
x_end_rarefaction = xi

# Shock intersections
t_end_points_r = np.ones_like(x_start_points_r)
t_end_points_r = np.minimum(t_end_points_r, x_start_points_r / (s - slope_r))

for xs, xe in zip(x_start_points_l, x_end_points_l):
    ax.plot([xs, xe], [0.0, 1.0], 'b-')
for xs, xe, te in zip(x_start_points_r, x_end_points_r, t_end_points_r):
    ax.plot([xs, xe], [0.0, te], 'g-')
for xe in x_end_rarefaction:
    ax.plot([0.0, xe], [0.0, 1.0], 'r--')
# Shock
ax.plot([0.0, s], [0.0, 1.0], 'k-', linewidth=3)

ax.set_xbound(-1.0, 1.0)
ax.set_ybound(0.0, 1.0)
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$t$")

fig.tight_layout()
plt.show()

