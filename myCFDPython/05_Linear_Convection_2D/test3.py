# 开发人员：leo
# 开发时间：2022/10/21 22:56

import numpy as np
def func_array(x1,x2):
    f = 0.5 * x1 ** 2 + 1 * x2 ** 2
    return f

x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)
x1,y1 = np.meshgrid(x,y)
z = func_array(x1,y1)

import matplotlib.pyplot as plt
plt.figure()
plt.contourf(x1,y1,z,20,cmap="afmhot_r",alpha=0.5)
plt.show()

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(x1, y1, z, cmap='rainbow',linewidth=0, antialiased=False)
#ax.zaxis.set_major_locator(LinearLocator(5))
ax.zaxis.set_major_formatter('{x:.0f}')
ax.set_zlim(0, 150)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('z')
plt.show()

