# 开发人员：leo
# 开发时间：2022/10/21 22:53

import matplotlib.pyplot as plt
import numpy as np

# 原始坐标 x,y 和对应的状态变量值 a
a=np.linspace(0,100,10000)
T=np.mgrid[0:50:0.5,0:50:0.5]
x=T[0]
y=T[1]
h,w=np.shape(x)

image=np.ones((100,100))

# 将坐标映射到image像素中
for i in range(h):
    for j in range(w):
        i_x=int(np.round(x[i,j]*2))
        i_y=int(np.round(y[i,j]*2))
        image[i_x,i_y]=a[i*h+w-1]
plt.figure()
plt.subplot(111)
extent=(0,200,0,200) #任意设置显示的坐标范围
plt.imshow(image,cmap=plt.cm.rainbow,vmin=min(a),vmax=max(a),extent=extent)
plt.title('$\Omega$')
plt.colorbar()
plt.show()