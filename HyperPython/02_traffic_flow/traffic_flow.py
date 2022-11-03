# 开发人员：leo
# 开发时间：2022/11/3 16:14

import matplotlib.pyplot as plt
import numpy as np

q = np.linspace(0, 1)  # 右闭区间，默认共50个点
f = q * (1. - q)
plt.plot(q, f, lw=2, color='k')
plt.xlabel('q')
plt.ylabel("flux")
plt.xlim(0, 1)
plt.ylim(0, 0.25)
plt.show()
