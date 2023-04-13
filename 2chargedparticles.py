import matplotlib.pyplot as plt
import numpy as np

# Inputs for the charged particles
x1 = -5.0 # x-coordinate of charged particle 1
y1 = 0.0 # y-coordinate of charged particle 1
q1 = 1.0 # Charge of particle 1

x2 = 5.0 # x-coordinate of charged particle 2
y2 = 0.0 # y-coordinate of charged particle 2
q2 = -1.0 # Charge of particle 2

# Create a grid of points to evaluate the magnetic field at
X, Y = np.meshgrid(np.linspace(-10,10,100), np.linspace(-10,10,100))
Bx = np.zeros_like(X)
By = np.zeros_like(Y)

# Calculate the magnetic field components at each point on the grid
rx1 = X - x1
ry1 = Y - y1
r1 = np.sqrt(rx1**2 + ry1**2)
r1_cube = r1**3
Bx += q1 * (ry1 / r1_cube)
By += -q1 * (rx1 / r1_cube)

rx2 = X - x2
ry2 = Y - y2
r2 = np.sqrt(rx2**2 + ry2**2)
r2_cube = r2**3
Bx += q2 * (ry2 / r2_cube)
By += -q2 * (rx2 / r2_cube)

# Plot the magnetic field as lines
fig, ax = plt.subplots()
ax.streamplot(X, Y, Bx, By, color='b', linewidth=1, cmap='autumn')
ax.scatter([x1, x2], [y1, y2], c=['r', 'g'], s=100, marker='o', label=['Charged Particle 1', 'Charged Particle 2'])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Magnetic Field between Charged Particles')
ax.legend()
plt.show()
