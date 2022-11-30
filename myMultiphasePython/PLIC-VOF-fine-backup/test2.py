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

            # 计算出t=star时刻的线段
            nx_star = ny[j, i] / (1.0 + (v1 - v0) * dt / dy)
            alpha_star = alpha[j, i] + (ny[j, i] * v0 * dt) / (1.0 + (v1 - v0) * dt / dy)
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
                CU[j, i] = max(u * dt / dx, 0)
            elif C[j, i] < minima:
                CD[j, i] = 0.0
                CS[j, i] = 0.0
                CU[j, i] = 0.0
            else:
                if math.fabs(ny[j, i]) > minima:
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




                if 0:
                #if math.fabs(nx[j, i]) > minima and math.fabs(ny[j, i]) > minima:  # 判断是否在界面处
                    """
                    l1 = calcy(alpha_star, nx_star, ny[j, i], v0 * dt)
                    l2 = calcy(alpha_star, nx_star, ny[j, i], 0)
                    l3 = calcy(alpha_star, nx_star, ny[j, i], dx)
                    l4 = calcy(alpha_star, nx_star, ny[j, i], dx + v1 * dt)
                    s1 = (l1 + l2) * v0 * dt / 2.0
                    s2 = (l2 + l3) * dx / 2.0
                    s3 = (l3 + l4) * v1 * dt / 2.0
                    """
                    OH = calcy(alpha_star, nx_star, ny[j, i], 0.0)
                    OE = calcx(alpha_star, nx_star, ny[j, i], 0.0)
                    if OH > dy and OE > dx:
                        CD[j, i] = max(-v0 * dt / dx, 0)
                        l3 = calcy(alpha_star, nx_star, ny[j, i], dx)
                        x1 = calcx(alpha_star, nx_star, ny[j, i], dy)
                        s2 = dx * dy - (dy - l3) * (dx - x1) / 2.0
                        CS[j, i] = s2 / (dx * dy)
                        l4 = calcy(alpha_star, nx_star, ny[j, i], dx + v1 * dt)
                        s3 = (l3 + l4) * v1 * dt / 2.0
                        CU[j, i] = max(s3 / (dx * dy), 0)
                        if CS[j, i]>0.5:
                            print("判断1",CS[j, i])
                    if OH > dy and OE <= dx:
                        CD[j, i] = max(-v0 * dt / dx, 0)
                        CU[j, i] = 0.0
                        x1 = calcx(alpha_star, nx_star, ny[j, i], dy)
                        #print("x1=",x1)
                        x2 = calcx(alpha_star, nx_star, ny[j, i], 0.0)
                        s2 = (x1 + x2) * dy / 2.0
                        #print("s2=",s2)
                        CS[j, i] = s2 / (dx * dy)
                        if CS[j, i]>0.5:
                            print("C",C[j, i])
                            print("CU", CU[j, i])
                            print("alpha", alpha[j, i])
                            print("判断2",CS[j, i])
                            print("s2", s2)
                            #print("l2", l2)
                            print("x1", x1)
                            print("x2", x2)
                            print("OH", OH)
                            print("OE", OE)
                    if OH <= dy and OE > dx:
                        l1 = calcy(alpha_star, nx_star, ny[j, i], v0 * dt)
                        l2 = calcy(alpha_star, nx_star, ny[j, i], 0)
                        l3 = calcy(alpha_star, nx_star, ny[j, i], dx)
                        l4 = calcy(alpha_star, nx_star, ny[j, i], dx + v1 * dt)
                        s1 = (l1 + l2) * v0 * dt / 2.0
                        s2 = (l2 + l3) * dx / 2.0
                        s3 = (l3 + l4) * v1 * dt / 2.0
                        CD[j, i] = max(-s1 / (dx * dy), 0)
                        CS[j, i] = s2 / (dx * dy)
                        CU[j, i] = max(s3 / (dx * dy), 0)
                        if CS[j, i]>0.5:
                            print("判断3",CS[j, i])
                    if 0<OH <= dy and 0<OE <= dx:
                        l1 = calcy(alpha_star, nx_star, ny[j, i], v0 * dt)
                        l2 = calcy(alpha_star, nx_star, ny[j, i], 0)
                        s1 = (l1 + l2) * v0 * dt / 2.0
                        CD[j, i] = max(-s1 / (dx * dy), 0)
                        x1 = calcx(alpha_star, nx_star, ny[j, i], 0.0)
                        s2 = (l2 * x1) / 2.0
                        CS[j, i] = s2 / (dx * dy)
                        CU[j, i] = 0.0
                        if CS[j, i]>0.5:
                            print("判断4",CS[j, i])
                            print("s2",s2)
                            print("l2", l2)
                            print("x1", x1)
                            print("OH", OH)
                            print("OE", OE)

                    """
                    l1 = calcy(alpha_star, nx_star, ny[j, i], v0 * dt)
                    l2 = calcy(alpha_star, nx_star, ny[j, i], 0)
                    if calcx(alpha_star, nx_star, ny[j, i], 0) > dx:
                        l3 = calcy(alpha_star, nx_star, ny[j, i], dx)
                        l4 = calcy(alpha_star, nx_star, ny[j, i], dx + v1 * dt)
                        s1 = (l1 + l2) * v0 * dt / 2.0
                        s2 = (l2 + l3) * dx / 2.0
                        s3 = (l3 + l4) * v1 * dt / 2.0
                    else:

                    s1 = (l1 + l2) * v0 * dt / 2.0
                    s2 = (l2 + l3) * dx / 2.0
                    s3 = (l3 + l4) * v1 * dt / 2.0


                    CD[j, i] = max(min(-v0*dt/dx, -s1/(dx*dy)), 0)
                    #CD[j, i] = 0.0
                    CS[j, i] = min(s2 / (dx * dy), 1.0)
                    CU[j, i] = max(min(v1 * dt / dx, s3 / (dx * dy)), 0)
                    """
                    # CS[j, i] = max(s1 / (dx * dy), 0)
                    # CS[j, i] = min(s2 / (dx * dy), 1.0)
                    # CD[j, i] = max(s3 / (dx * dy), 0)
                    # CS[j, i] = C[j, i]- CD[j, i] - CS[j, i]
                    # 测试
                    # print("good")
                    # print(flag)
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