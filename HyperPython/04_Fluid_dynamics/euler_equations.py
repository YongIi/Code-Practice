# solve euler equation using PyClaw

from clawpack import pyclaw
from clawpack import riemann
from matplotlib import animation
import matplotlib.pyplot as plt
# from clawpack.visclaw.JSAnimation import IPython_display
import numpy as np

# A controller, which handles the running, output, and can be used for plotting
claw = pyclaw.Controller()
claw.tfinal = 0.12                    # Simulation end time
claw.keep_copy = True          # Keep solution data in memory for plotting
claw.output_format = None    # Don't write solution data to file
claw.num_output_times = 50  # Write 50 output frames

# print(dir(riemann))

# 指定riemann solver
riemann_solver = riemann.euler_with_efix_1D
claw.solver = pyclaw.ClawSolver1D(riemann_solver)

# 指定BC, use extrapolation boundary conditions, so that waves simply pass out of the domain
claw.solver.all_bcs = pyclaw.BC.extrap

# specify the domain and the grid. Note that each argument to the Domain constructor must be a tuple
domain = pyclaw.Domain( (0.,), (1.,), (500,))

# create a solution object that belongs to the controller and extends over the domain we specified
claw.solution = pyclaw.Solution(claw.solver.num_eqn,domain)

# The initial data is specified in an array named solution.q. 
# The density is contained in q[0,:], the momentum in q[1,:], and the energy in q[2,:]
x=domain.grid.x.centers # grid cell centers
gam = 1.4 # ratio of specific heats

rho_left = 1.0; rho_right = 0.125
p_left = 1.0; p_right = 0.1

claw.solution.q[0,:] = (x<0.5)*rho_left + (x>=0.5)*rho_right
claw.solution.q[1,:] = 0.
claw.solution.q[2,:] = ((x<0.5)*p_left + (x>=0.5)*p_right)/(gam-1.0)

import matplotlib.pyplot as plt
plt.plot(x, claw.solution.q[0,:],'-o')
plt.savefig('Sod shock-tube IC.png')

# specify the ratio of specific heats.
problem_data = claw.solution.problem_data
problem_data['gamma'] = 1.4
problem_data['gamma1'] = 0.4

# run the simulation
claw.run()


# Plotting
fig = plt.figure()
ax = plt.axes(xlim=(0, 1), ylim=(-0.2, 1.2))

frame = claw.frames[0]
pressure = frame.q[0,:]
line, = ax.plot([], [], 'o-', lw=2)

def fplot(frame_number):
    frame = claw.frames[frame_number]
    pressure = frame.q[0,:]
    line.set_data(x,pressure)
    return line,

anim = animation.FuncAnimation(fig, fplot, frames=len(claw.frames), interval=30)
anim.save('sod.gif')

fig2 = plt.figure()
plt.plot(x, claw.solution.q[0,:],lw=3,label='rho')
plt.plot(x, claw.solution.q[1,:],lw=3,label='u')
plt.plot(x, claw.solution.q[2,:],lw=3,label='E')
plt.legend()
plt.savefig('sod.png')





