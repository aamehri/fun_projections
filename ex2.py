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
fig = plt.figure(figsize=(15, 6))

# Subplots for real, imaginary, circular projections, and back circular projection on time axis
ax1 = fig.add_subplot(141, projection='3d')
ax2 = fig.add_subplot(142, projection='3d')
ax3 = fig.add_subplot(143, projection='3d')
ax4 = fig.add_subplot(144, projection='3d')


# Function to update plot
def update(frame):
    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()

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

    # Circular back projection (tilted)
    ax3.plot(real_part[:frame], imag_part[:frame], time[:frame], 'g')  # Tilted by adding time to z-axis
    ax3.set_title('Circular Back Projection (Tilted)')
    ax3.set_xlabel('Real')
    ax3.set_ylabel('Imaginary')
    ax3.set_zlabel('Time')

    # Back circular projection on time axis
    ax4.plot(time[:frame], real_part[:frame], imag_part[:frame], 'm')
    ax4.set_title('Back Circular Projection on Time Axis')
    ax4.set_xlabel('Time')
    ax4.set_ylabel('Real')
    ax4.set_zlabel('Imaginary')


# Animate the plot
ani = animation.FuncAnimation(fig, update, frames=len(time), interval=20, repeat=False)

plt.show()
