# 开发人员：leo
# 开发时间：2022/11/16 15:57

# 重构界面，利用C与nx, ny计算出线段nx*x+ny*y=alpha的alpha值

import numpy as np
import calc_normal_vecter as nxy
import math

# 定义一个依据alpha求C的函数，其中np.heaviside(alpha-nx*dx,0.0)第二个参数的意思是当第一个参数等于0时，取第二参数的值
def calcC(alpha, dx, dy, nx, ny):  # 传参时传入nx[j, i]，alpha[j, i]
    C = alpha**2/(2*nx*ny)*(1-np.heaviside(alpha-nx*dx,0.0)*((alpha-nx*dx)/alpha)**2 \
                             -np.heaviside(alpha-ny*dy,0.0)*((alpha-ny*dy)/alpha)**2)/(dx*dy)
    return C

def calcAlpha(x, y, dx, dy, C):
    # 定义中间变量
    alpha = np.zeros_like(C)
    minima = 0.000000000001

    # 计算界面的法向量nx与ny
    nx, ny = nxy.calcnxy(dx, dy, C)
    print(len(C), len(nx))  # 测试后删除

    # 计算每个网格的alpha值
    for j in range(0, len(y)):
        for i in range(0, len(x)):
            # 当法向量不是在第一象限时，将向量投影在第一象限
            # 为了保证方程不变，当存在nx或ny变号时，更改相应的u或v，即u*nx=(-u)*(-nx)
            if nx[j, i] < 0:
                nx[j, i] = -nx[j, i]
                # u = -u
            if ny[j, i] < 0:
                ny[j, i] = -ny[j, i]
                # v = -v      # u和v的变号啥时候用到？？？？？？？？？？

            # 如何处理nx等值为0的情况
            nx[j, i] += minima
            ny[j, i] += minima
            alpha[j, i] += minima
            C[j, i] += minima

            # alpha1线段过D点
            alpha1 = ny[j, i]*dy
            C1 = calcC(alpha1, dx, dy, nx[j, i], ny[j, i])
            # alpha2线段过B点
            alpha2 = nx[j, i]*dx
            C2 = calcC(alpha2, dx, dy, nx[j, i], ny[j, i])

            # 判断两个heaviside function的值并计算alpha的值
            if C[j, i] <= min(C1, C2):
                # H1, H2 = 0.0, 0.0
                alpha[j, i] = math.sqrt(2*nx[j, i]*ny[j, i]*dx*dy*C[j, i])
            elif C[j, i] >= max(C1, C2):
                # H1, H2 = 1.0, 1.0
                a = -1.0
                b = 2*(nx[j, i]*dx+ny[j, i]*dy)
                c = -(2*nx[j, i]*ny[j, i]*dx*dy*C[j, i]+(nx[j, i]*dx)**2+(ny[j, i]*dy)**2)
                alpha[j, i] = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
                """
                if (b**2-4*a*c) > 0.0:
                    alpha[j, i] = (-b+math.sqrt(b**2-4*a*c))/(2*a)
                else:
                    alpha[j, i] = 0.000000000001
                """
            elif alpha2 < C[j, i] < alpha1:
                # H1, H2 = 1.0, 0.0
                # alpha[j, i] = (2*nx[j, i]*ny[j, i]*dx*dy*C[j, i]+(nx[j, i]*dx)**2)/(2*nx[j, i]*dx)
                alpha[j, i] = (2*ny[j, i]*dy*C[j, i]+nx[j, i]*dx)/2
            elif alpha1 < C[j, i] < alpha2:
                # H1, H2 = 0.0, 1.0
                # alpha[j, i] = (2*nx[j, i]*ny[j, i]*dx*dy*C[j, i]+(ny[j, i]*dy)**2)/(2*ny[j, i]*dy)
                alpha[j, i] = (2*nx[j, i]*dx*C[j, i]+ny[j, i]*dy)/2

            # 以下代码用于验证界面重构代码的准确性
            if math.fabs(C[j, i] - calcC(alpha[j, i], dx, dy, nx[j, i], ny[j, i])) >0.01:
                print("请注意：重构的alpha[]可能计算有误")
                print(j, i, C[j, i])
                print(calcC(alpha[j, i], dx, dy, nx[j, i], ny[j, i]))

            """
            # 恢复u,v
            u = 1.0
            v = -0.5
            """


    return alpha

