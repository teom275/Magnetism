import numpy as np
import matplotlib.pyplot as plt

# Define the Cartesian coordinates of the point in question
x = 1.0  # x-coordinate
y = 0.5  # y-coordinate

# Define the parameters of the two charged particles
q1 = 1.0  # charge of particle 1
v1 = 1.0  # velocity of particle 1
x1 = 0.0  # x-coordinate of particle 1
y1 = 0.0  # y-coordinate of particle 1

q2 = -1.0  # charge of particle 2
v2 = 0.5  # velocity of particle 2
x2 = 1.0  # x-coordinate of particle 2
y2 = 0.0  # y-coordinate of particle 2

# Calculate the magnetic field at the point in question due to the two charged particles
mu0 = 4 * np.pi * 10**-7  # permeability of free space
r1 = np.sqrt((x - x1)**2 + (y - y1)**2)
r2 = np.sqrt((x - x2)**2 + (y - y2)**2)

numerator1 = q1 * v1 * (y - y1)
denominator1 = (r1**2 + (y - y1)**2)**1.5
B1x = (mu0 / (4 * np.pi)) * numerator1 / denominator1

numerator2 = q2 * v2 * (y - y2)
denominator2 = (r2**2 + (y - y2)**2)**1.5
B2x = (mu0 / (4 * np.pi)) * numerator2 / denominator2

numerator1 = q1 * v1 * (x - x1)
denominator1 = (r1**2 + (x - x1)**2)**1.5
B1y = -(mu0 / (4 * np.pi)) * numerator1 / denominator1

numerator2 = q2 * v2 * (x - x2)
denominator2 = (r2**2 + (x - x2)**2)**1.5
B2y = -(mu0 / (4 * np.pi)) * numerator2 / denominator2

Bx = B1x + B2x
By = B1y + B2y

# Create a Cartesian plot
plt.figure()
plt.quiver(x, y, Bx, By, angles='xy', scale_units='xy', scale=1, color='b', label='B-field')

# Set the title and legend
plt.title('Magnetic Field in Cartesian Coordinates')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Show the Cartesian plot
plt.show()
