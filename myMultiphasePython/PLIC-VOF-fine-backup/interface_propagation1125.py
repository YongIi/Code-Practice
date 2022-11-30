# 开发人员：leo
# 开发时间：2022/11/16 15:59

import myplot
import numpy as np
import math
# from pynverse import inversefunc  # 计算反函数的库

def calcy(alpha, nx, ny, x):  ## 传参时传入nx[j, i]，alpha[j, i]
    ny += 0.00001
    y = (alpha - nx*x)/ny
    return y

def calcx(alpha, nx, ny, y):
    nx += 0.00001
    x = (alpha-ny*y)/nx
    return x

def calcCstar(nx,ny,u,v,dt,dx,dy,alpha,x,y,C):
    # 定义中间变量
    minima = 0.001
    CL = np.zeros_like(C)
    CS = np.zeros_like(C)
    CR = np.zeros_like(C)
    Cstar = np.zeros_like(C)

    # 计算出t=star时刻的线段
    """
    nx_star = nx/(1.0+(u-(-u)*dt/dx))
    print("nx_star的尺度是",len(nx_star))
    alpha_star = alpha + (nx*(-u)*dt)/(1.0+(u-(-u)*dt/dx))
    print("alpha_star的尺度是", len(alpha_star))
    print(alpha_star[5,5])
    #myplot.plotValue(x, y, alpha_star)
    # myplot.plotValue(x, y, nx_star)
    """

    for j in range(0, len(y)):
        for i in range(0, len(x)):
            u0 = u
            u1 = u
            #print(nx[j, i])
            if nx[j, i] < 0.0:
                flag = 1
                u0, u1 = -u1, -u0
                # print("反向")
            else:
                flag = 0

            if nx[j, i] < 0:
                nx[j, i] = -nx[j, i]
                #u = -u
            if ny[j, i] < 0:
                ny[j, i] = -ny[j, i]
                v = -v

            #print("u=",u1)


            """
            if nx[j, i] < 0 and ny[j, i] < 0:
                nx[j, i] = -nx[j, i]
                ny[j, i] = -ny[j, i]
                u = -u
                v = -v
            if nx[j, i] < 0 and ny[j, i] > 0:
                nx[j, i] = -nx[j, i]
                u = -u
            if nx[j, i] > 0 and ny[j, i] < 0:
                ny[j, i] = -ny[j, i]
                v = -v
            """

            # if 1:
            #if alpha[j, i] > 0.0:
            #if minima < C[j, i] < 1.0 +minima:
            if C[j, i] > 1.0 - minima:
                CL[j, i] = max(-u * dt / dx, 0)
                # CL[j, i] = 0.0
                CS[j, i] = 1.0 - max(u * dt / dx, 0) + min(u * dt / dx, 0)
                CR[j, i] = max(u * dt / dx, 0)
            elif C[j, i] < minima:
                CL[j, i] = 0.0
                CS[j, i] = 0.0
                CR[j, i] = 0.0
            else:
                if math.fabs(ny[j, i]) < minima:
                #if math.fabs(nx[j, i]) > minima and math.fabs(ny[j, i]) <= 0.5*math.fabs(nx[j, i]):
                    if u1 > 0.0:
                        CL[j, i] = max(-u0 * dt / dx, 0)
                        x1 = C[j, i] * dx * dy / dy
                        if (x1 + u1 * dt >= dx):
                            CS[j, i] = 1.0 - max(u0 * dt / dx, 0)
                            CR[j, i] = (x1 + u1 * dt - dx) / dx
                        else:
                            CS[j, i] = 1.0 - max(u0 * dt / dx, 0) - (dx - (x1 + u1 * dt)) / dx
                            CR[j, i] = 0.0
                    else:
                        CR[j, i] = 0.0
                        x1 = C[j, i] * dx * dy / dy
                        x2 = x1 + u1*dt
                        if x2 < 0.0:
                            CL[j, i] = C[j, i]
                            CS[j, i] = 0.0
                        else:
                            s = x2*dy
                            CS[j, i] = s/(dx*dy)
                            CL[j, i] = C[j, i] - CS[j, i]
                            #"""
                elif math.fabs(nx[j, i]) < minima:
                    CR[j, i] = max(C[j, i] * (dx * dy) / dx * u1 * dt / (dx * dy), 0)
                    CL[j, i] = max(-C[j, i] * (dx * dy) / dx * u0 * dt / (dx * dy), 0)
                    CS[j, i] = C[j, i] - CR[j, i] - CL[j, i]
                else:
                    """
                    # 计算出t=star时刻的线段
                    nx_star = nx[j, i] / (1.0 + (u1 - u0) * dt / dx)
                    alpha_star = alpha[j, i] + (nx[j, i] * u0 * dt) / (1.0 + (u1 - u0) * dt / dx)


                    OH = calcy(alpha_star, nx_star, ny[j, i], 0.0)
                    CL[j, i] = max(-min(OH, dy)*u0*dt/(dx*dy), 0.0)
                    BF = calcy(alpha_star, nx_star, ny[j, i], dx)
                    CR[j, i] = max(max(BF,0.0)*u1*dt/(dx*dy),0.0)
                    CS[j, i] = C[j, i] - CR[j, i] - CL[j, i]
                    """
                    OH = calcy(alpha[j, i], nx[j, i], ny[j, i], 0.0)
                    CL[j, i] = max(-min(OH, dy) * u0 * dt / (dx * dy), 0.0)
                    BF = calcy(alpha[j, i], nx[j, i], ny[j, i], dx)
                    CR[j, i] = max(max(BF, 0.0) * u1 * dt / (dx * dy), 0.0)
                    CS[j, i] = C[j, i] - CR[j, i] - CL[j, i]

                    pass








                if flag:
                    # pass
                    # print("bad")
                    # print("flag的值",flag)
                    CL[j, i], CR[j, i] = CR[j, i], CL[j, i]
                    # print("u=",u0)
                    # print("CL,CR,CS",CL[j, i],CR[j, i],CS[j, i])
                    # print("CR",CR[j, i])




    #myplot.plotContour(x, y, CS)
    #myplot.plotContour(x,y,CR)
    Cstar[1:-1, 1:-1] = CS[1:-1, 1:-1] + CR[1:-1, 0:-2] + CL[1:-1, 2:]
    Cstar = np.minimum(1.0, np.maximum(0.0, Cstar))

    # 周期性边界条件
    Cstar[0, :] = Cstar[-2, :]  # 第0行，列是[:]
    Cstar[-1, :] = Cstar[1, :]
    Cstar[:, 0] = Cstar[:, -2]
    Cstar[:, -1] = Cstar[:, 1]

    return Cstar


