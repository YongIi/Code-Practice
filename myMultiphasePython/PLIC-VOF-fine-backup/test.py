# 开发人员：leo
# 开发时间：2022/11/16 15:15

a = range(1,5)
print(a)
for i in a:
    print(i)

a = range(1,5)
print(a[0])

import numpy as np

print(np.heaviside(0,0.5))

H1, H2 = 0.0, 0.0
print(H1, H2)

print("---------测试反函数--------")
from pynverse import inversefunc
def calcC(a,b,c,x):
    y = a+b+c+x**2
    return y

"""
inversefunc(partial(calculation_function, prefecture_name="a"))
inversefunc(lambda x: calculation_function(x,"a"))
"""
# calcAlpha = inversefunc(partial(calculation_function, prefecture_name="a"))
calcAlpha = inversefunc(lambda x: calcC(x,1,2,3))

print(calcC(44,1,2,3))
print(calcAlpha(56))

print("--------")
print(max(5.22,5.2222222222222222222))

print(np.arange(5))
print(-np.arange(5))
aa = np.arange(5)
bb = 1 -np.arange(5)*2
print(aa+bb)

print(np.heaviside(6,0.5))

aa = np.arange(-5, 5 ,2)
print(aa)
aa = np.maximum(0.0, aa)
print(aa)

flag = 1
print(flag)
if flag:
    print("成功")

for i in range(3):
    print(1)

C1 = 0.5 * min(nx[j, i], ny[j, i]) / max(nx[j, i], ny[j, i])
C2 = 1.0 - C1

# DAN
