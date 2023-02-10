# 开发人员：leo
# 开发时间：2023/2/9 16:35

import numpy as np

a=np.arange(3)
print(a)

b=a.reshape(1,-1)
print(b)

c=a.reshape(-1,1)
print(c)

d = np.abs(b-c)
print(d)