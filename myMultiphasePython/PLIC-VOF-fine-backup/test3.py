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

            # 计算出t=star时刻的线段
            nx_star = nx[j, i] / (1.0 + (u1 - u0) * dt / dx)
            alpha_star = alpha[j, i] + (nx[j, i] * u0 * dt) / (1.0 + (u1 - u0) * dt / dx)
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
                if math.fabs(nx[j, i]) > minima:
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




                if 0:
                #if math.fabs(nx[j, i]) > minima and math.fabs(ny[j, i]) > minima:  # 判断是否在界面处
                    """
                    l1 = calcy(alpha_star, nx_star, ny[j, i], u0 * dt)
                    l2 = calcy(alpha_star, nx_star, ny[j, i], 0)
                    l3 = calcy(alpha_star, nx_star, ny[j, i], dx)
                    l4 = calcy(alpha_star, nx_star, ny[j, i], dx + u1 * dt)
                    s1 = (l1 + l2) * u0 * dt / 2.0
                    s2 = (l2 + l3) * dx / 2.0
                    s3 = (l3 + l4) * u1 * dt / 2.0
                    """
                    OH = calcy(alpha_star, nx_star, ny[j, i], 0.0)
                    OE = calcx(alpha_star, nx_star, ny[j, i], 0.0)
                    if OH > dy and OE > dx:
                        CL[j, i] = max(-u0 * dt / dx, 0)
                        l3 = calcy(alpha_star, nx_star, ny[j, i], dx)
                        x1 = calcx(alpha_star, nx_star, ny[j, i], dy)
                        s2 = dx * dy - (dy - l3) * (dx - x1) / 2.0
                        CS[j, i] = s2 / (dx * dy)
                        l4 = calcy(alpha_star, nx_star, ny[j, i], dx + u1 * dt)
                        s3 = (l3 + l4) * u1 * dt / 2.0
                        CR[j, i] = max(s3 / (dx * dy), 0)
                        if CS[j, i]>0.5:
                            print("判断1",CS[j, i])
                    if OH > dy and OE <= dx:
                        CL[j, i] = max(-u0 * dt / dx, 0)
                        CR[j, i] = 0.0
                        x1 = calcx(alpha_star, nx_star, ny[j, i], dy)
                        #print("x1=",x1)
                        x2 = calcx(alpha_star, nx_star, ny[j, i], 0.0)
                        s2 = (x1 + x2) * dy / 2.0
                        #print("s2=",s2)
                        CS[j, i] = s2 / (dx * dy)
                        if CS[j, i]>0.5:
                            print("C",C[j, i])
                            print("CR", CR[j, i])
                            print("alpha", alpha[j, i])
                            print("判断2",CS[j, i])
                            print("s2", s2)
                            #print("l2", l2)
                            print("x1", x1)
                            print("x2", x2)
                            print("OH", OH)
                            print("OE", OE)
                    if OH <= dy and OE > dx:
                        l1 = calcy(alpha_star, nx_star, ny[j, i], u0 * dt)
                        l2 = calcy(alpha_star, nx_star, ny[j, i], 0)
                        l3 = calcy(alpha_star, nx_star, ny[j, i], dx)
                        l4 = calcy(alpha_star, nx_star, ny[j, i], dx + u1 * dt)
                        s1 = (l1 + l2) * u0 * dt / 2.0
                        s2 = (l2 + l3) * dx / 2.0
                        s3 = (l3 + l4) * u1 * dt / 2.0
                        CL[j, i] = max(-s1 / (dx * dy), 0)
                        CS[j, i] = s2 / (dx * dy)
                        CR[j, i] = max(s3 / (dx * dy), 0)
                        if CS[j, i]>0.5:
                            print("判断3",CS[j, i])
                    if 0<OH <= dy and 0<OE <= dx:
                        l1 = calcy(alpha_star, nx_star, ny[j, i], u0 * dt)
                        l2 = calcy(alpha_star, nx_star, ny[j, i], 0)
                        s1 = (l1 + l2) * u0 * dt / 2.0
                        CL[j, i] = max(-s1 / (dx * dy), 0)
                        x1 = calcx(alpha_star, nx_star, ny[j, i], 0.0)
                        s2 = (l2 * x1) / 2.0
                        CS[j, i] = s2 / (dx * dy)
                        CR[j, i] = 0.0
                        if CS[j, i]>0.5:
                            print("判断4",CS[j, i])
                            print("s2",s2)
                            print("l2", l2)
                            print("x1", x1)
                            print("OH", OH)
                            print("OE", OE)

                    """
                    l1 = calcy(alpha_star, nx_star, ny[j, i], u0 * dt)
                    l2 = calcy(alpha_star, nx_star, ny[j, i], 0)
                    if calcx(alpha_star, nx_star, ny[j, i], 0) > dx:
                        l3 = calcy(alpha_star, nx_star, ny[j, i], dx)
                        l4 = calcy(alpha_star, nx_star, ny[j, i], dx + u1 * dt)
                        s1 = (l1 + l2) * u0 * dt / 2.0
                        s2 = (l2 + l3) * dx / 2.0
                        s3 = (l3 + l4) * u1 * dt / 2.0
                    else:

                    s1 = (l1 + l2) * u0 * dt / 2.0
                    s2 = (l2 + l3) * dx / 2.0
                    s3 = (l3 + l4) * u1 * dt / 2.0


                    CL[j, i] = max(min(-u0*dt/dx, -s1/(dx*dy)), 0)
                    #CL[j, i] = 0.0
                    CS[j, i] = min(s2 / (dx * dy), 1.0)
                    CR[j, i] = max(min(u1 * dt / dx, s3 / (dx * dy)), 0)
                    """
                    # CL[j, i] = max(s1 / (dx * dy), 0)
                    # CS[j, i] = min(s2 / (dx * dy), 1.0)
                    # CR[j, i] = max(s3 / (dx * dy), 0)
                    # CS[j, i] = C[j, i]- CR[j, i] - CL[j, i]
                    # 测试
                    # print("good")
                    # print(flag)
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