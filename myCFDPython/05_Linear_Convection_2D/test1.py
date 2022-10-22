# 开发人员：leo
# 开发时间：2022/10/21 22:50

import matplotlib.pyplot as plt
import numpy as np
a=np.linspace(0,100,10000)
T=np.mgrid[0:100:1,0:100:1]
x=T[0]
y=T[1]

plt.figure()
plt.subplot(111)
plt.scatter(x,y,c=a,cmap=plt.cm.rainbow,vmin=min(a),vmax=max(a))
plt.text(50,50,r'Nancy',{'color':'r','fontsize':20})
plt.title('$\Omega$')
plt.colorbar()
plt.show()
