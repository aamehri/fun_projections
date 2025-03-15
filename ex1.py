import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Parameters
duration = 5  # seconds
sample_rate = 100  # samples per second
frequency = 1  # Hz

# Generate time array
time = np.arange(0, duration, 1 / sample_rate)

# Signal with increasing then decreasing amplitude
amplitude = np.concatenate((np.linspace(0, 1, len(time) // 2), np.linspace(1, 0, len(time) // 2)))

# Generate signal
signal = amplitude * np.exp(2j * np.pi * frequency * time)

# Extract real and imaginary parts
real_part = np.real(signal)
imag_part = np.imag(signal)

# Create figure
fig = plt.figure(figsize=(10, 6))

# Subplots for real, imaginary, and circular projections
ax1 = fig.add_subplot(131, projection='3d')
ax2 = fig.add_subplot(132, projection='3d')
ax3 = fig.add_subplot(133, projection='3d')


# Function to update plot
def update(frame):
    ax1.clear()
    ax2.clear()
    ax3.clear()

    # Real plane projection
    ax1.plot(time[:frame], np.zeros(frame), real_part[:frame], 'b')
    ax1.set_title('Real Plane Projection')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Imaginary')
    ax1.set_zlabel('Real')

    # Imaginary plane projection
    ax2.plot(time[:frame], imag_part[:frame], np.zeros(frame), 'r')
    ax2.set_title('Imaginary Plane Projection')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Imaginary')
    ax2.set_zlabel('Real')

    # Circular back projection
    ax3.plot(real_part[:frame], imag_part[:frame], np.zeros(frame), 'g')
    ax3.set_title('Circular Back Projection')
    ax3.set_xlabel('Real')
    ax3.set_ylabel('Imaginary')
    ax3.set_zlabel('Time')

    ax3.set_zlim(-1, 1)  # To keep the z-axis consistent


# Animate the plot
ani = animation.FuncAnimation(fig, update, frames=len(time), interval=20, repeat=False)

plt.show()
