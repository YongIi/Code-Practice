# 开发人员：leo
# 开发时间：2023/2/10 14:55
import matplotlib.pyplot as plt
import numpy as np

k = 5
x = np.arange(-k+1, k)
y = np.sin(x/2.)+1.+2.*(x>0)
xx = np.arange(-k+1+0.2, k+0.2)
diff = np.abs(x.reshape(1,-1)-xx.reshape(-1,1))
closest = np.argmin(diff, axis =1)
print(diff)
print(closest)

a = [1,2,3,4,5,6,7,8,9]
print(a[:-1])  # 不包括最右边