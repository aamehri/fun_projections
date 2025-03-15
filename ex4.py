import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Parameters
duration = 5  # seconds
sample_rate = 100  # samples per second
frequency = 1  # Hz

# Generate time array
time = np.arange(0, duration, 1/sample_rate)

# Signal with increasing then decreasing amplitude
amplitude = np.concatenate((np.linspace(0, 1, len(time)//2), np.linspace(1, 0, len(time)//2)))

# Generate signal
signal = amplitude * np.exp(2j * np.pi * frequency * time)

# Extract real and imaginary parts
real_part = np.real(signal)
imag_part = np.imag(signal)

# Create figure and single 3D axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Function to update the plot for each frame
def update(frame):
    ax.clear()  # Clear previous frame

    # Plot the signal moving around an axis (real vs imaginary vs time)
    ax.plot(real_part[:frame], imag_part[:frame], time[:frame], 'g', label='Signal (3D)')

    # Project circular motion onto xy-plane (real vs imaginary)
    ax.plot(real_part[:frame], imag_part[:frame], zs=0, zdir='z', color='b', label='Circular Projection (2D)')

    # Project sine motion vertically along time axis (time vs real)
    ax.plot(np.zeros(frame), real_part[:frame], zs=time[:frame], zdir='y', color='r', label='Sine Projection (Aligned)')

    # Project cosine motion vertically along time axis (time vs imaginary)
    ax.plot(imag_part[:frame], np.zeros(frame), zs=time[:frame], zdir='x', color='m', label='Cosine Projection (Aligned)')

    # Set labels and title
    ax.set_title('Signal with Aligned Sine and Cosine Projections')
    ax.set_xlabel('Real')
    ax.set_ylabel('Imaginary')
    ax.set_zlabel('Time')

    # Add legend for clarity
    ax.legend()

    # Adjust view for optimal visualization
    ax.view_init(elev=30, azim=45)

# Create animation
ani = FuncAnimation(fig, update, frames=len(time), interval=20, repeat=False)

plt.show()
