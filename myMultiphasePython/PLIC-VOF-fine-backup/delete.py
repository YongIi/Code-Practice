
def calcC_nplus1(nx,ny,u,v,dt,dx,dy,alpha,x,y,C):
    # 定义中间变量
    minima = 0.0001
    CD = np.zeros_like(C)
    CS = np.zeros_like(C)
    CU = np.zeros_like(C)
    C_nplus1 = np.zeros_like(C)

    # 计算出t=n+1时刻的线段
    ny_star = ny / (1.0 + (v - (-v) * dt / dy))
    print("nx_star的尺度是", len(ny_star))
    alpha_star = alpha + (ny * (-v) * dt) / (1.0 + (v - (-v) * dt / dy))
    print("alpha_star的尺度是", len(alpha_star))
    # myplot.plotValue(x, y, alpha_star)

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

            if math.fabs(nx[j, i]) > minima or math.fabs(ny[j, i]) > minima:  # 判断是否在界面处
                #calcx = inversefunc(lambda x: calcy(x, alpha_star[j, i], nx[j, i], ny_star[j, i]))
                l1 = calcy(alpha_star[j, i], nx[j, i], ny_star[j, i], v * dt)
                l2 = calcy(alpha_star[j, i], nx[j, i], ny_star[j, i], 0.0)
                l3 = calcy(alpha_star[j, i], nx[j, i], ny_star[j, i], dy)
                l4 = calcy(alpha_star[j, i], nx[j, i], ny_star[j, i], dy + v * dt)
                s1 = (l1 + l2) * v * dt / 2.0
                s2 = (l2 + l3) * dy / 2.0
                s3 = (l3 + l4) * v * dt / 2.0
                CD[j, i] = max(min(-v * dt / dy, -s1 / (dx * dy)), 0)
                CS[j, i] = min(s2 / (dx * dy), 1.0)
                CU[j, i] = max(min(v * dt / dy, s3 / (dx * dy)), 0)
                # 测试
                if nx[j, i] < 0.0 and ny[j, i] < 0.0:
                    CD[j, i], CU[j, i] = CU[j, i], CD[j, i]
            else:
                if C[j, i] > 1.0 - minima:
                    CD[j, i] = max(-v * dt / dy, 0)
                    CS[j, i] = 1.0 - max(v * dt / dy, 0) + min(v * dt / dy, 0)
                    CU[j, i] = max(v * dt / dy, 0)
                elif C[j, i] < minima:
                    CD[j, i] = 0.0
                    CS[j, i] = 0.0
                    CU[j, i] = 0.0

            # 恢复u,v
            u = 1.0
            v = -0.5

    C_nplus1[1:-1, 1:-1] = CS[1:-1, 1:-1] + CU[0:-2, 1:-1] + CD[2:, 1:-1]
    C_nplus1 = np.minimum(1.0, np.maximum(0.0, C_nplus1))

    # 周期性边界条件
    C_nplus1[0, :] = C_nplus1[-2, :]  # 第0行，列是[:]
    C_nplus1[-1, :] = C_nplus1[1, :]
    C_nplus1[:, 0] = C_nplus1[:, -2]
    C_nplus1[:, -1] = C_nplus1[:, 1]

    return C_nplus1