# 开发人员：leo
# 开发时间：2023/2/9 21:37

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

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

k = 5
x = np.arange(-k+1,k)
y = np.sin(x/2.)+1.
y = np.exp(x/3.)
xx = np.linspace(-k+1,k-1,1000)
yy = pw_minmod(x,y,xx)
width = 12
size = (width, 4)
plt.figure(figsize=(width,6))
plt.plot(xx,yy,'-k',lw=2)
plt.plot(x,y,'or',markersize=10,alpha=0.5)
plt.axis( (-4,4,-0.1,4.1) );
plt.title('minmod approximation',fontsize=20);
for i in range(len(y)-1):
    if 1<=i<len(y):
        x_avgs = [(x[i]+x[i-1])/2.,(x[i]+x[i+1])/2.]
        y_avgs = [(y[i]+y[i-1])/2.,(y[i]+y[i+1])/2.]
        currentAxis = plt.gca()
        currentAxis.add_patch(Rectangle((x_avgs[0], y_avgs[0]),
                                         x_avgs[1]-x_avgs[0], y_avgs[1]-y_avgs[0],
                                         facecolor="grey",alpha=0.5))
plt.show()