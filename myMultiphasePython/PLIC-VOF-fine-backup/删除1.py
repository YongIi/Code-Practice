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
                            #"""
                else:
                    if math.fabs(nx[j, i]) > minima and math.fabs(ny[j, i]) < minima:
                        CU[j, i] = max(C[j, i]*(dx*dy)/dy*v1*dt/(dx*dy), 0)
                        CD[j, i] = max(-C[j, i]*(dx*dy)/dy*v0*dt/(dx*dy), 0)
                        CS[j, i] = C[j, i]