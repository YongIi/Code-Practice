# 开发人员：leo
# 开发时间：2023/2/9 22:22

import matplotlib.pyplot as plt
import numpy as np

def phi(theta, limiter):
    if limiter == 'minmod':
        phi = (1 + np.sign(theta)) / 2. * np.minimum(1, theta)
    elif limiter == 'vanleer':
        phi = (theta + np.abs(theta)) / (1 + np.abs(theta))
    elif limiter == 'MC':
        phi = np.maximum(0, np.minimum((1. + theta) / 2., np.minimum(2., theta)))
    elif limiter == 'superbee':
        phi = np.maximum(0, np.maximum(np.minimum(1., 2 * theta), np.minimum(2., theta)))
    return phi


def pw_limited(x, y, xx, limiter='minmod'):
    "From samples (x,y) generate piecewise-linear function sampled at points xx using Minmod slopes."
    diff = np.abs(x.reshape(1, -1) - xx.reshape(-1, 1))
    closest = np.argmin(diff, axis=1)

    forward = np.zeros_like(y)
    backward = np.zeros_like(y)
    theta = np.zeros_like(y)

    forward[:-1] = (y[1:] - y[:-1]) / (x[1:] - x[:-1])
    backward[1:] = (y[1:] - y[:-1]) / (x[1:] - x[:-1])
    theta[1:-1] = forward[1:-1] / backward[1:-1]

    sigma = phi(theta, limiter) * backward

    return y[closest] + sigma[closest] * (xx - x[closest])

k = 5
x = np.arange(-k+1,k)
y = np.sin(x/2.)+1. + 2.*(x>0)
xx = np.linspace(-k+1,k-1,1000)
width = 12
size = (width, 4)
fig, ax = plt.subplots(4,1,figsize=(width,10))
for i, limiter in enumerate( ('minmod', 'vanleer','superbee','MC') ):
    yy = pw_limited(x,y,xx,limiter=limiter)
    ax[i].plot(xx,yy,'-k',lw=2)
    ax[i].plot(x,y,'or',markersize=10,alpha=0.5)
    ax[i].axis( (-4,4,-0.1,4.4) );
    ax[i].text(.8,.2,limiter,
        horizontalalignment='center',
        transform=ax[i].transAxes,fontsize=20)
plt.show()
