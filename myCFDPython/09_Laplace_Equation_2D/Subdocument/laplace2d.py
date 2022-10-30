
# Laplace Equation 2D

import numpy
# from matplotlib import pyplot, cm

def laplace2d(p, y, dx, dy, l1norm_target):  # l1norm_target: tolerance -> required error
    l1norm = 1
    pn = numpy.empty_like(p)  # 返回一个与给定数组相同形状和类型的新数组。其值是任意的

    # solve the discretized form of governing equations
    while l1norm > l1norm_target:
        pn = p.copy()
        p[1:-1, 1:-1] = (dy**2 * (pn[1:-1, 2:] + pn[1:-1, 0:-2]) \
                       + dx**2 * (pn[2:, 1:-1] + pn[0:-2, 1:-1])) / (2 * (dx**2 + dy**2))
        # 更新边界条件
        p[:, 0] = 0  # p = 0 @ x = 0
        p[:, -1] = y  # p = y @ x = 2
        p[0, :] = p[1, :]  # dp/dy = 0 @ y = 0
        p[-1, :] = p[-2, :]  # dp/dy = 0 @ y = 1

        # calulation of error magnitude
        l1norm = (numpy.sum(numpy.abs(p[:]) - numpy.abs(pn[:])) /
                  numpy.sum(numpy.abs(pn[:])))

        l1norm2 = numpy.sum(numpy.abs(p[:] - pn[:])) / numpy.sum(numpy.abs(pn[:]))

        print(l1norm == l1norm2)  # always True this case

    return p