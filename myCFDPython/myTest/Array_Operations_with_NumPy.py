# 开发人员：leo
# 开发时间：2022/10/20 17:16

# Array Operations with NumPy  这种方法也太实用了，我喜欢

import numpy
from datetime import datetime

u = numpy.array((0,1,2,3,4,5))

for i in range(1, len(u)):
    print(u[i]-u[i-1])

# 等价于：
print(u[1:] - u[0:-1])

print(u[1:])
print(u[0:-1])  # [0 1 2 3 4] 同样的，左边是闭区间，右边是开区间

# 测试加速

nx = 3
ny = 3
nt = 100
c = 1
dx = 2 / (nx - 1)
dy = 2 / (ny - 1)
sigma = .2
dt = sigma * dx

x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 2, ny)

# 测试时间
# 第一种方法：嵌套循环
time1 = datetime.now()
u = numpy.ones((ny, nx)) # create a 1xn vector of 1's
un = numpy.ones((ny, nx))
u[int(.5 / dy): int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2

for n in range(nt + 1): ##loop across number of time steps
    un = u.copy()
    row, col = u.shape
    for j in range(1, row):
        for i in range(1, col):
            u[j, i] = (un[j, i] - (c * dt / dx *
                                  (un[j, i] - un[j, i - 1])) -
                                  (c * dt / dy *
                                   (un[j, i] - un[j - 1, i])))
            u[0, :] = 1
            u[-1, :] = 1
            u[:, 0] = 1
            u[:, -1] = 1
print("嵌套循环时间：", datetime.now() - time1)

# 第二种方法：采用矩阵操作，省略循环操作
time2 = datetime.now()
u = numpy.ones((ny, nx))
un = numpy.ones((ny, nx))
u[int(.5 / dy): int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2

for n in range(nt + 1): ##loop across number of time steps
    un = u.copy()
    u[1:, 1:] = (un[1:, 1:] - (c * dt / dx * (un[1:, 1:] - un[1:, 0:-1])) -
                              (c * dt / dy * (un[1:, 1:] - un[0:-1, 1:])))
    u[0, :] = 1
    u[-1, :] = 1
    u[:, 0] = 1
    u[:, -1] = 1
print("矩阵操作时间：", datetime.now() - time2)  # 都太快了，测试不出来