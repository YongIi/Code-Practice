# 开发人员：leo
# 开发时间：2022/10/30 17:39

import math
import numpy as np
import matplotlib.pyplot as plt

# print(dir(math))
print(math.sqrt(2))  # the math module versions operate only on scalars，矩阵操作不能用math，要用numpy

x = np.linspace(0, 1, 5)  # 右闭区间，包括最右
print(x)

y = np.arange(0, 1, 0.2)  # 右开区间，不包括最右
print(y)

print(x + y)
print(x * y)

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A)

x = np.linspace(0, 4, 1000)
f = np.sin(np.exp(x))
plt.plot(x, f)
plt.show()

print(1 / 2)
print(1.0 / 2.0)

# define the cylinder of untit radius centered at (0, 0)
R = 1.0
x_center, y_center = 0.0, 0.0
theta = np.linspace(0.0, 2 * math.pi, 100)
x_cylinder, y_cylinder = (x_center + R * np.cos(theta),
                          y_center + R * np.sin(theta))

# plot the cylinder
size = 4
plt.figure(figsize=(size, size))
plt.grid()
plt.xlabel('x', fontsize=16)
plt.ylabel('y', fontsize=16)
plt.plot(x_cylinder, y_cylinder, color='b', linestyle='-', linewidth=2)
plt.xlim(-1.1, 1.1)
plt.ylim(-1.1, 1.1)
plt.show()