def calcC_nplus1(nx,ny,u,v,dt,dx,dy,alpha,x,y,C):
    # 定义中间变量
    minima = 0.001
    CD = np.zeros_like(C)
    CS = np.zeros_like(C)
    CU = np.zeros_like(C)
    C_nplus1 = np.zeros_like(C)

    # 计算出t=star时刻的线段
    """
    nx_star = nx/(1.0+(u-(-u)*dt/dx))
    print("nx_star的尺度是",len(nx_star))
    alpha_star = alpha + (nx*(-u)*dt)/(1.0+(u-(-u)*dt/dx))
    print("alpha_star的尺度是", len(alpha_star))
    print(alpha_star[5,5])
    #myplot.plotValue(x, y, alpha_star)
    # myplot.plotValue(x, y, nx_star)
    """

    for j in range(0, len(y)):
        for i in range(0, len(x)):
            v0 = v
            v1 = v
            #print(nx[j, i])
            if ny[j, i] < 0.0:
                flag = 1
                v0, v1 = -v1, -v0
                # print("反向")
            else:
                flag = 0

            if nx[j, i] < 0:
                nx[j, i] = -nx[j, i]
                #u = -u
            if ny[j, i] < 0:
                ny[j, i] = -ny[j, i]
                #v = -v

            #print("u=",v1)


            """
            if nx[j, i] < 0 and ny[j, i] < 0:
                nx[j, i] = -nx[j, i]
                ny[j, i] = -ny[j, i]
                u = -u
                v = -v
            if nx[j, i] < 0 and ny[j, i] > 0:
                nx[j, i] = -nx[j, i]
                u = -u
            if nx[j, i] > 0 and ny[j, i] < 0:
                ny[j, i] = -ny[j, i]
                v = -v
            """

            # if 1:
            #if alpha[j, i] > 0.0:
            #if minima < C[j, i] < 1.0 +minima:
            if C[j, i] > 1.0 - minima:
                CD[j, i] = max(-v * dt / dy, 0)
                # CS[j, i] = 0.0
                CS[j, i] = 1.0 - max(v * dt / dy, 0) + min(v * dt / dy, 0)
                CU[j, i] = max(v * dt / dx, 0)
            elif C[j, i] < minima:
                CD[j, i] = 0.0
                CS[j, i] = 0.0
                CU[j, i] = 0.0
            else:
                if math.fabs(nx[j, i]) < minima:
                #if math.fabs(nx[j, i]) > minima and math.fabs(ny[j, i]) <= 0.5*math.fabs(nx[j, i]):
                    if v1 > 0.0:
                        CD[j, i] = max(-v0 * dt / dy, 0)
                        y1 = C[j, i] * dx * dy / dx
                        if (y1 + v1 * dt >= dy):
                            CS[j, i] = 1.0 - max(v0 * dt / dy, 0)
                            CU[j, i] = (y1 + v1 * dt - dy) / dy
                        else:
                            CS[j, i] = 1.0 - max(v0 * dt / dy, 0) - (dy - (y1 + v1 * dt)) / dy
                            CU[j, i] = 0.0
                    else:
                        CU[j, i] = 0.0
                        y1 = C[j, i] * dx * dy / dx
                        y2 = y1 + v1*dt
                        if y2 < 0.0:
                            CD[j, i] = C[j, i]
                            CS[j, i] = 0.0
                        else:
                            s = y2*dx
                            CS[j, i] = s/(dx*dy)
                            CD[j, i] = C[j, i] - CS[j, i]
                            #"""
                elif math.fabs(ny[j, i]) < minima:
                    CU[j, i] = max(C[j, i] * (dx * dy) / dy * v1 * dt / (dx * dy), 0)
                    CD[j, i] = max(-C[j, i] * (dx * dy) / dy * v0 * dt / (dx * dy), 0)
                    CS[j, i] = C[j, i] - CU[j, i] - CD[j, i]
                else:
                    """

                    # 计算出t=star时刻的线段
                    ny_star = ny[j, i] / (1.0 + (v1 - v0) * dt / dy)
                    alpha_star = alpha[j, i] + (ny[j, i] * v0 * dt) / (1.0 + (v1 - v0) * dt / dy)

                    OH = calcy(alpha_star, nx_star, ny[j, i], 0.0)
                    CL[j, i] = max(-min(OH, dy) * u0 * dt / (dx * dy), 0.0)
                    BF = calcy(alpha_star, nx_star, ny[j, i], dx)
                    CR[j, i] = max(max(BF, 0.0) * u1 * dt / (dx * dy), 0.0)
                    CS[j, i] = C[j, i] - CR[j, i] - CL[j, i]

                    """
                    #OH = calcy(alpha[j, i], nx[j, i], ny[j, i], 0.0)
                    AB = calcx(alpha[j, i], nx[j, i], ny[j, i], 0.0)
                    #CL[j, i] = max(-min(OH, dy) * u0 * dt / (dx * dy), 0.0)
                    CD[j, i] = max(-min(AB, dx)*v0*dt/(dx*dy),0.0)
                    DG = calcx(alpha[j, i], nx[j, i], ny[j, i], dy)
                    CU[j, i] = max(max(DG,0.0)*v1*dt/(dx*dy),0.0)
                    CS[j, i] = C[j, i] - CD[j, i] - CU[j, i]


                if flag:
                    # pass
                    # print("bad")
                    # print("flag的值",flag)
                    CD[j, i], CU[j, i] = CU[j, i], CD[j, i]
                    # print("u=",v0)
                    # print("CS,CD,CS",CS[j, i],CD[j, i],CS[j, i])
                    # print("CD",CD[j, i])




    #myplot.plotContour(x, y, CS)
    #myplot.plotContour(x,y,CD)
    C_nplus1[1:-1, 1:-1] = CS[1:-1, 1:-1] + CU[0:-2, 1:-1] + CD[2:, 1:-1]
    C_nplus1 = np.minimum(1.0, np.maximum(0.0, C_nplus1))

    # 周期性边界条件
    C_nplus1[0, :] = C_nplus1[-2, :]  # 第0行，列是[:]
    C_nplus1[-1, :] = C_nplus1[1, :]
    C_nplus1[:, 0] = C_nplus1[:, -2]
    C_nplus1[:, -1] = C_nplus1[:, 1]

    return C_nplus1