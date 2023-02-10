# 开发人员：leo
# 开发时间：2023/2/10 16:22
import sympy
#from pyweno import symbolic
import matplotlib.pyplot as plt
import numpy as np

weno_order = 5  # must be odd
k = (weno_order+1)/2

width = 12
size = (width,4)
colors = 'brg'
plt.figure(figsize=size)
x=np.arange(-k+1,k)
y=np.random.rand(len(x))
#y = np.array((1.,1.,1.,0.,0.))
plt.plot(x,y,'ok')
plt.axis((-(k-.5),k-.5,-0.5,2.1))
plt.show()

def stencil_interpolant(x,y,n,offset):
    """Return the polynomial interpolant (of degree n-1)
       through the points (x_j,y_j) for offset <= j <= offset+n-1.
    """
    return np.poly1d(np.polyfit(x[offset:offset+n],y[offset:offset+n],n-1))

def plot_interpolants(x,y,interpolants,axis=None,color='kbrg'):
    if axis is None:
        fig, axis = plt.subplots(figsize=size)
    xc = np.linspace(-0.5,0.5)
    xx = np.linspace(-(k-1),k-1)
    for i, interpolant in enumerate(interpolants):
        axis.plot(xx,interpolant(xx),'-'+color[i])
        axis.plot(xc,interpolant(xc),'-'+color[i],linewidth=5,alpha=0.5)
    axis.plot(x,y,'ok')
    axis.axis((-(k-.5),k-.5,-0.5,2.1));

p_opt = stencil_interpolant(x,y,5,0)
plot_interpolants(x,y,[p_opt])
plt.title('Quartic interpolant')
plt.show()

fig, ax = plt.subplots(3,1,figsize=(width,10))
names = ['left','right','center']
p = []
for i in range(int(k)):
    print(k)
    p.append(stencil_interpolant(x,y,int(k),i))
    plot_interpolants(x,y,[p[i]],axis=ax[i],color=[colors[i]])
    ax[i].set_title(names[i]+' interpolant')
plt.show()
plot_interpolants(x,y,p+[p_opt],color='brgk')
plt.show()

# 计算权重，但是缺少相应的pyweno包
"""
def compute_opt_weights(k,xi):
    """
    Get the optimal weights (gamma) at points xi.
    """
    if not hasattr(xi,'__iter__'): xi = [xi]
    opt_weights = symbolic.optimal_weights(k,xi)
    gamma = {}
    for i, xi_val in enumerate(xi):
        gamma[xi_val] = np.empty(k)
        for j in range(k):
            gamma[xi_val][j] = opt_weights[0][(i,j)]

    return gamma

gamma = compute_opt_weights(k,(-1,0.5,1))

print "$\gamma_{j,-1/2}$:",  gamma[-1]
print "$\gamma_{j,+1/2}$:",  gamma[1]
"""


