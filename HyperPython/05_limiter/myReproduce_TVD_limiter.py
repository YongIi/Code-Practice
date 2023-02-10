# 开发人员：leo
# 开发时间：2023/2/10 14:25

import matplotlib.pyplot as plt
import numpy as np


def phi(theta, limiter):
    if limiter == 'minmod':
        phi = (1 + np.sign(theta)) / 2. * np.minimum(1, theta)
    elif limiter == 'vanleer':
        phi = (theta + np.abs(theta)) / (1. + np.abs(theta))
    elif limiter == 'MC':
        phi = np.maximum(0, np.minimum((1. + theta) / 2., np.minimum(2., theta)))
    elif limiter == 'superbee':
        phi = np.maximum(0., np.maximum(np.minimum(1., 2. * theta), np.minimum(2., theta)))
    return phi


def pw_limited(x, y, xx, limiter='minmod'):
    "From samples (x,y) generate piecewise-linear function sampled at points xx using Minmod slopes."
    # 查找距离xx最近的x的index，计算出来的closest维度与xx一致
    diff = np.abs(x.reshape(1, -1) - xx.reshape(-1, 1))
    closest = np.argmin(diff, axis=1)

    # 定义中间变量
    forward = np.zeros_like(y)  # forward- and backward-difference slope approximations at point i
    backward = np.zeros_like(y)
    theta = np.zeros_like(y)  # the ratio of the two above

    forward[:-1] = (y[1:] - y[:-1]) / (x[1:] - x[:-1])  # 没有求最后一个点的斜率
    backward[1:] = (y[1:] - y[:-1]) / (x[1:] - x[:-1])  # 没有求第一个点的斜率
    theta[1:-1] = forward[1:-1] / backward[1:-1]  # 求法不包含首位值，首位值为0

    # 求斜率
    sigma = phi(theta, limiter) * backward

    # 插值结果
    # x, y, forward, backward, theta, sigma都是离散点上的值，在调用时需要用[closest]
    yy = y[closest] + sigma[closest] * (xx - x[closest])
    return yy


# parameters
k = 5
x = np.arange(-k + 1, k)
y = np.sin(x / 2.) + 1. + 2. * (x > 0)
xx = np.linspace(-k + 1, k - 1, 1000)
width = 12
size = (width, 4)
fig, ax = plt.subplots(4, 1, figsize=(width, 10))
limiters = ('minmod', 'vanleer', 'superbee', 'MC')
for i, limiter in enumerate(limiters):
    print(i, limiter)
    yy = pw_limited(x, y, xx, limiter=limiter)
    ax[i].plot(xx,yy,'-k',lw=2)
    ax[i].plot(x,y,'or',markersize=10,alpha=0.5)
    ax[i].axis((-4,4,-0.1,4.4))
    ax[i].text(.8,.2,limiter,
               horizontalalignment='center',
               transform=ax[i].transAxes, fontsize=20)
plt.show()
