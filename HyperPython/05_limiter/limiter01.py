# 开发人员：leo
# 开发时间：2023/2/8 21:07

import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.rcParams.update({'font.size': 22})

k = 5
x = np.arange(-k+1,k)
y = np.sin(x/2.)+1.
width = 12
size = (width, 4)
plt.figure(figsize=size)
plt.plot(x,y,'or',markersize=10, alpha=0.5)  # alpha是透明度
plt.axis((-k,k,-0.1,2.1))
plt.show()

# 分段常数插值
def piecewise_constant_interp(x,y,xx):  # (x,y)是已知的离散点，x扩大到xx，并对y进行插值
    #From samples (x,y) generate piecewise constant function sampled at points xx.
    diff = np.abs(x.reshape(1,-1)-xx.reshape(-1,1))  # ??????
    closest = np.argmin(diff, axis=1)
    return y[closest]

xx = np.linspace(-k+1,k-1,1000)
yy = piecewise_constant_interp(x,y,xx)
plt.figure(figsize=size)
plt.plot(xx,yy,'-k',lw=2)
plt.plot(x,y,'or',markersize=10,alpha=0.5)
plt.axis( (-k, k, -0.1, 2.1) )
plt.title('Piecewise-constant approximation',fontsize=20)
plt.show()


def piecewise_linear_interp(x, y, xx, fd='centered'):
    "From samples (x,y) generate piecewise-linear function sampled at points xx using finite difference slopes."
    diff = np.abs(x.reshape(1, -1) - xx.reshape(-1, 1))
    closest = np.argmin(diff, axis=1)

    sigma = np.zeros_like(y)
    if fd == 'centered':
        sigma[1:-1] = (y[2:] - y[:-2]) / (x[2:] - x[:-2])
    elif fd == 'forward':
        sigma[:-1] = (y[1:] - y[:-1]) / (x[1:] - x[:-1])
    elif fd == 'backward':
        sigma[1:] = (y[1:] - y[:-1]) / (x[1:] - x[:-1])
    return y[closest] + sigma[closest] * (xx - x[closest])  # 斜率法重构守恒量，插值出网格界面上的值


def compare_fd(x, y, xx, axis=(-4, 4, -0.1, 2.1)):
    fig, ax = plt.subplots(3, 1, figsize=(width, 8))
    for i, fd in enumerate(('centered', 'forward', 'backward')):
        yy = piecewise_linear_interp(x, y, xx, fd=fd)
        ax[i].plot(xx, yy, '-k', lw=2)
        ax[i].plot(x, y, 'or', markersize=10, alpha=0.5)
        ax[i].axis(axis);
        ax[i].text(.5, .9, fd,
                   horizontalalignment='center',
                   transform=ax[i].transAxes, fontsize=20)
    plt.show()


compare_fd(x, y, xx)

# 对比间断数据
x1 = np.arange(-k+1,k,0.1)
y1 = np.sin(x1/2.)+1. + 2.*(x1>0)
y2 = np.sin(x/2.)+1. + 2.*(x>0)

plt.figure(figsize=size)
plt.plot(x1,y1,'or',markersize=10, alpha=0.5)  # alpha是透明度
plt.axis((-k,k,-0.1,5.1))
plt.show()

compare_fd(x,y2,xx,axis=(-4,4,-0.5,4.8))


def pw_minmod(x, y, xx):
    "From samples (x,y) generate piecewise-linear function sampled at points xx using Minmod slopes."
    diff = np.abs(x.reshape(1, -1) - xx.reshape(-1, 1))
    closest = np.argmin(diff, axis=1)

    forward = np.zeros_like(y)
    backward = np.zeros_like(y)
    sigma = np.zeros_like(y)

    forward[:-1] = (y[1:] - y[:-1]) / (x[1:] - x[:-1])
    backward[1:] = (y[1:] - y[:-1]) / (x[1:] - x[:-1])

    sigma = (np.sign(forward) + np.sign(backward)) / 2. * np.minimum(np.abs(forward), np.abs(backward))  # 确保当样本数据是极值点时，该处的斜率为0

    return y[closest] + sigma[closest] * (xx - x[closest])

yy = pw_minmod(x,y,xx)
plt.figure(figsize=size)
plt.plot(xx,yy,'-k',lw=2)
plt.plot(x,y,'or',markersize=10,alpha=0.5)
plt.axis( (-4,4,-0.5,4.8) );
plt.title('Minmod approximation',fontsize=20)
plt.show()