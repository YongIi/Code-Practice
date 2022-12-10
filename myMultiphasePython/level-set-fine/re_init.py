# 开发人员：liyong
# 开发时间：2022/12/6 11:58

import math
import numpy as np

# reinitialization会导致质量不守恒（尤其是该文件用的格式），要尽量少用

# def sgn(phi,dx):  # epsilon由网格尺寸的2-3倍给定，此处仅给了1倍
#     return phi/math.sqrt(phi**2+dx**2)

def reinit(x,y,dx,dy,dt,nt,phi):
    # 迭代前将phi赋值给phid，后面求出来的phid是reinit后的符号距离函数
    phid = phi.copy()

    # 定义中间变量
    a = np.zeros_like(phi)
    b = np.zeros_like(phi)
    c = np.zeros_like(phi)
    d = np.zeros_like(phi)
    G = np.zeros_like(phi)
    sgn = np.ones_like(phi)
    # subcell临时变量
    deltaphi = np.ones_like(phi)
    temp1 = np.zeros_like(phi)
    temp2 = np.zeros_like(phi)
    temp3 = np.zeros_like(phi)
    temp4 = np.zeros_like(phi)
    temp5 = np.zeros_like(phi)
    gamma = 0.1*dx
    D = np.zeros_like(phi)

    # reinitialization
    for n in range(nt):
        phin = phid.copy()

        # 一阶迎风格式
        a[2:-2, 2:-2] = (phin[2:-2, 2:-2]-phin[2:-2, 1:-3])/dx
        b[2:-2, 2:-2] = (phin[2:-2, 3:-1]-phin[2:-2, 2:-2])/dx
        c[2:-2, 2:-2] = (phin[2:-2, 2:-2]-phin[1:-3, 2:-2])/dy
        d[2:-2, 2:-2] = (phin[3:-1, 2:-2]-phin[2:-2, 2:-2])/dy

        for j in range(2, len(y)-2):
            for i in range(2, len(x) - 2):
                if phi[j, i] > 0.0:  # 必须以原始的phi进行判断
                    sgn[j, i] = 1.0
                    G[j, i] = math.sqrt(max((max(a[j, i], 0.0))**2, (min(b[j, i],0.0))**2) \
                                       +max((max(c[j, i], 0.0))**2, (min(d[j, i],0.0))**2))-1
                elif phi[j, i] < 0.0:
                    sgn[j, i] = -1.0
                    G[j, i] = math.sqrt(max((min(a[j, i], 0.0))**2, (max(b[j, i], 0.0))**2) \
                                       +max((min(c[j, i], 0.0))**2,(max(d[j, i], 0.0))**2))-1
                else:
                    sgn[j, i] = 0.0
                    G[j, i] = 0.0

        # 没有进行亚网格修正
        phid[2:-2, 2:-2] = phin[2:-2, 2:-2] - dt*sgn[2:-2, 2:-2]*G[2:-2, 2:-2]

        # 进行亚网格修正
        temp1[2:-2, 2:-2] = np.sqrt((phi[2:-2, 3:-1]-phi[2:-2, 1:-3])**2+(phi[3:-1, 2:-2]-phi[1:-3, 2:-2])**2)/2.0
        temp2[2:-2, 2:-2] = np.abs(phi[2:-2, 3:-1]-phi[2:-2, 2:-2])
        temp3[2:-2, 2:-2] = np.abs(phi[2:-2, 2:-2]-phi[2:-2, 1:-3])
        temp4[2:-2, 2:-2] = np.abs(phi[3:-1, 2:-2]-phi[2:-2, 2:-2])
        temp5[2:-2, 2:-2] = np.abs(phi[2:-2, 2:-2]-phi[1:-3, 2:-2])

        deltaphi = np.maximum(temp1,np.maximum(temp2,np.maximum(temp3,np.maximum(temp4,np.maximum(temp5,gamma)))))
        D = dx*phi/deltaphi

        for j in range(2, len(y)-2):
            for i in range(2, len(x) - 2):
                if phi[j, i]*phi[j, i-1]<0.0 or phi[j, i]*phi[j, i+1]<0.0 or \
                        phi[j, i]*phi[j-1, i]<0.0 or phi[j, i]*phi[j+1, i]<0.0:
                    phid[j, i] = phin[j, i] - dt/dx*(sgn[j, i]*math.fabs(phin[j, i])-D[j, i])
                # else:
                #     phid[j, i] = phin[j, i] - dt * sgn[j, i] * G[j, i]

        # 更新边界条件
        # phid[1, :] = 2*phid[2, :]-phid[3, :]
        # phid[0, :] = 2*phid[1, :]-phid[2, :]  # 第0行，列是[:]
        # phid[-2, :] = 2*phid[-3, :]-phid[-4, :]
        # phid[-1, :] = 2*phid[-2, :]-phid[-3, :]
        # phid[:, 1] = 2*phid[:, 2]-phid[:, 3]
        # phid[:, 0] = 2*phid[:, 1]-phid[:, 2]
        # phid[:, -2] = 2*phid[:, -3]-phid[:, -4]
        # phid[:, -1] = 2*phid[:, -2]-phid[:, -3]

        phid[0, :] = phid[2, :]  # 第0行，列是[:]
        phid[1, :] = phid[2, :]
        phid[-1, :] = phid[-3, :]
        phid[-2, :] = phid[-3, :]
        phid[:, 0] = phid[:, 2]
        phid[:, 1] = phid[:, 2]
        phid[:, -1] = phid[:, -3]
        phid[:, -2] = phid[:, -3]

        # phid[0, :] = 2*phid[2, :]-phid[4, :]  # 第0行，列是[:]
        # phid[1, :] = 2*phid[2, :]-phid[3, :]
        # phid[-1, :] = 2*phid[-3, :]-phid[-5, :]
        # phid[-2, :] = 2*phid[-3, :]-phid[-4, :]
        # phid[:, 0] = 2*phid[:, 2]-phid[:, 4]
        # phid[:, 1] = 2*phid[:, 2]-phid[:, 3]
        # phid[:, -1] = 2*phid[:, -3]-phid[:, -5]
        # phid[:, -2] = 2*phid[:, -3]-phid[:, -4]

    return phid


