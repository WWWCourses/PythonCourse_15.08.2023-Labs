import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

# Create some sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a 2x2 grid for the subplots
fig = plt.figure()

# Define a gridspec to specify subplot sizes
gs = gridspec.GridSpec(2, 2, height_ratios=[2, 1])  # The height ratio [2, 1] ensures the bottom subplot is twice as tall

# Create the top-left subplot
ax1 = plt.subplot(gs[0, 0])
ax1.plot(x, y1)
ax1.set_title('Plot 1')

# Create the top-right subplot
ax2 = plt.subplot(gs[0, 1])
ax2.plot(x, y2)
ax2.set_title('Plot 2')

# Create the bottom subplot that spans both columns
ax3 = plt.subplot(gs[1, :])
ax3.plot(x, y1 + y2)
ax3.set_title('Combined Plot')

# Adjust spacing between subplots
plt.tight_layout()

plt.show()