import matplotlib.pyplot as plt
import numpy as np

N = 3 # Number of charged particles
x = np.array([1, 2, 3, 4, 5]) # x-coordinates of charged particles
y = np.array([1, 2, 3, 4, 5]) # y-coordinates of charged particles
q = np.array([1, -1, 1, -1, 1]) # Charges of particles

# Create a grid of points to evaluate the magnetic field at
X, Y = np.meshgrid(np.linspace(-10,10,100), np.linspace(-10,10,100))
Bx = np.zeros_like(X)
By = np.zeros_like(Y)

# Calculate the magnetic field components at each point on the grid
for i in range(N):
    rx = X - x[i]
    ry = Y - y[i]
    r = np.sqrt(rx**2 + ry**2)
    r_cube = r**3
    Bx += q[i] * (ry / r_cube)
    By += -q[i] * (rx / r_cube)

# Plot the magnetic field as lines
fig, ax = plt.subplots()
ax.streamplot(X, Y, Bx, By, color='b', linewidth=1, cmap='autumn')
ax.scatter(x, y, color='r', s=100, marker='o', label='Charged Particles')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Magnetic Field and Charged Particles')
ax.legend()
plt.show()
