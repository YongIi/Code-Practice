# 开发人员：liyong
# 开发时间：2022/12/6 9:45

#  3阶QUICK格式推进phi

import numpy as np

def calcPhi(x,y,dx,dy,dt,u,v,phi):
    #  定义中间变量
    phiR = np.zeros_like(phi)
    phiL = np.zeros_like(phi)
    phiU = np.zeros_like(phi)
    phiD = np.zeros_like(phi)

    phin = phi.copy()

    #  计算网格面通量
    for j in range(2, len(y)-2):
        for i in range(2, len(x)-2):
            if u[j, i] >= 0.0:
                phiR[j, i] =(3*phin[j, i+1]+6*phin[j, i]-phin[j, i-1])/8
                phiL[j, i] =(3*phin[j, i]+6*phin[j, i-1]-phin[j, i-2])/8
            else:
                phiR[j, i] =(3*phin[j, i]+6*phin[j, i+1]-phin[j, i+2])/8
                phiL[j, i] =(3*phin[j, i-1]+6*phin[j, i]-phin[j, i+1])/8

            if v[j, i] >= 0.0:
                phiU[j, i] =(3*phin[j+1, i]+6*phin[j, i]-phin[j-1, i])/8
                phiD[j, i] =(3*phin[j, i]+6*phin[j-1, i]-phin[j-2, i])/8
            else:
                phiU[j, i] =(3*phin[j, i]+6*phin[j+1, i]-phin[j+2, i])/8
                phiD[j, i] =(3*phin[j-1, i]+6*phin[j, i]-phin[j+1, i])/8

    #  时间推进phi
    phi[2:-2, 2:-2] = phin[2:-2, 2:-2] - u[2:-2, 2:-2] * dt / dx * (phiR[2:-2, 2:-2] - phiL[2:-2, 2:-2]) \
                                       - v[2:-2, 2:-2] * dt / dy * (phiU[2:-2, 2:-2] - phiD[2:-2, 2:-2])

    # 更新边界条件
    # phi[1, :] = 2 * phi[2, :] - phi[3, :]
    # phi[0, :] = 2 * phi[1, :] - phi[2, :]  # 第0行，列是[:]
    # phi[-2, :] = 2 * phi[-3, :] - phi[-4, :]
    # phi[-1, :] = 2 * phi[-2, :] - phi[-3, :]
    # phi[:, 1] = 2 * phi[:, 2] - phi[:, 3]
    # phi[:, 0] = 2 * phi[:, 1] - phi[:, 2]
    # phi[:, -2] = 2 * phi[:, -3] - phi[:, -4]
    # phi[:, -1] = 2 * phi[:, -2] - phi[:, -3]

    phi[0, :] = phi[2, :]  # 第0行，列是[:]
    phi[1, :] = phi[2, :]
    phi[-1, :] = phi[-3, :]
    phi[-2, :] = phi[-3, :]
    phi[:, 0] = phi[:, 2]
    phi[:, 1] = phi[:, 2]
    phi[:, -1] = phi[:, -3]
    phi[:, -2] = phi[:, -3]

    # 以下更新边界条件的方式有可能在边界处形成非物理的界面
    # phi[0, :] = 2 * phi[2, :] - phi[4, :]  # 第0行，列是[:]
    # phi[1, :] = 2 * phi[2, :] - phi[3, :]
    # phi[-1, :] = 2 * phi[-3, :] - phi[-5, :]
    # phi[-2, :] = 2 * phi[-3, :] - phi[-4, :]
    # phi[:, 0] = 2 * phi[:, 2] - phi[:, 4]
    # phi[:, 1] = 2 * phi[:, 2] - phi[:, 3]
    # phi[:, -1] = 2 * phi[:, -3] - phi[:, -5]
    # phi[:, -2] = 2 * phi[:, -3] - phi[:, -4]

    return  phi

