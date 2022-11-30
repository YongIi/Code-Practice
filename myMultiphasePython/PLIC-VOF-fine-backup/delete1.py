
def calcCstar(nx,ny,u,v,dt,dx,dy,alpha,x,y,C):
    # 定义中间变量
    minima = 0.0001
    CL = np.zeros_like(C)
    CS = np.zeros_like(C)
    CR = np.zeros_like(C)
    Cstar = np.zeros_like(C)

    # 计算出t=star时刻的线段
    nx_star = nx/(1.0+(u-(-u)*dt/dx))
    print("nx_star的尺度是",len(nx_star))
    alpha_star = alpha + (nx*(-u)*dt)/(1.0+(u-(-u)*dt/dx))
    print("alpha_star的尺度是", len(alpha_star))
    print(alpha_star[5,5])
    #myplot.plotValue(x, y, alpha_star)

    for j in range(0, len(y)):
        for i in range(0, len(x)):
            """
            if nx[j, i] < 0:
                nx[j, i] = -nx[j, i]
                u = -u
            if ny[j, i] < 0:
                ny[j, i] = -ny[j, i]
                v = -v

            """

            if  math.fabs(nx[j, i]) > minima or math.fabs(ny[j, i]) > minima:  # 判断是否在界面处
                l1 = calcy(alpha_star[j, i], nx_star[j, i], ny[j, i], u * dt)
                l2 = calcy(alpha_star[j, i], nx_star[j, i], ny[j, i], 0)
                l3 = calcy(alpha_star[j, i], nx_star[j, i], ny[j, i], dx)
                l4 = calcy(alpha_star[j, i], nx_star[j, i], ny[j, i], dx + u * dt)
                s1 = (l1 + l2) * u * dt / 2.0
                s2 = (l2 + l3) * dx / 2.0
                s3 = (l3 + l4) * u * dt / 2.0
                CL[j, i] = max(min(-u * dt / dx, -s1 / (dx * dy)), 0)
                CS[j, i] = min(s2 / (dx * dy), 1.0)
                CR[j, i] = max(min(u * dt / dx, s3 / (dx * dy)), 0)
                # 测试
                if nx[j, i] < 0.0 and ny[j, i] < 0.0:
                    CL[j, i],CR[j, i] = CR[j, i], CL[j, i]
            else:
                if C[j, i] > 1.0 - minima:
                    CL[j, i] = max(-u*dt/dx, 0)
                    CS[j, i] = 1.0 - max(u*dt/dx,0) + min(u*dt/dx,0)
                    CR[j, i] = max(u*dt/dx, 0)
                elif C[j, i] < minima:
                    CL[j, i] = 0.0
                    CS[j, i] = 0.0
                    CR[j, i] = 0.0

            # 恢复u,v
            u = 1.0
            v = -0.5

    Cstar[1:-1, 1:-1] = CS[1:-1, 1:-1] + CR[1:-1, 0:-2] + CL[1:-1, 2:]
    Cstar = np.minimum(1.0, np.maximum(0.0, Cstar))

    # 周期性边界条件
    Cstar[0, :] = Cstar[-2, :]  # 第0行，列是[:]
    Cstar[-1, :] = Cstar[1, :]
    Cstar[:, 0] = Cstar[:, -2]
    Cstar[:, -1] = Cstar[:, 1]

    return Cstar

