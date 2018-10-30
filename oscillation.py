from __future__ import division
import numpy as np
import  matplotlib.pyplot  as plt
#harmonic oscillator in python 
# helped me alot > https://flothesof.github.io/harmonic-oscillator-three-methods-solution.html
# Parameters for the simulation
ST = 1/1000
# Length of the simulation in seconds
duration = 1
# Physical parameters
M = 1.0
k = 2 

# Initialization
t = np.linspace(0, duration, int(duration / ST) + 1)
ddtheta = np.zeros(len(t))
dtheta = np.zeros(len(t))
theta = np.zeros(len(t))

ddtheta[0] = 0.0
dtheta[0] = 0.0
theta[0] = 1.0

# Main loop
for k in range(1, len(t)):
    ddtheta[k] = (1 / M) * (k * (0 - theta[k-1]))
    dtheta[k] = dtheta[k-1] + ddtheta[k] * ST 
    theta[k] = theta[k-1] + dtheta[k] * ST 

plt.figure()
plt.plot(t, theta, color='red')
# Axis  labels
plt.xlabel('t')
plt.ylabel('')
plt.show()